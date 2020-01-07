rtsp = "rtsp://admin:admin123@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"

# cap = cv2.VideoCapture(rtsp)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
# i = 0
# ret, fram  = cap.read()
# while(ret):
#     i = i + 1
#     ret, frame = cap.read()
#     print(frame)
#     out.write(frame)
#     if i == 1000:
#         break
# # Release everything if job is finished
# cap.release()
import cv2
import numpy as np
import random
def run_on_video(input_dir, output_dir=None, frac_to_keep=1, size=(1280, 720)):
    cap = cv2.VideoCapture(input_dir)
    count = 0
    if output_dir is not None:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_dir,fourcc, 27.0, size)
    while True:
        read, image = cap.read()
        image = cv2.resize(image, size)
        count += 1
        print(count)
        if random.random() < frac_to_keep and read:
            if output_dir is not None:
                print(count)
                out.write(image)
            else:
                cv2.imshow("window", image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        if not read or count == 500:
            print("releasing cap")
            if output_dir is not None: out.release()
            cap.release()
            break

run_on_video(rtsp, './recorded.mp4')