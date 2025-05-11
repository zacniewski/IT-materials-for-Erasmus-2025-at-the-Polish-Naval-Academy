# Image Acquisition in Image Processing

## **What is Image Acquisition?**
The process of capturing visual data from physical sources (cameras, scanners) and converting it into digital pixels.

---

## **Key Components**
1. **Sensors** (CCD/CMOS)  
2. **Lens**  
3. **ADC** (Analog-to-Digital Converter)  

![Acquisition Pipeline](https://github.com/opencv/opencv/raw/4.x/doc/pics/tutorial_sensor_block_diagram.png)  
*(Image credit: OpenCV documentation)*

---

## **Types of Image Acquisition**
### 1. **Cameras**
- **Digital** (RGB)  
- **Thermal** (Infrared)  
- **Microscopic**  

![Camera Types](https://github.com/opencv/opencv/raw/4.x/doc/pics/tutorial_camera_types.png)

### 2. **Scanners**
- Flatbed (documents)  
- 3D (depth sensing)  

---

## **Image Representation**
| Type        | Example | Description |
|-------------|---------|-------------|
| **Grayscale** | ![Grayscale](https://github.com/opencv/opencv/raw/4.x/samples/data/lena.jpg) | 1 channel (0-255) |
| **Color** | ![Color](https://github.com/opencv/opencv/raw/4.x/samples/data/lena.jpg) | 3 channels (BGR) |
| **Binary** | ![Binary](https://github.com/opencv/opencv/raw/4.x/doc/pics/tutorial_threshold_binary.png) | 0 or 1 pixels |

---

## **Factors Affecting Quality**
1. **Resolution**  
2. **Lighting Conditions**  
3. **Sensor Noise**  

![Noise Example](https://github.com/opencv/opencv/raw/4.x/doc/pics/tutorial_noise_example.png)

---

## **Python Code Example**
```python
import cv2
cap = cv2.VideoCapture(0)  # Camera capture
ret, frame = cap.read()
cv2.imwrite("capture.jpg", frame)
cap.release()
```