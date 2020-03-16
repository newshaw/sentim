#count sentiment analysis for  debate about the same gender marriage
# #----------------------------------------------------

from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt


#making a table and define it's columns
t = PrettyTable(['Wahlperiod','sitzung','sentimental'])

sent=[]
#debate
fnames=["15119","15136","16017","16063","16079","16105","16197","17126","17187","17228","18006","18088","18112","18155","18199","18244"]


for i in range(len(fnames)):
    #open the file
    f  = open("Datensatz GE/"+"GE_"+fnames[i] + ".xml", "r")
    Wahl=fnames[i][0] + fnames[i][1]
    sitz=fnames[i][2] + fnames[i][3] + fnames[i][4]
    # use textblob to analyze the text
    blob = TextBlob(f.read())
    # analyze sentiment of text
    sent.append(blob.polarity)
    # add a row to table per each debate
    t.add_row([Wahl, sitz , sent[i]])
# ploting the graph with x-axis = debate, y-axis = sentiment of each debate, linear form )
plt.plot(fnames, sent, "o--", color="b")
plt.xticks(rotation='vertical')
#give range to axis
plt.axis([0, len(fnames) + 1, -0.3, +0.3])
plt.title("Gleich Geschlecht Ehe")
# save the graphic
plt.savefig("ge2")
print(t)
plt.show()
