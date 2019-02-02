#!flask/bin/python
from flask import Flask, jsonify, request
from datetime import datetime
import tweepy
import os
import json
import base64
import time

app = Flask(__name__)
twitterAPI = None

def set_credentials():
    with open('credentials.json') as json_file:
        data = json.load(json_file)
        api_key = data['api_key']
        api_secret = data['api_secret']
        oauth_access_token = data['oauth_access_token']
        oauth_access_token_secret = data['oauth_access_token_secret']

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(oauth_access_token, oauth_access_token_secret)
        global twitterAPI 
        twitterAPI = tweepy.API(auth)


@app.route('/time', methods=['GET'])
def get_time():
    return jsonify({'time': datetime.now()})

@app.route('/picture', methods=['POST'])
def post_picture():
    # Check data TODO

    # Decode to make it usable again
    dictionary = json.loads(request.data)
    pictureData = base64.b64decode(dictionary['pictureData'])

    # Write to a file
    filename = str(time.strftime("%Y:%m:%d_%H:%M:%S"))

    with open("pictures/" + filename + ".jpg", "w") as picture_file:
            newFileByteArray = bytearray(pictureData)
            picture_file.write(newFileByteArray)

    # Finally twitter the received picture
    twitterAPI.update_with_media('pictures/' + filename + '.jpg', filename)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    set_credentials()
    app.run(debug=True)