from resources.SpotifyConection import getUsername,newConection
from models.Playlist import *
from models.Track import * 
from models.Artist import *

# Create a empty playlist with a name

def createPlaylist(name_playlist):

    try:
        newConection().user_playlist_create(getUsername(), name_playlist, public=True)
    except:
        print('INFO: ERROR TO CREATE A PLAYLIST')

# Get playlist by id

def getPlaylist(id_playlist):

    request = newConection().user_playlist(getUsername(), playlist_id=id_playlist, fields=None)
    playlist = Playlist()
    playlist.setPlaylistByJson(request)

    return playlist

# Get saved playlist at the spotify account

def getMinePlaylists():

    playlists = []

    request = newConection().current_user_playlists(limit=50, offset=0)

    for item in request['items']:
        playlist = Playlist()
        playlist.setPlaylistByJson(item)
        playlists.append(playlist)

    return playlists

# Transfer songs of playlist source to playlist target

def transferSongsPlaylist(id_playlist_source,id_playlist_target):

    playlist = newConection().user_playlist(getUsername(), playlist_id=id_playlist_source, fields=None)
    songs = playlist["tracks"]["items"]

    id_song_list = []
    for song in songs:
        id_song_list.append(song["track"]["id"])

    newConection().user_playlist_add_tracks(getUsername(), id_playlist_target, id_song_list, position=None)

# Copy a playlist and save it in your account

def copyPlaylist(id_playlist_source):

    playlist_source = newConection().user_playlist(getUsername(), playlist_id=id_playlist_source, fields=None)
    name_playlist_source = playlist_source['name']

    name_copied_playlist = name_playlist_source + ' (CP)'
    createPlaylist(name_copied_playlist)

    request = newConection().current_user_playlists(limit=50, offset=0)
    user_playlists = request['items']

    id_copied_playlist = ''

    for index_playlist in user_playlists:
        if(name_copied_playlist == index_playlist['name']):
            id_copied_playlist = index_playlist['id']
            break

    transferSongsPlaylist(id_playlist_source, id_copied_playlist)
