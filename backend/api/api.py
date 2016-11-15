from flask import *
import os
import requests
import re
import hashlib

api = Blueprint('api', __name__, template_folder='templates')

@api.route('/')
def renderIndex():
    if request.method == "GET":
        print("HERE")
        return render_template("index.html")

def grabData(rawartist, artists):
    apikey = "a658bb1ac88d31aaacb4038f7589f694"
    artists[rawartist] = {}
    artists[rawartist]['genres'] = []
    artists[rawartist]['similar'] = []
    params = {
        "method": "artist.getinfo",
        "artist": rawartist,
        "autocorrect": 1,
        "api_key": apikey,
    }
    params['format']= 'json'
    # url = Request(str(query))
    r = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
    for genre in (r.json()['artist']['tags']['tag']):
        artists[rawartist]['genres'].append((str(genre['name'].encode('utf-8'))))

    for similar_artist in r.json()['artist']['similar']['artist']:
        artists[rawartist]['similar'].append((str(similar_artist['name'].encode('utf-8'))))

    artists[rawartist]['listeners'] = r.json()['artist']['stats']['listeners']
    artists[rawartist]['playcount'] = r.json()['artist']['stats']['playcount']
    return artists

@api.route('/api/v1/artist', methods=['POST', 'GET', 'PUT'])
def artistApi():
    artists = {}
    if request.method == "POST":
        myvals = request.get_json()
        rawartist = (str(myvals['artist']))
        counter = 0
        similarcounter = 0
        mastercounter = 0
        open('genre_data.txt', 'w').close()
        while True:
            artists = grabData(rawartist, artists)
            print(artists)
            for similar in artists[rawartist]['similar']:
                artists = grabData(similar, artists)
            if (counter == len(artists[rawartist]['similar'])):
                counter = 0
                rawartist = artists[artists[rawartist]['similar'][similarcounter]]['similar'][counter]
                similarcounter += 1
                continue
            with open('genre_data.txt', 'a') as file:
                genre_data = '$'.join(artists[rawartist]['genres'])
                file.write(str(mastercounter) + ", " + artists[rawartist]['playcount'] + " " + artists[rawartist]['listeners'] + " " + "$" + str(genre_data) + "$;" + '\n')
            mastercounter += 1
            rawartist = artists[rawartist]['similar'][counter]
            counter += 1

        return 200
	return 404
