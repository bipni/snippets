import socket
import multiprocessing
import os
import subprocess

def pinger(job_q, results_q):

    DEVNULL = open(os.devnull, 'w')

    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip], stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

def getMyIp():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    hostIp = "8.8.8.8"
    port = 80

    s.connect((hostIp, port))

    ip = s.getsockname()[0]

    s.close()

    return ip

def scanner(ip):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(ip, 554)
        # s.close()
        return ip, True
    except:
        # s.close()
        return ip, False

def main():

    ipList = []

    myIp = getMyIp().split('.')
    
    baseIp = myIp[0] + '.' + myIp[1] + '.' + myIp[2] + '.'

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(255)]

    for p in pool:
        p.start()
    
    for i in range(1, 255):
        jobs.put(baseIp + '{0}'.format(i))
    
    for p in pool:
        jobs.put(None)
    
    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        ipList.append(ip)
    
    print("All available ip in this network:\n")
    for i in ipList:
        print(i)
    


if __name__ == '__main__':
    print("\nPlease Wait...\n")
    main()