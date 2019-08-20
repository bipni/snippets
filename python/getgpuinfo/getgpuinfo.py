import os
import re


def gpu():
    card = []
    formatCard = []
    device = []
    value = []

    os.chdir('/')
    os.chdir('dev')
    os.chdir('dri')

    listOfDriver = os.popen('ls -l').read()
    driver = listOfDriver.split('\n')

    for i in driver:
        card.append(i)

    for j in card:
        formatCard.append(re.sub(' +', ' ', j))

    for k in range(len(formatCard)):
        device.append(formatCard[k].split(' '))

    for p in range(len(device)):
        if device[p][len(device[p]) - 1][:len(device[p][len(device[p]) - 1])-1] == 'card':
            if (device[p][len(device[p]) - 1][0]) == 'c':
                c = 'char'
            else:
                c = 'block'

            s = 'readlink ' + '/sys/dev/' + c + '/' + device[p][4][:len(device[p][4]) - 1] + '\\' + ':' + device[p][5] + '/device/driver'
            addr = '/dev/dri/' + device[p][len(device[p]) - 1]

            gAddr = os.popen(s).read()
            gpuType = gAddr.split('/')

            if gpuType[len(gpuType)-1] == 'amdgpu\n':
                gpuName = 'AMD'
                flag = True
            elif gpuType[len(gpuType)-1][0:1] == 'i':
                gpuName = 'Intel'
                flag = True
            else:
                gpuName = 'NVDIA'
                flag = False
            value.append([addr, gpuName, flag])

    return value


if __name__ == '__main__':
    ls = gpu()
    print(ls)
