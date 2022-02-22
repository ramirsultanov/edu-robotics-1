import cv2

"""A function that attempts to record 10 second video from web camera 
and if successful writes the video to the 'output/' folder"""


def execute(dev):
    cap = cv2.VideoCapture(dev)

    if not cap.isOpened():
        print("Error opening camera")

    out = cv2.VideoWriter('output/output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    n = int(cap.get(cv2.CAP_PROP_FPS)) * 10
    count = 0
    while cap.isOpened() and count < n:
        count += 1
        ret, frame = cap.read()

        if ret:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()


