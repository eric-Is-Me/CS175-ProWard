import requests
import matplotlib.pyplot as plt
import numpy as np

api_key = "RGAPI-58f81372-08c2-4217-8177-6ff2dab9e18c"

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
    return response.json()

def plot_bar_kda():
    index = np.arange(len(kda))
    width = 0.3
    #fig = plt.figure()
    #ax = fig.add_subplot(111) #??
    #rect1 = ax.bar(index, kda, width, color = 'b')
    
    index2 = np.arange(len(kda2))
    rect1 = plt.bar(index, kda, width, color='b')
    rect2 = plt.bar(index2 + width, kda2, width, color='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('KDA score', fontsize=10)
    plt.title('Avg KillDeathAssist Ratio over ' + str(matchCounter) + ' games')
    plt.legend( (rect1[0], rect2[0]), (summonerName + ' (' + str(avg_kda) + ')'\
                                       , summonerName2 + ' (' + str(avg_kda2) + ')') )
    plt.show()

def plot_bar_dpm():
    index = np.arange(len(dpm))
    index2 = np.arange(len(dpm2))
    plt.bar(index, dpm, col='b')
    plt.bar(index2, dpm2, col='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('DPM score', fontsize=10)
    plt.title('Average DamagePerMin over ' + str(matchCounter) + ' games: ' + str(avg_dpm))
    plt.show()

def plot_bar_cspm():
    index = np.arange(len(cspm))
    index2 = np.arange(len(cspm2))
    plt.bar(index, cspm, col='b')
    plt.bar(index2, cspm2, col='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('CSPM', fontsize=10)
    plt.title('Average CreepScorePerMin over ' + str(matchCounter) + ' games: ' + str(avg_cspm))
    plt.show()

def plot_bar_gpm():
    index = np.arange(len(gpm))
    index2 = np.arange(len(gpm2))
    plt.bar(index, gpm, col='b')
    plt.bar(index2, gpm2, col='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('GPM score', fontsize=10)
    plt.title('Average GoldPerMin over ' + str(matchCounter) + ' games: ' + str(avg_gpm))
    plt.show()

def plot_bar_vision():
    index = np.arange(len(vision))
    index2 = np.arange(len(vision2))
    plt.bar(index, vision, col='b')
    plt.bar(index2, vision2, col='r')
    plt.xlabel('games', fontsize=10)
    plt.ylabel('Vision score', fontsize=10)
    plt.title('Average Vision Score over ' + str(matchCounter) + ' games: ' + str(avg_vision))
    plt.show()

# get region and user info
region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in your summoner name: '))
summonerName2 = (str)(input('Type in a pro summoner name: '))

# find information about user from in-game(public) name
name_JSON = requestSummonerName(region, summonerName)
name_JSON2 = requestSummonerName(region, summonerName2)

summonerID = name_JSON['id']
accountID = name_JSON["accountId"]
summonerMastery = requestSummonerMastery(region, summonerID)
summonerID2 = name_JSON2['id']
accountID2 = name_JSON2["accountId"]
summonerMastery2 = requestSummonerMastery(region, summonerID2)

# find list of player's matches to extract data from
matchlist_JSON = requestMatchList(region, accountID)
matchId = []
#gameTime = []
kda = []
dpm = []
vision = []
gpm = []
cspm = []
matchCounter = 0
for matchNo in range(100):
    # We only want to append relevant Summoner's Rift Games. queue: 400, 420
    if matchlist_JSON['matches'][matchNo]['queue'] == 400 \
    or matchlist_JSON['matches'][matchNo]['queue'] == 420:
        matchId.append(matchlist_JSON['matches'][matchCounter]['gameId'])
        matchID = str(matchId[matchCounter])
        match_JSON = requestMatchInfo(region, matchID)
        matchCounter += 1
    
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
        #minutes = int(gameDuration / 60)
        #seconds = gameDuration % 60
        #gameTime = str(minutes) + ':' + str(seconds)
        #gameTime = str(gameTime)    # str like 20:10
        kda.append(round((kills + assists) / deaths, 2))
        dpm.append(round(totalDamageDealtToChampions/gameDuration*60, 2))
        vision.append(visionScore)
        gpm.append(round(goldEarned/gameDuration*60, 2))
        cs = totalMinionsKilled + neutralMinionsKilled
        cspm.append(round(cs/gameDuration*60, 2))
        #matchCounter += 1
        # we only need data for 30 most recent relevant matches
        if matchCounter == 30:
            break

avg_kda = round(sum(kda)/matchCounter, 2)
avg_dpm = round(sum(dpm)/matchCounter, 2)
avg_cspm = round(sum(cspm)/matchCounter, 2)
avg_gpm = round(sum(gpm)/matchCounter, 2)
avg_vision = int(sum(vision)/matchCounter)



matchlist_JSON2 = requestMatchList(region, accountID2)
matchId2 = []
kda2 = []
dpm2 = []
vision2 = []
gpm2 = []
cspm2 = []
matchCounter2 = 0
for matchNo in range(100):
    if matchlist_JSON2['matches'][matchNo]['queue'] == 400 \
    or matchlist_JSON2['matches'][matchNo]['queue'] == 420:
        matchId2.append(matchlist_JSON2['matches'][matchCounter2]['gameId'])
        matchID2 = str(matchId2[matchCounter2])
        match_JSON2 = requestMatchInfo(region, matchID2)
        matchCounter2 += 1
    
        if len(match_JSON2) > 5:
            for pNo in range(10):
                participantName2 = match_JSON2['participantIdentities'][pNo]['player']['summonerName']
                participantName2 = str(participantName2)
                if (participantName2.lower() == summonerName2.lower()):
                    partID2 = match_JSON2['participantIdentities'][pNo]['participantId']
                    break

        # find in-game statistics
        for pNo in range(10):
            if (match_JSON2['participants'][pNo]['participantId'] == partID2):
                gameDuration = match_JSON2['gameDuration']
                kills = match_JSON2['participants'][pNo]['stats']['kills']
                assists = match_JSON2['participants'][pNo]['stats']['assists']
                deaths = match_JSON2['participants'][pNo]['stats']['deaths']        
                if(deaths == 0):
                    deaths = 1
                totalDamageDealtToChampions = match_JSON2['participants'][pNo]['stats']['totalDamageDealtToChampions']
                visionScore = match_JSON2['participants'][pNo]['stats']['visionScore']
                goldEarned = match_JSON2['participants'][pNo]['stats']['goldEarned']
                totalMinionsKilled = match_JSON2['participants'][pNo]['stats']['totalMinionsKilled']
                neutralMinionsKilled = match_JSON2['participants'][pNo]['stats']['neutralMinionsKilled']
        
        kda2.append(round((kills + assists) / deaths, 2))
        dpm2.append(round(totalDamageDealtToChampions/gameDuration*60, 2))
        vision2.append(visionScore)
        gpm2.append(round(goldEarned/gameDuration*60, 2))
        cs = totalMinionsKilled + neutralMinionsKilled
        cspm2.append(round(cs/gameDuration*60, 2))
        if matchCounter2 == 30:# or matchCounter2 == matchCounter:
            break

avg_kda2 = round(sum(kda2)/matchCounter, 2)
avg_dpm2 = round(sum(dpm2)/matchCounter, 2)
avg_cspm2 = round(sum(cspm2)/matchCounter, 2)
avg_gpm2 = round(sum(gpm2)/matchCounter, 2)
avg_vision2 = int(sum(vision2)/matchCounter)






plot_bar_kda()
#plot_bar_dpm()
#plot_bar_cspm()
#plot_bar_gpm()
#plot_bar_vision()

#print("avg kda: ", round(avg_kda, 2))
#print("Total Account Mastery:", summonerMastery)


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
