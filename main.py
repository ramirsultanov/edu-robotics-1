import cv2

import task_1_1
import task_1_2
import task_1_3

if __name__ == '__main__':
    img = cv2.imread("resources/Lenna.png")
    img = cv2.resize(img, (500, 500))
    dev = 0
    task_1_1.execute(img)
    task_1_2.execute(img)
    task_1_3.execute(dev)
