#count sentiment analysis for every debate
# #----------------------------------------------------

from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt
#making a table and define it's columns
t = PrettyTable(['Wahlperiod','sitzung','sentimental'])
fig = plt.figure()
sent = []
#Debate
fnames=["10184","11035","11037","11194","12104","12132","12185","13022","13185","15119","15136","16017","16063","16079","16105","16197","16222","17126","17187","17201","17228","17244","18006","18088","18112","18155","18199","18207","18244"]
for i in range(len(fnames)):
    #open the file
    f = open("Datensatz alle/"+fnames[i] + ".xml", "r")
    Wahl=fnames[i][0] + fnames[i][1]
    sitz=fnames[i][2] + fnames[i][3] + fnames[i][4]
    blob = TextBlob(f.read())
    # Count the sentimental polarity of the debate
    sent.append(blob.polarity)
    # add a row to table per erach debate
    t.add_row([Wahl, sitz , sent])
# ploting the graph with x-axis = debate, y-axis = sentiment of each debate, linear form )
plt.plot(fnames ,sent,"o--",)
plt.xticks(rotation='vertical')
plt.axis([0, len(fnames) + 1, -0.3, +0.3])
plt.title("Alle")
#save the graphic
plt.savefig("all2")
#show table
print(t)
#show plot
plt.show()



