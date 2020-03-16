from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import re

#Initiate table
t = PrettyTable(['wahl', 'Partei', "sentimental"])
#initiate plot
fig = plt.figure()
ax = plt.subplot(111)
#wahperioden
folders = [ "15", "16", "17", "18"]
##political parties
parteien = [ "CDU", "FDP", "Grune", "Linke", "SPD"]
c=["black","yellow","green","indianred","firebrick"]

for i in range(5):
    sent=[]
    for j in range(len(folders)):
        #open file
        f = open("Datensatz ParteiSpezifisch/GE/" +  parteien[i].lower() + "/" + parteien[i] + folders[j]+ "GE.xml", "r")
        partei = parteien[i]
        wahl = folders[j]
        #use textblob to analyze the text
        blob = TextBlob(f.read())
        #analyze sentiment of text
        sent.append(blob.polarity)

    # add a data to the graphic (x=folders,y=sent ,marker="o"(how it will be show (here dots)),color=(here blue))
    plt.plot( folders, sent, 'o--',color=c[i])
    #add a row to table
    t.add_row([folders, partei, sent])
    plt.xticks(rotation='vertical')
    #make a legend for graphic
    ax.plot(folders, sent, label=parteien[i], c=c[i])
ax.legend(loc='lower left')
# label of X-axis and Y-axis
plt.ylabel("sentiment")
plt.xlabel("Wahlperioden")
# save the graphic
plt.savefig("15-18")
# show the plot
plt.show()
# print the table
print(t)
t.clear_rows()

##########################
