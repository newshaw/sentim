#die Wahlperiode 18
from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import re

##Initiate table
t = PrettyTable(['sitzung', 'Partei', "sentimental"])
fig = plt.figure()
ax = plt.subplot(111)
##political parties
parteien = [ "CDU", "Grune", "Linke", "SPD"]
#color of each partei
c = ["black", "green", "red", "firebrick"]

for i in range(4):
    sitz = []
    sent = []
    # open the file
    f = open("18/" + parteien[i] + "18all.xml","r")
    #read the file
    text=f.read()
    partei = parteien[i]
    # find different debate in each file (Wahlperiode)
    res = [p.start() for p in re.finditer("<ID>", text)]
    for r in range(len(res)):
            sitz.append(text[res[r] + 11] + text[res[r] + 12] + text[res[r] + 13])
            s = text.find("<text>", res[r])
            e = text.find("</textNode>", res[r])
            # use textblob to analyze the text
            blob = TextBlob(text[s:e])
            # Count the sentimental polarity of the debate
            sent.append(blob.polarity)
            # add a row to table per each debate
            t.add_row([sitz[r], partei, sent[r]])
    # ploting the graph with x-axis = debate, y-axis = sentiment of each debate, linear form and color of each partei)
    plt.plot(sitz, sent, 'o--', color=c[i])
    #make a legend
    ax.plot(sitz, sent, label=parteien[i], c=c[i])
    plt.xticks(rotation='vertical')
#show the table
print(t)
# label of X-axis and Y-axis
plt.xlabel("Debate")
plt.ylabel('sentiment polarity')
plt.title("wahlperiode 18")
ax.legend(loc='upper left')
# show the plot
plt.show()

