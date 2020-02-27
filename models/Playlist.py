from models.Track import *

class Playlist():

	def __init__(self):
		self.__id = ''
		self.__name = ''
		self.__description = ''
		self.__external_url = ''
		self.__image = ''
		self.__tracks = []
	
	def getId(self):
		return self.__id
	
	def getName(self):
		return self.__name
	
	def getDescription(self):
		return self.__description

	def getExternalUrl(self):
		return self.__external_url

	def getImage(self):
		return self.__image

	def getTracks(self):
		return self.__tracks

	def setPlaylistByJson(self, playlist_json):
		self.__id = playlist_json["id"]
		self.__name = playlist_json["name"]
		self.__description = playlist_json["description"]
		self.__image = playlist_json['images'][0]['url']

		try:
			items_result = []
			for item in playlist_json['tracks']['items']:
				track = Track()
				track.setTrackByJson(item["track"])
				items_result.append(track)
			self.__tracks = items_result
		except:
			self.__tracks = []

		

