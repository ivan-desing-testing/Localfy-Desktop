import csv

def getOauthParameters():
    parameters = dict()
    with open ('repository/oauth_parameters.csv') as document:
        reader = csv.reader(document)
        for row in reader:
            parameters[row[0]] = row[1]
    return parameters

def getLocalSavesPlaylists():
    parameters = dict()
    with open('repository/saved_playlists.csv') as document:
        reader = csv.reader(document)
        for row in reader:
            parameters[row[0]] = row[1]
    return parameters

