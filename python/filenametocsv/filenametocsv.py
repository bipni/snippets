import os
import glob
import csv

x = glob.glob(r"/home/bipni/Documents/EX/*.*")
with open('addfaces.csv', 'w', newline='') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ["filename", "name", "roll", "mobile", "class", "section", "gender"])
    writer.writeheader()
    for path in x:
        filename = path.split('/')
        # print(filename[len(filename)-1])
        flnm = filename[len(filename)-1].split(',')
        name = flnm[0]
        roll = flnm[1]
        mbl = flnm[2]
        clss = flnm[3]
        sec = flnm[4]
        gen = flnm[5].strip('.jpg')

        writer.writerows([{
                "filename": filename[len(filename)-1],
                "name": name,
                "roll": roll,
                "mobile": mbl,
                "class": clss,
                "section": sec,
                "gender": gen
                }]
            )
