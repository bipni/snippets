import socket
import multiprocessing
import time
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


def main():
    port = 554
    myIp = getMyIp().split('.')
    network = myIp[0] + '.' + myIp[1] + '.' + myIp[2] + '.'

    cameraIp = getCameraIp(network, port)

    print("\n\n" + str(len(cameraIp)) + " Camera Found\n")
    print("Available Camera IP: ", end='\n')
    for i, j in enumerate(cameraIp):
        print(f'Camera {i+1}: {j}')

    print("\n")


if __name__ == '__main__':
    main()
