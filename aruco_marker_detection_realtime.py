import cv2

# Set up the ArUco detector for AprilTag 36h11
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h11)
parameters = cv2.aruco.DetectorParameters()
parameters.adaptiveThreshWinSizeMin = 3
parameters.adaptiveThreshWinSizeMax = 23
parameters.adaptiveThreshWinSizeStep = 10
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Open video capture (0 for webcam, or provide a file path for a video)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture each frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect markers in the frame
    corners, ids, rejected = detector.detectMarkers(gray)

    # Draw markers if any are detected
    if ids is not None:
        print("Detected markers:", ids)
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    else:
        print("No markers detected in this frame.")

    # Display the frame with detected markers
    cv2.imshow("Detected Markers", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()