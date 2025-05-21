import cv2
print(cv2.__version__)

image = cv2.imread('jordan.png')
cv2.imshow('Michael Jordan', image)
cv2.waitKey(0)

flipped = cv2.flip(image, 1)
cv2.imshow('Flipped Michael 1', flipped)
cv2.waitKey(0)

flipped2 = cv2.flip(image, 0)
cv2.imshow('Flipped Michael 2', flipped2)
cv2.waitKey(0)

flipped3 = cv2.flip(image, -1)
cv2.imshow('Flipped Michael 3', flipped3)
cv2.waitKey(0)
cv2.imwrite('flipped.png', flipped3)

