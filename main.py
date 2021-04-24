import requests
import base64, json
from secrets import *

#curl -H "Authorization: Basic ZjM...zE=" -d grant_type=authorization_code -d code=MQCbtKe...44KN -d redirect_uri=https%3A%2F%2Fwww.foo.com%2Fauth https://accounts.spotify.com/api/token

authUrl = "https://accounts.spotify.com/api/token"

authHeader = {}
authData = {}

#Base64 encode Client ID and Client Secret

def getAccessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    #print(base64_message)

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"

    res = requests.post(authUrl, headers = authHeader, data=authData)

    responseObject = res.json()

    #print(json.dumps(responseObject, indent=2))
    accessToken = responseObject['access_token']

    return accessToken


def getPlaylistTracks(token, playlistID):
    playlistEndPoint = f"https://api.spotify.com/v1/playlists/{playlistID}"

    getHeader = {
        "Authorization": "Bearer " + token
    }

    res = requests.get(playlistEndPoint, headers = getHeader)

    playlistObject = res.json()

    return playlistObject

#API requests
token = getAccessToken(clientID, clientSecret)
playlistID = "1Z0hFOnk5cW4wHcRSTIkTg?si=4478bd8e95334f9b" 

tracklist = getPlaylistTracks(token, playlistID)

#To print the tracklist into termina
#print(json.dumps(tracklist, indent=2))

## Printing the result to a json file

with open('tracklist.json', 'w') as f:
    json.dump(tracklist, f)


##Printing tracklist
for t in tracklist['tracks']['items']:
    print('-------------')
    for a in t['track']['artists']:
        print(a['name'])

    songname =t['track']['name']
    print(songname)