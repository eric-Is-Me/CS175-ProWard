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
    #if 'URL' not in response
    return response.json()

def plot_bar_kda():
    # this is for plotting purpose
    index = np.arange(len(kda))
    plt.bar(index, kda)
    plt.xlabel('games', fontsize=10)
    plt.ylabel('KDA score', fontsize=10)
    plt.title('Avg KillDeathAssist Ratio over ' + str(matchCounter) + ' games: ' + str(avg_kda))
    plt.show()

def plot_bar_dpm():
    index = np.arange(len(dpm))
    plt.bar(index, dpm)
    plt.xlabel('games', fontsize=10)
    plt.ylabel('DPM score', fontsize=10)
    plt.title('Average DamagePerMin over ' + str(matchCounter) + ' games: ' + str(avg_dpm))
    plt.show()

def plot_bar_cspm():
    # this is for plotting purpose
    index = np.arange(len(cspm))
    plt.bar(index, cspm)
    plt.xlabel('games', fontsize=10)
    plt.ylabel('CSPM', fontsize=10)
    plt.title('Average CreepScorePerMin over ' + str(matchCounter) + ' games: ' + str(avg_cspm))
    plt.show()

def plot_bar_gpm():
    index = np.arange(len(gpm))
    plt.bar(index, gpm)
    plt.xlabel('games', fontsize=10)
    plt.ylabel('GPM score', fontsize=10)
    plt.title('Average GoldPerMin over ' + str(matchCounter) + ' games: ' + str(avg_gpm))
    plt.show()

def plot_bar_vision():
    index = np.arange(len(vision))
    plt.bar(index, vision)
    plt.xlabel('games', fontsize=10)
    plt.ylabel('Vision score', fontsize=10)
    plt.title('Average Vision Score over ' + str(matchCounter) + ' games: ' + str(avg_vision))
    plt.show()

# get region and user info
region = (str)(input('Type in a region: '))
summonerName = (str)(input('Type in a summoner name: '))

# find information about user from in-game(public) name
name_JSON = requestSummonerName(region, summonerName)

summonerID = name_JSON['id']
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
cspm = []
matchCounter = 0
for matchNo in range(100):
    matchId.append(matchlist_JSON['matches'][matchNo]['gameId'])
    matchID = str(matchId[matchNo])
    match_JSON = requestMatchInfo(region, matchID)
    
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
        matchCounter += 1
        

kda_scores = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, \
    6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
avg_kda = round(sum(kda)/matchCounter, 2)
avg_dpm = round(sum(dpm)/matchCounter, 2)
avg_cspm = round(sum(cspm)/matchCounter, 2)
avg_gpm = round(sum(gpm)/matchCounter, 2)
avg_vision = int(sum(vision)/matchCounter)

plot_bar_kda()
plot_bar_dpm()
plot_bar_cspm()
plot_bar_gpm()
plot_bar_vision()

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
