import numpy as np
import cv2 as cv
import glob

# Termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points, like (0,0,0), (1,0,0), (2,0,0), ..., (7,5,0)
objp = np.zeros((6 * 8, 3), np.float32)  # 6 rows and 8 columns
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)  # 8 internal corners in x and 6 in y

# Arrays to store object points and image points from all the images
objpoints = []  # 3D point in real-world space
imgpoints = []  # 2D points in image plane

# Load images
images = glob.glob('camera_calibration_images/*.jpg')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chessboard corners (8x6 internal corners)
    ret, corners = cv.findChessboardCorners(gray, (8, 6), None)

    # If found, add object points, image points (after refining them)
    if ret:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (8, 6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)

cv.destroyAllWindows()

# Perform camera calibration if enough points are found
if len(objpoints) > 0 and len(imgpoints) > 0:
    h, w = gray.shape[:2]
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, (w, h), None, None)

    # Output calibration results
    print("Camera matrix:\n", mtx)
    print("Distortion coefficients:\n", dist)

    # Save the calibration results to a YAML file
    cv_file = cv.FileStorage('calibration_data.yaml', cv.FILE_STORAGE_WRITE)
    cv_file.write('camera_matrix', mtx)
    cv_file.write('distortion_coefficients', dist)
    cv_file.write('rotation_vectors', rvecs)
    cv_file.write('translation_vectors', tvecs)
    cv_file.release()

    print("Camera calibration data saved to 'calibration_data.yaml'.")
else:
    print("No valid checkerboard patterns detected. Calibration could not be performed.")