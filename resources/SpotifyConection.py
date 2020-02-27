import sys
import spotipy
import spotipy.oauth2
import spotipy.util as util
from resources.RepositoryController import getOauthParameters

parameters = getOauthParameters()

USERNAME_ID = parameters['username_id']
SCOPES = parameters['scopes']
CLIENT_ID = parameters['client_id']
CLIENT_SECRET = parameters['client_secret']
REDIRECT_URI = parameters['redirect_uri']


def getUsername(): return USERNAME_ID

def newConection():

    token = util.prompt_for_user_token(getUsername(), SCOPES, client_id= CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri= REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print("INFORMATION:Can't get token for", getUsername())

    return sp
