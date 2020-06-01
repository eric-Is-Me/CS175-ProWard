import requests
import time
api_key = "RGAPI-662349ed-9a07-4632-b76a-36c103558c78"

def requestSummonerName(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestSummonerMastery(region, summonerID):
    URL = 'https://' + region + '.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/' + summonerID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestMatchList(region, accountID):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountID + '?api_key=' + api_key
    response = requests.get(URL)
    return response.json()

def requestMatchInfo(region, matchID):
    URL = 'https://' + region + '.api.riotgames.com/lol/match/v4/matches/' + matchID + '?api_key=' + api_key
    response = requests.get(URL)
    #if 'URL' not in response
    return response.json()


# get region and user info
region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in a summoner name: '))

# find information about user from in-game(public) name
name_JSON = requestSummonerName(region, summonerName)
summonerID = name_JSON["id"]
accountID = name_JSON["accountId"]
summonerMastery = requestSummonerMastery(region, summonerID)

# find list of player's matches to extract data from
matchlist_JSON = requestMatchList(region, accountID)
matchId = []
gameTime = []
kda = []
dpm = []
vision = []
gpm = []
cs = []
matchCounter = 0
for matchNo in range(100):
    matchId.append(matchlist_JSON['matches'][matchNo]['gameId'])
    matchID = str(matchId[matchNo])
    match_JSON = requestMatchInfo(region, matchID)
    
    # print (match_JSON)
    # print (matchNo)
    if len(match_JSON) > 5:
        # find correct participant(player) in single match
        for pNo in range(10):
            participantName = match_JSON['participantIdentities'][pNo]['player']['summonerName']
            participantName = str(participantName)
            if (participantName.lower() == summonerName.lower()):
                partID = match_JSON['participantIdentities'][pNo]['participantId']
                break

        # find in-game statistics
        for pNo in range(10):
            if (match_JSON['participants'][pNo]['participantId'] == partID):
                gameDuration = match_JSON['gameDuration']
                kills = match_JSON['participants'][pNo]['stats']['kills']
                assists = match_JSON['participants'][pNo]['stats']['assists']
                deaths = match_JSON['participants'][pNo]['stats']['deaths']        
                if(deaths == 0):
                    deaths = 1
                totalDamageDealtToChampions = match_JSON['participants'][pNo]['stats']['totalDamageDealtToChampions']
                visionScore = match_JSON['participants'][pNo]['stats']['visionScore']
                goldEarned = match_JSON['participants'][pNo]['stats']['goldEarned']
                totalMinionsKilled = match_JSON['participants'][pNo]['stats']['totalMinionsKilled']
                neutralMinionsKilled = match_JSON['participants'][pNo]['stats']['neutralMinionsKilled']
        
        #minutes.append(int(gameDuration / 60))
        minutes = int(gameDuration / 60)
        seconds = gameDuration % 60
        gameTime = str(minutes) + ':' + str(seconds)
        gameTime = str(gameTime)
        kda.append(round((kills + assists) / deaths, 2))
        dpm.append(round(totalDamageDealtToChampions/gameDuration/60, 2))
        vision.append(visionScore)
        gpm.append(round(goldEarned/gameDuration/60, 2))
        cs.append(totalMinionsKilled + neutralMinionsKilled)
        matchCounter += 1
        
print(kda)
avg_kda = sum(kda)/matchCounter
print("avg kda: ", round(avg_kda, 2))
print("Total Account Mastery:", summonerMastery)


#pip the poro id: IS6jAFiLaj6yy3xcSpyIDpTMRvFEG6Vh3ph-I7RVhdyV7_M
    #my acct
    #mastery: 90
#doublelift id: XV7kJbSAgcQO_JCx8EWs7grADevXPzUlR9QBV6oMvqpjwIg
    #famous pro
    #mastery: 302
#c9 zvennn  id: RT0KducVYCbEwdnUrfQg5c1sh2LzIS2vXYuff336wrMeOo4
    #rank 1
    #mastery: 315
#tl tactical id: t5G8-JWkv9AvJqPIApk-nxiH0hd2kUZ1lnT_lTlKEvtXNpvM
    #rank 3
    #mastery: 290
#c9 zven id: WlP8-ALvIffYzMgcSLoA2Cj6zXqNtKXw24GEmEDe3azcFXc
    #rank 5
    #mastery: 349
