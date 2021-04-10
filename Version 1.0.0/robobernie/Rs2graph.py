import json
import requests
import datetime 
import matplotlib.pyplot as plt
import os
import numpy as np



def NAResortGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"

    Dstop = datetime.datetime.now()
    stop = Dstop.strftime(format)
    d = datetime.timedelta(days = 14)
    Dstart = Dstop - d
    start = Dstart.strftime(format)
    i = 0
    params = {
        "start" : start,
        "stop" : stop 
    }
    
    url = "https://api.battlemetrics.com/servers/8928472/player-count-history"
    response = requests.get(url, params)
    json_data = response.json()

    y1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    x1 = np.array([])
    x2 = np.array([])
    int(i)
    for i in json_data["data"]:
            x1 = np.append(x1, (i["attributes"]["max"]))
            x2 = np.append(x2, (i["attributes"]["min"]))
            
    if (x1.shape > y1.shape):
        y1 = np.append(y1, [14])
    

        

    plt.plot(y1, x1, Label="Max players", marker="o")
    plt.plot(y1, x2, Label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.savefig("images/NA.png")
    plt.clf()

def EUResortGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"

    Dstop = datetime.datetime.now()
    stop = Dstop.strftime(format)
    d = datetime.timedelta(days = 14)
    Dstart = Dstop - d
    start = Dstart.strftime(format)
    i = 0
    params = {
        "start" : start,
        "stop" : stop 
    }
    url = "https://api.battlemetrics.com/servers/9766010/player-count-history"
    response = requests.get(url, params)
    json_data = response.json()

    y1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    x3 = np.array([])
    x4 = np.array([])
    int(i)
    for i in json_data["data"]:
            x3 = np.append(x3, (i["attributes"]["max"]))
            x4 = np.append(x4, (i["attributes"]["min"]))
            
    if (x3.shape > y1.shape):
        y1 = np.append(y1, [14])

    plt.plot(y1, x3, Label="Max players", marker="o")
    plt.plot(y1, x4, Label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.savefig("images/EU.png")
    plt.clf()
def terriGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"

    Dstop = datetime.datetime.now()
    stop = Dstop.strftime(format)
    d = datetime.timedelta(days = 14)
    Dstart = Dstop - d
    start = Dstart.strftime(format)
    i = 0
    params = {
        "start" : start,
        "stop" : stop 
    }
    url = "https://api.battlemetrics.com/servers/10139428/player-count-history"
    response = requests.get(url, params)
    json_data = response.json()

    y1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    x5 = np.array([])
    x6 = np.array([])
    int(i)
    for i in json_data["data"]:
            x5 = np.append(x5, (i["attributes"]["max"]))
            x6 = np.append(x6, (i["attributes"]["min"]))
            
    if (x5.shape > y1.shape):
        y1 = np.append(y1, [14])

    plt.plot(y1, x5, Label="Max players", marker="o")
    plt.plot(y1, x6, Label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.savefig("images/Ter.png")
    plt.clf()

def HLLGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"

    Dstop = datetime.datetime.now()
    stop = Dstop.strftime(format)
    d = datetime.timedelta(days = 14)
    Dstart = Dstop - d
    start = Dstart.strftime(format)
    i = 0
    params = {
        "start" : start,
        "stop" : stop 
    }
    url = "https://api.battlemetrics.com/servers/10003552/player-count-history"
    response = requests.get(url, params)
    json_data = response.json()

    y1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    x7 = np.array([])
    x8 = np.array([])
    int(i)
    for i in json_data["data"]:
            x7 = np.append(x7, (i["attributes"]["max"]))
            x8 = np.append(x8, (i["attributes"]["min"]))
            
    if (x7.shape > y1.shape):
        y1 = np.append(y1, [14])

    plt.plot(y1, x7, Label="Max players", marker="o")
    plt.plot(y1, x8, Label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.savefig("images/HLL.png")
    plt.clf()
#fig = go.Figure()
#fig.add_trace(go.Scatter(x=y1, y=x1, mode='lines+markers', name='Max'))
#fig.add_trace(go.Scatter(x=y1, y=x2, mode='lines+markers', name='Min'))
#fig.write_image("images/fig1.png")
#fig.show()