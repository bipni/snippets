import sys
import json

with open('cameras.json') as json_file:
    cameras = json.load(json_file)

cams = sys.argv

for cam in cams:
    print(json.dumps(cameras.get(cam), indent=4))