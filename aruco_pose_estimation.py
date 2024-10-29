import cv2
import numpy as np

# Load camera calibration parameters
camera_calibration_parameters_filename = 'calibration_data.yaml'  
cv_file = cv2.FileStorage(camera_calibration_parameters_filename, cv2.FILE_STORAGE_READ)
mtx = cv_file.getNode('camera_matrix').mat()
dst = cv_file.getNode('distortion_coefficients').mat()
cv_file.release()

# ArUco dictionary and parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h11)
aruco_params = cv2.aruco.DetectorParameters()  # Create detector parameters
detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

# Side length of the ArUco marker in meters
aruco_marker_side_length = 0.0785

# Set object points for the corners of the marker
obj_points = np.array([
    [-aruco_marker_side_length / 2, aruco_marker_side_length / 2, 0],  # Top-left
    [aruco_marker_side_length / 2, aruco_marker_side_length / 2, 0],   # Top-right
    [aruco_marker_side_length / 2, -aruco_marker_side_length / 2, 0],  # Bottom-right
    [-aruco_marker_side_length / 2, -aruco_marker_side_length / 2, 0]  # Bottom-left
], dtype=np.float32)

# Start the video stream
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect ArUco markers in the video frame
    corners, marker_ids, rejected = detector.detectMarkers(frame)

    # If at least one marker is detected
    if marker_ids is not None:
        # Draw detected markers
        cv2.aruco.drawDetectedMarkers(frame, corners, marker_ids)

        for i in range(len(marker_ids)):
            # Use solvePnP to estimate the pose
            success, rvec, tvec = cv2.solvePnP(obj_points, corners[i], mtx, dst)

            # Check if the pose estimation was successful
            if success:
                # Ensure rvec and tvec are in the correct shape (1x3 or 3x1)
                rvec = rvec.reshape(3)  # Ensuring rvec is 1x3
                tvec = tvec.reshape(3)  # Ensuring tvec is 1x3

                # Draw axes for each marker using drawFrameAxes
                cv2.drawFrameAxes(frame, mtx, dst, rvec, tvec, aruco_marker_side_length * 1.5, 2)

                # Print translation and rotation vectors
                print(f"Marker ID: {marker_ids[i][0]}")
                print(f"Translation vector: {tvec.ravel()}")
                print(f"Rotation vector: {rvec.ravel()}")
                print()
            else:
                print(f"Pose estimation failed for marker ID: {marker_ids[i][0]}")

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close windows
cap.release()
cv2.destroyAllWindows()