#ssh -i "data.pem" ubuntu@ec2-52-55-52-149.compute-1.amazonaws.com


import base64
import json
with open("Pics/edmonton.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    #print(str)
dict = []
with open('dummy.json', 'r') as file:
    json_data = file.read()
    dict = json.loads(json_data)
    #print(dict)
    for p in dict:
        if p['id'] == '3':
            p['image'] = str
            break

print(dict)
with open('dummy.json', 'w') as f:
    json.dump(dict, f, indent = 4)
