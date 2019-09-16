import socket
import multiprocessing
import time
import cv2
import threading

link = []


def getMyIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    hostIp = "8.8.8.8"
    port = 80

    s.connect((hostIp, port))

    myIp = s.getsockname()[0]

    s.close()

    return myIp


def getCameraIp(network, port, timeout=3.0):
    print("\nPlease wait...\n")

    q = multiprocessing.Queue()
    processes = []

    for i in range(1, 255):
        ip = network + str(i)
        p = multiprocessing.Process(target=checkServer, args=[ip, port, q])
        processes.append(p)
        p.start()

    time.sleep(timeout)

    cameraIp = []

    for x, p in enumerate(processes):
        if p.exitcode is None:
            p.terminate()
        else:
            open_ip, address, port = q.get()
            if open_ip:
                cameraIp.append(address)

    for x, p in enumerate(processes):
        p.join()

    return cameraIp


def checkServer(address, port, queue):
    s = socket.socket()
    try:
        s.connect((address, port))
        queue.put((True, address, port))
    except socket.error:
        queue.put((False, address, port))


def getRtspLink(cameraIp, username="", password=""):
    threads = []
    rtspTemplate = [
        #255 IP Came
        "rtsp://[username]:[password]@[ip]:554/11",
        "rtsp://[username]:[password]@[ip]/1",
        
        #2n Helios
        "rtsp://[username]:[password]@[ip]/h264_stream",

        


        "rtsp://[username]:[password]@[ip]/rtsph264480p",
        "rtsp://[username]:[password]@[ip]/rtsph2641080p",
        "rtsp://[username]:[password]@[ip]/rtsph2641024p",
        "rtsp://[username]:[password]@[ip]/rtsph264720p",
        "rtsp://[username]:[password]@[ip]/cam/realmonitor",
        "rtsp://[username]:[password]@[ip]/live",
        "rtsp://[username]:[password]@[ip]:85/",
        "rtsp://[username]:[password]@[ip]/cam/realmonitor?channel=0&subtype=1",
        "rtsp://[username]:[password]@[ip]/media/video1",
        "rtsp://[username]:[password]@[ip]/media/video2",
        "rtsp://[username]:[password]@[ip]/av0_0",
        "rtsp://[username]:[password]@[ip]/video1",
        "rtsp://[username]:[password]@[ip]/11",
        "rtsp://[username]:[password]@[ip]/Streaming/Channels/1",
        "rtsp://[username]:[password]@[ip]/axis-media/media.amp?videocodec=h264&resolution=640x480",
        "rtsp://[username]:[password]@[ip]/onvif-media/media.amp",
        "rtsp://[username]:[password]@[ip]/axis-media/media.amp",
        "rtsp://[username]:[password]@[ip]/ucast/12",
        "rtsp://[username]:[password]@[ip]/cam/realmonitor",
        "rtsp://[ip]:554/user=[username]_[password]=_channel=0_stream=0.sdp",
        "rtsp://[username]:[password]@[ip]/primarystream",
        "rtsp://[username]:[password]@[ip]/ufirststream",
        "rtsp://[username]:[password]@[ip]/stream1",
        "rtsp://[username]:[password]@[ip]/stream2",
        "rtsp://[username]:[password]@[ip]/stream3",
        "rtsp://[username]:[password]@[ip]/live1.sdp",
        "rtsp://[username]:[password]@[ip]/ch0_0.h264",
        "rtsp://[username]:[password]@[ip]/Video?Codec=MPEG4&Width=1280&Height=720&Fps=15",
        "rtsp://[username]:[password]@[ip]/live2.sdp",
        "rtsp://[username]:[password]@[ip]/Video?Codec=MPEG4&Width=1280&Height=720&Fps=15",
        "rtsp://[username]:[password]@[ip]/Video",
        "rtsp://[ip]:554/onvif/videoStreamId=1"
    ]

    for i, j in enumerate(cameraIp):
        for y, x in enumerate(rtspTemplate):
            p = x.replace("[username]", username[i], 1)
            q = p.replace("[password]", password[i], 1)
            r = q.replace("[ip]", j, 1)

            t = threading.Thread(target=isLinkValid, args=[r, ])
            t.start()
            threads.append(t)

        for pr in threads:
            pr.join()


def isLinkValid(r):
    global link
    cap = cv2.VideoCapture(r)

    if cap.isOpened():
        link.append(r)


def main():
    username = []
    password = []
    port = 554
    myIp = getMyIp().split('.')
    network = myIp[0] + '.' + myIp[1] + '.' + myIp[2] + '.'

    cameraIp = getCameraIp(network, port)

    for i in cameraIp:
        print("IP: " + i)
        un = input("Enter Username: ")
        pw = input("Enter Password: ")
        username.append(un)
        password.append(pw)

    getRtspLink(cameraIp, username, password)

    print("\n\n\n\n\n" + str(len(cameraIp)) + " Camera Found\n")
    print("Available RTSP Link: ", end='\n')
    for i in link:
        print(i)

    print("\n")


if __name__ == '__main__':
    main()
