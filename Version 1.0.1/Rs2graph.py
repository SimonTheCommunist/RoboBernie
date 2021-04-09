import json
import requests
import datetime 
import matplotlib.pyplot as plt
import os
import numpy as np



def NAResortGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"                                                           #sets the datetime format to be compatible with battlemetrics api params

    Dstop = datetime.datetime.now()                                                         #gets the current date and time, to use with battlemetrics api
    stop = Dstop.strftime(format)                                                           #fortmats it
    d = datetime.timedelta(days = 14)                                                       #gets time delta 
    Dstart = Dstop - d                                                                      #gets the starting time
    start = Dstart.strftime(format)                                                         #formats it 
    i = 0                                                                                   #declares i to use in itterations 
    params = {
        "start" : start,
        "stop" : stop   
    }                                                                                       #api calling parameters
    
    url = "https://api.battlemetrics.com/servers/8928472/player-count-history"              #url
    response = requests.get(url, params)                                                    #gets the api response
    json_data = response.json()                                                             #formats it for JSON

    y1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])                                        #declares an numpy array to use with the yaxis of the graph
    x1 = np.array([])                                                                       #declares numpy array to use for the xvalues of the max 
    x2 = np.array([])                                                                       #declares numpy array to use for the x values of the min 
    int(i)                                                                                  #specifies i is an interger
    for i in json_data["data"]:
            x1 = np.append(x1, (i["attributes"]["max"]))                                    #itterates through the dataset and appends values to the array
            x2 = np.append(x2, (i["attributes"]["min"]))
            
    if (x1.shape > y1.shape):
        y1 = np.append(y1, [14])                                                             #sometimes battlemetrics has more then 14 datapoints
                                                                                            #so this appends an extra y value, if that occurs, so when making the graph they can have the same dimension

        

    plt.plot(y1, x1, label="Max players", marker="o")                                       #plots the points
    plt.plot(y1, x2, label="Min players", marker="o")                                       #plots the points
    plt.xlabel("days since 2 weeks ago")                                                     #labels axis
    plt.ylabel("players")                                                                    #labels y axis
    plt.legend()                                                                             #starts the legend
    plt.savefig("images/NA.png")                                                             #saves as an image
    plt.clf()                                                                                 #clears the graph so the other functions dont overlap and shit 

def EUResortGraph():
    format = "%Y-%m-%dT%H:%M:%SZ"                                                             #im not refucking writing these comments lmao 

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

    plt.plot(y1, x3, label="Max players", marker="o")
    plt.plot(y1, x4, label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.legend()
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

    plt.plot(y1, x5, label="Max players", marker="o")
    plt.plot(y1, x6, label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.legend()
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

    plt.plot(y1, x7, label="Max players", marker="o")
    plt.plot(y1, x8, label="Min players", marker="o")
    plt.xlabel("days since 2 weeks ago")
    plt.ylabel("players")
    plt.legend()
    plt.savefig("images/HLL.png")
    plt.clf()
#fig = go.Figure()
#fig.add_trace(go.Scatter(x=y1, y=x1, mode='lines+markers', name='Max'))
#fig.add_trace(go.Scatter(x=y1, y=x2, mode='lines+markers', name='Min'))
#fig.write_image("images/fig1.png")
#fig.show()