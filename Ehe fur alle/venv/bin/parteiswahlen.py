# Here we draw graphics for political parties in various selections
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import re

# t = PrettyTable(['sitzung', 'Partei', "sentimental"])

fig = plt.figure()
# Wahlperioden
folders = [ "11","12","13","15", "16", "17", "18", "19"]
##political parties
parteien = ["AFD", "CDU", "FDP", "Grune", "Linke", "SPD"]

#for each partei
for i in range(6):
    #for each wahlperiod
    for j in range(len(folders)):
        #open file
        f = open("Datensatz ParteiSpezifisch/alle/" + parteien[i].lower() + "/" + parteien[i] + folders[j] + "all.xml", "r")
        partei = parteien[i]
        wahl = folders[j]
        #use textblob to analyze the text
        blob = TextBlob(f.read())
        #analyze sentiment of text
        sent = blob.polarity
        #add a data to the graphic (x=j+1,y=sent ,marker="o"(how it will be show (here dots)),color=(here blue))
        plt.scatter(j+1, sent,marker="o",c="b")
    #label of X-axis and Y-axis
    plt.xlabel("Wahlperioden")
    plt.ylabel('sentiment polarity')
    plt.xticks(rotation='vertical')
    # give the graphic a title
    plt.title("partei : " + parteien[i])
    #range of x-axis and y-axis
    plt.axis([0, len(folders)+1, -0.3, +0.3])
    positions = (1,2,3,4,5,6,7,8,9)
    labels=folders
    plt.xticks(positions, labels)
    #save the graphics
    plt.savefig(parteien[i])
    #show the plot
    plt.show()


####DONE