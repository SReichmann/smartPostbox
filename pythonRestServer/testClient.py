import requests
import base64
import json

url = 'http://127.0.0.1:5000/picture'


with open("pictures/test.jpg", "rb") as image_file:
    encoded_picture = base64.b64encode(image_file.read())

data = {}
data['pictureData'] = encoded_picture
data['size'] = len(encoded_picture)
json_data = json.dumps(data)



response = requests.post(url, data=json_data)
print response.status_code