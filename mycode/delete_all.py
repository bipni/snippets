import pymongo
import glob
import shutil
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["alavya"]
anpr_appearances = mydb["anpr_appearances"]
attendance_appearences = mydb["attendance_appearences"]
attendance_faces = mydb["attendance_faces"]
school_face_details = mydb["school_face_details"]


anpr = anpr_appearances.delete_many({})
print(anpr.deleted_count, "documents deleted in anpr_appearance.")

atap = attendance_appearences.delete_many({})
print(atap.deleted_count, "documents deleted in attendance_appearences.")

atfc = attendance_faces.delete_many({})
print(atfc.deleted_count, "documents deleted in attendance_faces.")

scfc = school_face_details.delete_many({})
print(scfc.deleted_count, "documents deleted in school_face_details.")

f = 0
faces = glob.glob('/home/bipni/Documents/alavyav2/attendance/public/images/faces/*')
for face in faces:
    f += 1
    os.remove(face)
print(f'{f} faces deleted')

p = 0
plates = glob.glob('/home/bipni/Documents/alavyav2/attendance/public/images/plates/*')
for plate in plates:
    if not plate == '/home/bipni/Documents/alavyav2/attendance/public/images/plates/not_available.png':
        p += 1
        os.remove(plate)
print(f'{p} plates deleted')

v = 0
videos = glob.glob('/home/bipni/Videos/cam01/*')
for video in videos:
    v += 1
    os.remove(video)
print(f'{v} anpr videos deleted in cam01')

w = 0
wideos = glob.glob('/home/bipni/Videos/cam02/*')
for wideo in wideos:
    w += 1
    os.remove(wideo)
print(f'{w} anpr videos deleted in cam02')

i = 0
images = glob.glob('/home/bipni/Videos/images/*')
for image in images:
    i += 1
    os.remove(image)
print(f'{i} anpr images deleted')
