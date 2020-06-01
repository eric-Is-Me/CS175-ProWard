import requests

api_key = "RGAPI-662349ed-9a07-4632-b76a-36c103558c78"

def requestSummonerName(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerMastery(region, summonerID):
    URL = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + summonerID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

#def request other stuff

def requestMatchList(region, accountID):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestMatchInfo(region, matchID):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v4/matches/' + matchID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()
   


region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in a summoner name: '))

name_JSON = requestSummonerName(region, summonerName)
summonerID = name_JSON['id']
# total account game mastery
summonerMastery = requestSummonerMastery(region, summonerID)

accountID = name_JSON['accountId']
matchlist_JSON = requestMatchList(region, accountID)
matchId = matchlist_JSON['matches'][0]['gameId']
matchID = str(matchId)
match_JSON = requestMatchInfo(region, matchID)

for pNo in range(10):
    participantName = match_JSON['participantIdentities'][pNo]['player']['summonerName']
    participantName = str(participantName)
    #print("pName:",participantName)
    if (participantName.lower() == summonerName.lower()):
        partID = match_JSON['participantIdentities'][pNo]['participantId']
        break
#print("participant ID:", partID)

for pNo in range(10):
    if (match_JSON['participants'][pNo]['participantId'] == partID):
        gameDuration = match_JSON['gameDuration']
        kills = match_JSON['participants'][pNo]['stats']['kills']
        assists = match_JSON['participants'][pNo]['stats']['assists']
        deaths = match_JSON['participants'][pNo]['stats']['deaths']        
        totalDamageDealtToChampions = match_JSON['participants'][pNo]['stats']['totalDamageDealtToChampions']
        visionScore = match_JSON['participants'][pNo]['stats']['visionScore']
        goldEarned = match_JSON['participants'][pNo]['stats']['goldEarned']
        totalMinionsKilled = match_JSON['participants'][pNo]['stats']['totalMinionsKilled']
        neutralMinionsKilled = match_JSON['participants'][pNo]['stats']['neutralMinionsKilled']

# important in-game stats
kda = (kills + assists)/deaths
minutes = int(gameDuration / 60)
kda = round((kills + assists)/deaths, 2)
dpm = round(totalDamageDealtToChampions/minutes, 2)
vision = visionScore
gpm = round(goldEarned/minutes, 2)
cs = totalMinionsKilled + neutralMinionsKilled

#championId = requestMatchInfo['championId']

#print(summonerID)
print("Total Account Mastery:", summonerMastery)


#pip the poro id: IS6jAFiLaj6yy3xcSpyIDpTMRvFEG6Vh3ph-I7RVhdyV7_M
    #my acct
    #90
    # acct id: fL_4VTvcp3LYbm9S1xQ78FFtZVG_VdWAQgnXeuMROWycN8s
    # recent gameId: 3402933367
'''
Steps to finding game scores
def-> matchlist by acct
get "gameId"

def-> match by matchid
match player id

calc kda = (kills + assists) / deaths
"gameDuration" (in seconds)
"totalDamageDealtToChampions"
"visionScore"
"goldEarned"
"totalMinionsKilled"
"neutralMinionsKilled"


#should probably add player acct rank
'''
    
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
