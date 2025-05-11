# Image Acquisition in Image Processing

## **What is Image Acquisition?**
The process of capturing visual data (images/videos) from physical sources (cameras, scanners, sensors) and converting them into **digital form** for processing.

---

## **Key Components**
1. **Sensors**: Capture light/intensity (e.g., CCD/CMOS in cameras).  
2. **Lens**: Focuses light onto the sensor.  
3. **Analog-to-Digital Converter (ADC)**: Converts analog signals to digital pixels.  

![Image Acquisition System](https://www.researchgate.net/publication/334632187/figure/fig1/AS:781359735603200@1563720266584/Block-diagram-of-image-acquisition-system.png)  
*(Block diagram of an image acquisition system)*

---

## **Types of Image Acquisition**

### 1. **Cameras**
- **Digital Cameras**: Capture RGB images (e.g., DSLRs, smartphones).  
- **Thermal Cameras**: Detect infrared radiation.  
- **Microscopes**: High-resolution imaging for tiny objects.  

![Camera Types](https://www.researchgate.net/publication/339354072/figure/fig1/AS:860708058959872@1582167244770/Types-of-digital-cameras-used-in-image-acquisition.png)  
*(Common camera types for acquisition)*

### 2. **Scanners**
- Flatbed scanners (documents, photos).  
- 3D scanners (for depth maps).  

### 3. **Satellite/Sensors**
- Remote sensing (e.g., Landsat, Hubble Telescope).  

---

## **Image Representation**
- **Grayscale**: Single channel (0=black, 255=white).  
- **Color**: 3 channels (RGB/HSV).  
- **Binary**: Pixels as 0 or 1 (thresholded).  

| Grayscale | Color (RGB) | Binary |
|-----------|------------|--------|
| ![Grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Lenna_gray.png/120px-Lenna_gray.png) | ![Color](https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Lenna_%28test_image%29.png/120px-Lenna_%28test_image%29.png) | ![Binary](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Lenna_thresholded.png/120px-Lenna_thresholded.png) |

---

## **Factors Affecting Quality**
1. **Resolution**: Higher = more detail (e.g., 4K vs. 720p).  
2. **Lighting**: Poor light → noise.  
3. **Sensor Sensitivity**: ISO settings (trade-off: noise vs. brightness).  

![Noise Example](https://www.researchgate.net/publication/336324681/figure/fig2/AS:812472659316736@1570717980754/Image-with-added-Gaussian-noise.png)  
*(Image corrupted by Gaussian noise)*

---

## **Example Code (Python/OpenCV)**
```python
import cv2

# Initialize camera (0=default webcam)
cap = cv2.VideoCapture(0)

# Capture frame-by-frame
ret, frame = cap.read()
if ret:
    cv2.imwrite("captured_image.jpg", frame)

# Release camera
cap.release()
```

---

## **Applications**
- 📸 **Photography**: HDR imaging.  
- 🏭 **Industrial Inspection**: Defect detection.  
- 🚀 **Astronomy**: Capturing celestial bodies.  

---
**Note**: Replace `0` in `VideoCapture(0)` with a video file path for offline processing.