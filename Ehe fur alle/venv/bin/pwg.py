# analysis sentiment of debate in Parliament for  each partei in election periods "Wahlperioden"
# #----------------------------------------------------

from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import re

#making a tabel and define it's columns
t = PrettyTable(['sitzung', 'Partei', "sentimental"])

fig = plt.figure()
ax = plt.subplot(111)


#Wahlperioden
folders = [ "11","12","13","15","16","17","18"]
parteien = [ "CDU", "FDP", "Grune", "Linke", "SPD"]
c = ["black", "yellow", "green", "indianred", "firebrick"]

for i in range(5):
    sitz = []
    sent = []
    for j in range(len(folders)):
        f = open("Datensatz ParteiSpezifisch/alle/" + parteien[i].lower() + "/" + parteien[i] + folders[j] + "all.xml","r")

        partei = parteien[i]
        wahl = folders[j]
        #use textblob to analyze the text
        blob = TextBlob(f.read())
        # Count the sentimental polarity of the election period"wahleperiod"
        sent.append(blob.polarity)
        print(sent)
        # add a row to table per each election period
        t.add_row([wahl, partei, sent[j]])
    print(sent)
    plt.plot(folders, sent, 'o--', color=c[i])
    #make a legend
    ax.plot(folders, sent, label=parteien[i], c=c[i])
    plt.xticks(rotation='vertical')
#give a location to legend
ax.legend(loc='upper left')
# save the graphic
plt.savefig("p_all")
# show the plot
plt.show()
print(t)
####
