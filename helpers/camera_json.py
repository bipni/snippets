import sys
import json


json_file = open('cameras.json')
cameras = json.load(json_file)

cams = sys.argv
true = False

for cam in cams:
    if true:
        if cam == 'all':
            print(json.dumps(cameras, indent=4))
            break
        
        print(json.dumps(cameras.get(cam), indent=4))
    
    true = True