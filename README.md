# IT materials for Erasmus 2025 at the Polish Naval Academy

# Information 
This website contains materials useful for the subjects:  
>  - "Computer programming" (22 meetings, 20 hours of lectures and 40 hours of exercises/laboratories),  
>  - "Computer graphics" (10 meetings, 15 hours of lectures and 30 hours of exercises/laboratories).

# Table of contents  

## 1. Computer programming
  1. [Programming as a way of thinking](https://allendowney.github.io/ThinkPython/chap01.html),  
  2. [Variables and Statements](https://allendowney.github.io/ThinkPython/chap02.html),  
  3. [Functions](https://allendowney.github.io/ThinkPython/chap03.html),  
  4. [Functions and Interfaces](https://allendowney.github.io/ThinkPython/chap04.html),  
  5. [Conditionals and Recursion](https://allendowney.github.io/ThinkPython/chap05.html),  
  6. [Return Values](https://allendowney.github.io/ThinkPython/chap06.html),  
  7. [Iteration and Search](https://allendowney.github.io/ThinkPython/chap07.html),  
  8. [Strings and Regular Expressions](https://allendowney.github.io/ThinkPython/chap08.html),  
  9. [Lists](https://allendowney.github.io/ThinkPython/chap09.html),  
  10. [Dictionaries](https://allendowney.github.io/ThinkPython/chap10.html),  
  11. [Tuples](https://allendowney.github.io/ThinkPython/chap11.html),  
  12. [Text Analysis and Generation](https://allendowney.github.io/ThinkPython/chap12.html),  
  13. [Files and Databases](https://allendowney.github.io/ThinkPython/chap13.html),  
  14. [Classes and Functions](https://allendowney.github.io/ThinkPython/chap14.html),  
  15. [Classes and Methods](https://allendowney.github.io/ThinkPython/chap15.html),  
  16. [Classes and Objects](https://allendowney.github.io/ThinkPython/chap16.html),  
  17. [Inheritance](https://allendowney.github.io/ThinkPython/chap17.html),  
  18. [Python Extras](https://allendowney.github.io/ThinkPython/chap18.html),  
  19. [Final thoughts](https://allendowney.github.io/ThinkPython/chap19.html).  

The topics are based on the "Think Python" book, authored by Allen Downey:  
  - book on [GitHub](https://allendowney.github.io/ThinkPython/index.html) with Jupyter notebooks,  
  - other [books](https://greenteapress.com/wp/) authored by Allen Downey.  


## 2. Computer graphics

The topics are based on the syllabus to the "Computer Graphics" subject (see the attached pdf file).  

### Day 1 - "Introduction to Python and its graphics and images libraries (lecture)"  

  - book on [GitHub](https://allendowney.github.io/ThinkPython/index.html) with Jupyter notebooks,    
  - Python [resources](https://zacniewski.github.io/python-resources/) suggested by me :smiley:,    


What is Python?

Python is a high-level, interpreted programming language known for its:

    Readability and clean syntax
    Cross-platform compatibility
    Extensive standard library
    Large ecosystem of third-party packages
    Strong community support

Python is widely used for:
    Web development
    Data science and machine learning
    Scientific computing
    Automation and scripting
    Game development
    And of course, graphics and image processing

Python Graphics and Image Libraries
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


### Day 2 - "Retrieving, processing, and storing images, manipulating pixels"  
  - link ...


### Day 3 - "Transformations – rotating, cropping, scaling, flipping and translating (lecture)"  
  - link ...


### Day 4 - "Image arithmetic, masking and color spaces (lecture)"  
  - link ...


### Day 5 - "Histograms, blurring, smoothing and thresholding (lecture)"  
  - link ...

### Day 6 - "Basic image operations on images with OpenCV (lab)"  
  - link ...


### Day 7 - "Working with image arithmetic, masking and color spaces (lab)"  
  - link ...


### Day 8 - "Working with histograms, blurring, smoothing and thresholding (lab)"  
  - link ...


### Day 9 - "Working with gradients and edge detection (lab)"  
  - link ...


### Day 10 - "Working with video files (lab)"  
  - link ...

