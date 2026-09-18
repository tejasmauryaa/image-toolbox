import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imgpath = "cat02.jpg"
img = np.array(Image.open(imgpath).convert("RGB"))

plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.show()

A1 = np.array([[2, 0],
               [0, 0.5]])
A2 = np.array([[0, -1],
               [1,  0]])
A3 = np.array([[1, 1],
               [0, 1]])
A4 = np.array([[-1, 0],
               [ 0, 1]])
A5 = np.array([[1, 0],
               [0, 0]])
matrix = [A1, A2, A3, A4, A5]

e1 = np.array([1, 0])
e2 = np.array([0, 1])

for i, A in enumerate(matrix, 1):
    print(f"A{i}:")
    print("T(e1) =", A @ e1)
    print("T(e2) =", A @ e2)
    print()


def transform_image(img, A, yscaleA5=False):

    height, width = img.shape[:2]
    cx = width // 2
    cy = height // 2

    if yscaleA5:
        A = np.array([[1, 0],
                      [0, 0.02]])

    new_img = np.zeros_like(img)
    for y in range(height):
        for x in range(width):

            X = x - cx
            Y = y - cy
            new_X = A[0, 0] * X + A[0, 1] * Y
            new_Y = A[1, 0] * X + A[1, 1] * Y
            new_x = int(new_X + cx)
            new_y = int(new_Y + cy)

            if (0 <= new_x < width) and (0 <= new_y < height):
                new_img[new_y, new_x] = img[y, x]

    return new_img




img_A1 = transform_image(img, A1)
img_A2 = transform_image(img, A2)
img_A3 = transform_image(img, A3)
img_A4 = transform_image(img, A4)
img_A5 = transform_image(img, A5, yscaleA5=True)

plt.figure(figsize=(15, 8))

plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(img_A1)
plt.title("A1 - Scaling")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(img_A2)
plt.title("A2 - Rotation")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(img_A3)
plt.title("A3 - Shear")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(img_A4)
plt.title("A4 - Reflection")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(img_A5)
plt.title("A5 - Projection")
plt.axis("off")

plt.show()