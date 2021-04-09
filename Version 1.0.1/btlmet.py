import json
import requests
from Rs2graph import terriGraph, NAResortGraph, EUResortGraph, HLLGraph

def NAresort():
    url = "https://api.battlemetrics.com/servers/8928472"
    response = requests.get(url)
    json_data = response.json()
    NAGameMap = json_data["data"]["attributes"]["details"]["map"]
    NAServName = json_data["data"]["attributes"]["name"]
    NAServerSatus = json_data["data"]["attributes"]["status"]
    NAServIP = (str(json_data["data"]["attributes"]["ip"]))+":"+(str(json_data["data"]["attributes"]["port"]))
    NAplayerCount = (str(json_data["data"]["attributes"]["players"])+"/"+(str(json_data["data"]["attributes"]["maxPlayers"])))
    NArank = json_data["data"]["attributes"]["rank"]
    #NAResortGraph()
    return(NAServName, NAGameMap, NAServerSatus, NAServIP, NAplayerCount, NArank)

def EUresort():
    url = "https://api.battlemetrics.com/servers/9766010"
    response = requests.get(url)
    json_data = response.json()
    EUGameMap = json_data["data"]["attributes"]["details"]["map"]
    EUServName = json_data["data"]["attributes"]["name"]
    EUServerSatus = json_data["data"]["attributes"]["status"]
    EUServIP = (str(json_data["data"]["attributes"]["ip"]))+":"+(str(json_data["data"]["attributes"]["port"]))
    EUplayerCount = (str(json_data["data"]["attributes"]["players"])+"/"+(str(json_data["data"]["attributes"]["maxPlayers"])))
    EUrank = json_data["data"]["attributes"]["rank"]
    #EUResortGraph()
    return(EUServName, EUGameMap, EUServerSatus, EUServIP, EUplayerCount, EUrank)

def terri():
    url = "https://api.battlemetrics.com/servers/10139428"
    response = requests.get(url)
    json_data = response.json()
    TEGameMap = json_data["data"]["attributes"]["details"]["map"]
    TEServName = json_data["data"]["attributes"]["name"]
    TEServerSatus = json_data["data"]["attributes"]["status"]
    TEServIP = (str(json_data["data"]["attributes"]["ip"]))+":"+(str(json_data["data"]["attributes"]["port"]))
    TEplayerCount = (str(json_data["data"]["attributes"]["players"])+"/"+(str(json_data["data"]["attributes"]["maxPlayers"])))
    TErank = json_data["data"]["attributes"]["rank"]
    #terriGraph()
    return(TEServName, TEGameMap, TEServerSatus, TEServIP, TEplayerCount, TErank)

def HellLetLoose():
    url = "https://api.battlemetrics.com/servers/10003552"
    response = requests.get(url)
    json_data = response.json()
    HLLGameMap = json_data["data"]["attributes"]["details"]["map"]
    HLLServName = json_data["data"]["attributes"]["name"]
    HLLServerSatus = json_data["data"]["attributes"]["status"]
    HLLServIP = (str(json_data["data"]["attributes"]["ip"]))+":"+(str(json_data["data"]["attributes"]["port"]))
    HLLplayerCount = (str(json_data["data"]["attributes"]["players"])+"/"+(str(json_data["data"]["attributes"]["maxPlayers"])))
    HLLrank = json_data["data"]["attributes"]["rank"]
    #HLLGraph()
    return(HLLServName, HLLGameMap, HLLServerSatus, HLLServIP, HLLplayerCount, HLLrank)
