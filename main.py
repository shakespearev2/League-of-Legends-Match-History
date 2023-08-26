import requests
import tkinter

api_key = "RGAPI-d52a3e4c-a3c8-48f1-bc37-5fcc37d3ae40"
api_accinfo = "https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
api_getmatches = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
api_getmatchesdetails = "https://europe.api.riotgames.com/lol/match/v5/matches/"

matchcount= 0
mathcount_end = 3

while mathcount_end > matchcount:
    def accinfo():
        entery_user = "Owner Tr"
        username = entery_user.replace(" ", "%20")
        rqlink = api_accinfo + username + "?api_key=" + api_key
        rq = requests.get(rqlink)
        return rq.json()

    getaccinfo = accinfo()
    def matches():
        puuid = getaccinfo["puuid"]
        rqlink = api_getmatches + puuid + "/ids?api_key=" + api_key
        rq = requests.get(rqlink)
        getmatches = rq.json()
        getmatches_link = api_getmatchesdetails + getmatches[matchcount] + "?api_key=" + api_key
        getmatches_rq = requests.get(getmatches_link)
        return getmatches_rq.json()

    getmatches = matches()
    userpuuid = getaccinfo["puuid"]

    champlist = getmatches["info"]['participants']
    counter = 0

    for x in champlist:
        if(getmatches["info"]['participants'][counter]["puuid"] == userpuuid):
            break
        else:
            counter += 1

    def matchhistory():
        kills = getmatches["info"]['participants'][counter]['kills']
        deaths = getmatches["info"]['participants'][counter]['deaths']
        assists = getmatches["info"]['participants'][counter]['assists']
        champselect = getmatches["info"]['participants'][counter]['championName']
        return print(f"Champ: {champselect}, Kill: {kills}, Death: {deaths}, Assists: {assists}")


    matchhistory()
    matchcount += 1

#WINDOW

window = tkinter.Tk()


















