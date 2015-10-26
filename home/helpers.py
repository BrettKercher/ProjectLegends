def getSummonerUrl(region, summoner):
	return '/api/lol/' + region + '/v1.4/summoner/by-name/' + summoner

def getMatchUrl(region, id):
	return '/api/lol/' + region + '/v1.3/game/by-summoner/' + str(id) + '/recent'