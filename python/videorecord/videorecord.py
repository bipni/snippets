import cv2
import time
import os

homedir = os.path.expanduser("~")    
rtsp = "rtsp://admin:admin123@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"
size = (1280, 720)

def record_video():
    if not os.path.isdir(f'{homedir}/Videos'):
        os.mkdir(f'{homedir}/Videos')

    while True:
        hour, day = get_time()
        path = f'{homedir}/Videos/{time.ctime(time.time())}'
        print(hour)
        if not day == 'Fri':
            if hour >= 10 and hour < 12:
                path = f'{homedir}/Videos/{time.ctime(time.time())}.avi'
                cap = cv2.VideoCapture(rtsp)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(path,fourcc, 30.0, size)
                print('Start Recording')
                while True:
                    read, image = cap.read()
                    image = cv2.resize(image, size)
                    out.write(image)

                    hour, day = get_time()
                    print(f'inside {hour}')
                    if hour == 12:
                        cap.release()
                        out.release()
                        print('Stop Recording')
                        break

def get_time():
    local_time = time.ctime(time.time())
    lt = local_time.split(' ')
    if len(lt) == 5:
        hour = lt[3].split(':')
    if len(lt) == 6:
        hour = lt[4].split(':')
    return int(hour[0]), lt[0]

if __name__ == '__main__':
    record_video()