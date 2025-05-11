# Image Acquisition in Image Processing

## **What is Image Acquisition?**
The process of capturing visual data (images/videos) from physical sources (cameras, scanners, sensors) and converting them into **digital form** for processing.

---

## **Key Components**
1. **Sensors**: Capture light/intensity (e.g., CCD/CMOS in cameras).  
2. **Lens**: Focuses light onto the sensor.  
3. **Analog-to-Digital Converter (ADC)**: Converts analog signals to digital pixels.  

![Image Acquisition System](https://raw.githubusercontent.com/opencv/opencv/master/doc/imaging/sensor_model.png)  
*(Simplified diagram of an image acquisition pipeline)*

---

## **Types of Image Acquisition**

### 1. **Cameras**
- **Digital Cameras**: Capture RGB images (e.g., DSLRs, smartphones).  
- **Thermal Cameras**: Detect infrared radiation.  
- **Microscopes**: High-resolution imaging.  

![Camera Types](https://raw.githubusercontent.com/wiki/opencv/opencv/images/camera_types.png)  
*(Common camera types)*

### 2. **Scanners**
- Flatbed scanners (documents, photos).  
- 3D scanners (for depth maps).  

### 3. **Satellite/Sensors**
- Remote sensing (e.g., Landsat).  

---

## **Image Representation**
| Type        | Example | Description |
|-------------|---------|-------------|
| **Grayscale** | ![Grayscale](https://raw.githubusercontent.com/wiki/opencv/opencv/images/lena_gray.png) | Single channel (0=black, 255=white). |
| **Color (RGB)** | ![Color](https://raw.githubusercontent.com/wiki/opencv/opencv/images/lena_color.png) | 3 channels (Red, Green, Blue). |
| **Binary** | ![Binary](https://raw.githubusercontent.com/wiki/opencv/opencv/images/lena_threshold.png) | Pixels as 0 or 1 (after thresholding). |

---

## **Factors Affecting Quality**
1. **Resolution**: Higher = more detail (e.g., 4K vs. 720p).  
2. **Lighting**: Poor light → noise.  
3. **Sensor Sensitivity**: ISO settings.  

![Noise Example](https://raw.githubusercontent.com/wiki/opencv/opencv/images/image_noise.png)  
*(Gaussian noise in a low-light image)*

---

## **Example Code (Python/OpenCV)**
```python
import cv2

# Capture from webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cv2.imwrite("captured_image.jpg", frame)
cap.release()