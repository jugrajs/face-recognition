# face-recognition

Welcome to the Real-Time Face Recognition project! This project uses the `face_recognition` library along with OpenCV to perform real-time face recognition on a live camera feed. It includes two main files: `faceEncoder.py` for encoding and managing face encodings, and `live_face_recognition.py` for performing live face recognition using the encoded faces.

## Features

- **Face Encoder**: The `faceEncoder.py` script provides functions for encoding faces from images, saving and loading encodings to/from files, and encoding multiple faces from a set of images.

- **Live Face Recognition**: The `live_face_recognition.py` script captures live frames from a camera, identifies faces using the saved encodings, and marks recognized faces with bounding boxes.

## Getting Started

1. **Clone this repository to your local machine:**

```
git clone https://github.com/yourusername/real-time-face-recognition.git
```
2. Navigate to the project directory:
```
cd real-time-face-recognition
```
3. Install the required dependencies using the requirements.txt file:
```
pip install -r requirements.txt
```
4. Add your face images to the yourfaces folder:
    - Add your face images to the yourfaces folder.
    - Name the images with numbers as prefixes (e.g., 1.png, 2.png).
5. Run the faceEncoder.py script to encode and save face encodings:
```
python faceEncoder.py
```
6. This script will use images from the yourfaces folder to generate face encodings and save them in myencodings.dat.
7. Run the live_face_recognition.py script for real-time face recognition:
```
python live_face_recognition.py
```
8. This script captures frames from the default camera, compares the captured faces with the saved encodings, and displays the live video feed with recognized faces.
9. Press the 'q' key to quit the live face recognition application.
## Dependencies

- Python
- NumPy
- OpenCV
- face-recognition

## Files

- **faceEncoder.py:** Encodes and manages face encodings using the face_recognition library.
- **live_face_recognition.py:** Performs real-time face recognition using the saved face encodings.

## Notes

You can adjust the tolerance parameter in live_face_recognition.py to fine-tune face recognition sensitivity.
Make sure to replace yourusername with your actual GitHub username in repository URLs.
If you encounter any issues, refer to the documentation of the used libraries.
