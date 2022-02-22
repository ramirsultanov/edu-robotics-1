import cv2
import numpy as np

mouseX, mouseY = -1, -1


class Warper:

    def __init__(self, image):
        self.img = image

    def draw_circle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            global mouseX, mouseY
            cv2.circle(self.img, (x, y), 3, (255, 0, 255), -1)
            mouseX, mouseY = x, y


"""A function that accepts image, shows window with the image, 
waits for the user to input four points 
(with double click and '1' for the first point, '2' for the second point, etc.), 
and shows warped transformation after hitting 'w', 'c', or ESC"""


def execute(img):
    warper = Warper(img)
    window = "image"
    cv2.imshow(window, warper.img)
    cv2.setMouseCallback(window, warper.draw_circle)
    p1, p2, p3, p4 = (-1, -1), (-1, -1), (-1, -1), (-1, -1)
    while True:
        cv2.imshow(window, warper.img)
        key = cv2.waitKey(20) & 0xFF
        if key == ord('1'):
            p1 = mouseX, mouseY
        elif key == ord('2'):
            p2 = mouseX, mouseY
        elif key == ord('3'):
            p3 = mouseX, mouseY
        elif key == ord('4'):
            p4 = mouseX, mouseY
        elif key == ord('w') or key == ord('c') or key == 27:  # ASCII ESCape
            break
    width, height = warper.img.shape[0], warper.img.shape[1]
    pts1 = np.float32([[p1], [p2], [p3], [p4]])
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(warper.img, matrix, (width, height))
    cv2.imshow("output", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
