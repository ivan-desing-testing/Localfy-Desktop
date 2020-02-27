class Artist():

	def __init__(self):
		self.__id = ''
		self.__name = ''
	
	def getId(self):
		return self.__id

	def getName(self):
		return self.__name

	def setArtistByJson(self, artists_json):
		self.__id = artists_json['id']
		self.__name = artists_json['name']