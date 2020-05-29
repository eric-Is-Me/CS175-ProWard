import requests

api_key = "RGAPI-dd94f66a-0bb3-4b1a-997a-9e3c5443a9c5"

def requestSummonerName(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerMastery(region, summonerName):
    thingything = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + summonerName
    

#def request other stuff


print("Let's see if this works\n")
region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in a summoner name: '))

responseJSON = requestSummonerName(region, summonerName)
ID = responseJSON['id']
#ID = str(ID)
print(ID)

'''
API_version = {
 #       '/lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}'
    'CHAMPION-MASTERY': '4'
        }

REGIONS = {
        'North_America': 'NA1'
        }
'''
