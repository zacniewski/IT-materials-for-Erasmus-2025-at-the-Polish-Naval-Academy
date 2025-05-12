### What is Python?

Python is a high-level, interpreted programming language known for its:  
  - Readability and clean syntax
  - Cross-platform compatibility
  - Extensive standard library
  - Large ecosystem of third-party packages
  -  Strong community support

Python is widely used for:  
  - Web development
  - Data science and machine learning
  - Scientific computing
  - Automation and scripting
  - Game development
  - And of course, graphics and image processing

### Python Graphics and Image Libraries - basic examples
1. [Pillow](https://pillow.readthedocs.io/en/stable/handbook/overview.html) (PIL)

Purpose: Basic image processing
```python

from PIL import Image, ImageDraw

# Open an image
img = Image.open("example.jpg")

# Resize
img = img.resize((400, 300))

# Draw on image
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Hello World", fill=(255, 0, 0))

# Save
img.save("output.jpg")
```
2. [Matplotlib](https://matplotlib.org/stable/users/index.html)

Purpose: Data visualization and basic image display
```python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Display an image
img = mpimg.imread('example.jpg')
plt.imshow(img)
plt.show()

# Create plots
plt.plot([1, 2, 3, 4])
plt.ylabel('Some numbers')
plt.show()
```

3. [OpenCV](https://learnopencv.com/getting-started-with-opencv/) (cv2)

Purpose: Advanced image processing and computer vision
```python

import cv2

# Read image
img = cv2.imread('example.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 100, 200)

# Display
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

4. [PyGame](https://www.pygame.org/docs/)

Purpose: Game development and interactive graphics
```python

import pygame

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw a circle
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)
    pygame.display.flip()

pygame.quit()
```

5. [Turtle Graphics](https://www.datacamp.com/tutorial/turtle-graphics)

Purpose: Educational graphics programming
```python

import turtle

# Create turtle
t = turtle.Turtle()

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```


6. [Plotly](https://plotly.com/python/)

Purpose: Interactive web-based visualizations
```python

import plotly.express as px

# Create interactive plot
fig = px.scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13])
fig.show()
```
Getting Started

To begin working with graphics in Python:  
    Install Python from python.org  
    Install libraries using pip: `pip install pillow matplotlib opencv-python pygame plotly`  
    Start with simple projects and gradually explore more complex functionality  

Python's graphics capabilities make it excellent for everything from simple image manipulation to complex computer vision applications and interactive visualizations.  
