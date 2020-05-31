import requests

api_key = "RGAPI-3393b39f-548a-46e5-b636-e10dc64a17a3"

def requestSummonerName(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerMastery(region, summonerID):
    URL = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + summonerID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

#def request other stuff

def allknowing(region, accountID):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()


region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in a summoner name: '))

name_JSON = requestSummonerName(region, summonerName)
summonerID = name_JSON['id']
summonerMastery = requestSummonerMastery(region, summonerID)

print(summonerID)
print(summonerMastery)

accountID = name_JSON['accountId']
allinfo = allknowing(region,accountID)
print(allinfo)
'''
API_version = {
 #       '/lol/champion-mastery/v4/scores/by-summoner/{encryptedSummonerId}'
    'CHAMPION-MASTERY': '4'
        }

REGIONS = {
        'North_America': 'NA1'
        }
'''


#pip the poro id: IS6jAFiLaj6yy3xcSpyIDpTMRvFEG6Vh3ph-I7RVhdyV7_M
    #90
#doublelift id: XV7kJbSAgcQO_JCx8EWs7grADevXPzUlR9QBV6oMvqpjwIg
    #famous pro
    #302
#c9 zvennn  id: RT0KducVYCbEwdnUrfQg5c1sh2LzIS2vXYuff336wrMeOo4
    #rank 1
    #315
#tl tactical id: t5G8-JWkv9AvJqPIApk-nxiH0hd2kUZ1lnT_lTlKEvtXNpvM
    #rank 3
    #290
#c9 zven id: WlP8-ALvIffYzMgcSLoA2Cj6zXqNtKXw24GEmEDe3azcFXc
    #rank 5
    #349
