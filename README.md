# 🎨 Real-Time Color Detection using OpenCV

This Python project uses OpenCV to detect a specific color in real-time from a webcam feed. It highlights the detected region by drawing a bounding box around it. The detection is done using the HSV (Hue, Saturation, Value) color space.

---

## 🚀 Features

- Real-time video capture using webcam  
- Dynamic HSV threshold generation for any BGR color  
- Bounding box drawn on detected colored object  
- Easy to change the target color

---

## 📂 Project Structure

.
├── main.py          # Runs the webcam and performs color detection  
├── util.py          # Contains the get_limits() function

---

## 📦 Requirements

Install Python packages:  
`pip install opencv-python pillow numpy`

---

## ▶️ How to Run

Make sure you have a webcam connected.  
Run the project using:  
`python main.py`  
Press `q` to quit the webcam stream.

---

## 🎯 Customize the Target Color

In `main.py`, modify the `color` variable (in BGR format):  
`color = [0, 255, 255]  # Yellow`

You can replace this with any BGR color:  
- Red: `[0, 0, 255]`  
- Green: `[0, 255, 0]`  
- Blue: `[255, 0, 0]`

---

## 🙌 Acknowledgments

- [OpenCV](https://opencv.org/) for real-time computer vision tools  
- [Pillow](https://python-pillow.org/) for simple image operations  
- This project is inspired by color-based object tracking systems
