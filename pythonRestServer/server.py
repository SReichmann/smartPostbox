#!flask/bin/python
from flask import Flask, jsonify
from datetime import datetime
import tweepy
import os
import json

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
    twitterAPI.update_with_media('test.jpg', datetime.now())
    return jsonify({'time': datetime.now()})

@app.route('/picture', methods=['POST'])
def post_picture():
    # check data

    # Twitter stuff

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    set_credentials()
    app.run(debug=True)