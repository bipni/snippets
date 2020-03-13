import pymongo
import glob
import shutil
import os

faces_path = '/home/bipni/Documents/alavyav2/engine/public/images/faces'
plates_path = '/home/bipni/Documents/alavyav2/engine/public/images/plates'
cam1_videos_path = '/home/bipni/Videos/cam01'
cam2_videos_path = '/home/bipni/Videos/cam02'
cam3_videos_path = '/home/bipni/Videos/cam03'
cam4_videos_path = '/home/bipni/Videos/cam04'
images_path = '/home/bipni/Videos/images'

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
faces = glob.glob(faces_path + '/*')
for face in faces:
    f += 1
    os.remove(face)
print(f'{f} faces deleted')

p = 0
plates = glob.glob(plates_path + '/*')
for plate in plates:
    if not plate == f'{plates_path}/not_available.png':
        p += 1
        os.remove(plate)
print(f'{p} plates deleted')

v = 0
videos = glob.glob(cam1_videos_path + '/*')
for video in videos:
    v += 1
    os.remove(video)
print(f'{v} anpr videos deleted in cam01')

w = 0
wideos = glob.glob(cam2_videos_path + '/*')
for wideo in wideos:
    w += 1
    os.remove(wideo)
print(f'{w} anpr videos deleted in cam02')

x = 0
xideos = glob.glob(cam3_videos_path + '/*')
for xideo in xideos:
    x += 1
    os.remove(xideo)
print(f'{x} anpr videos deleted in cam03')

y = 0
yideos = glob.glob(cam4_videos_path + '/*')
for yideo in yideos:
    y += 1
    os.remove(yideo)
print(f'{y} anpr videos deleted in cam04')

i = 0
images = glob.glob(images_path + '/*')
for image in images:
    i += 1
    os.remove(image)
print(f'{i} anpr images deleted')
