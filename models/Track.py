from models.Artist import *

class Track():

	def __init__(self):
		self.__id = ''
		self.__name = ''
		self.__artist = ''
		self.__album = ''

	def getId(self):
		return self.__id

	def getName(self):
		return self.__name

	def getArtist(self):
		return self.__artist

	def getAlbum(self):
		return self.__album

	def setTrackByJson(self, track_json):
		self.__id = track_json['id']
		self.__name = track_json['name']
		artist = Artist()
		artist.setArtistByJson(track_json['artists'][0])
		self.__artist = artist
		self.__album = track_json['album']
