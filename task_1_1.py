import cv2

"""A function that accepts image, divides it into 9 tiles, and writes each tile to the 'output/' folder"""


def execute(img):
    n = 3
    for i in range(n):
        for j in range(n):
            cv2.imwrite("output/cropped_image_" + str(i) + str(j) + ".png",
                        img[(img.shape[0] // n * i):(img.shape[0] // n * (i + 1)),
                        (img.shape[1] // n * j):(img.shape[1] // n * (j + 1))])
