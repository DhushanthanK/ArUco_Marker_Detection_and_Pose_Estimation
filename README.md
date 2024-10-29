# ArUco Marker Detection and Pose Estimation

This project demonstrates camera calibration, ArUco marker generation, detection, and pose estimation using OpenCV. The project consists of several Python scripts that allow you to calibrate your camera, generate ArUco markers, detect them, and estimate their pose in real-time.

Camera Calibration:

<img width="1057" alt="Camera Calibration" src="https://github.com/user-attachments/assets/087279b8-951b-4c7f-ac85-8316316b564c">

ArUco Marker Detection:

<img width="491" alt="Detection" src="https://github.com/user-attachments/assets/4b0b9431-295a-4da6-adf7-b0e972f0008d">

Pose Estimation:

<img width="476" alt="Pose Estimation" src="https://github.com/user-attachments/assets/427f6df0-5a5f-4584-b5a4-f090364db016">

## Requirements

- Python 3.x
- OpenCV (with contrib modules)
- NumPy

## Instructions for Use

1. Clone the repository

```bash
git clone https://github.com/Dhushan27/aruco_marker_detection.git
cd aruco_marker_detection
```

2. Install the required packages using pip:

```bash
pip install opencv-python opencv-contrib-python numpy
```

3. Place your camera calibration images in the `camera_calibration_images` directory.

4. **Camera Calibration**: Run `camera_calibration.py` to generate the calibration parameters. Ensure you have chessboard images in the specified directory.

```bash
python camera_calibration.py
```
  
5. **Marker Generation**: Execute `aruco_marker_generation.py` to create a set of ArUco markers and save them in `markers` folder.

```bash
python aruco_marker_generation.py
```

6. **Marker Detection**: Use `aruco_marker_detection.py` for detecting markers in static images.

```bash
python aruco_marker_detection.py
```

7. **Real-time Detection**: Run `aruco_marker_detection_realtime.py` to detect markers using your webcam in real time.

```bash
python aruco_marker_detection_camera.py
```

8. **Pose Estimation**: Finally, run `aruco_pose_estimation.py` to estimate and visualize the pose of detected markers.

```bash
python aruco_pose_estimation.py
```
