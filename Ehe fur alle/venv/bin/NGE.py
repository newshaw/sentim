#count sentiment analysis for  debate ,that are not  about the same gender marriage
# #----------------------------------------------------

from textblob_de import TextBlobDE as TextBlob
from prettytable import PrettyTable
import matplotlib.pyplot as plt

#making a table and define it's columns
t = PrettyTable(['Wahlperiod','sitzung','sentimental'])
fig = plt.figure()
sent=[]
#debatte
fnames=["10184","11035","11037","11194","12104","12132","12185","13022","13185","16222","17201","17244","18207","19068"]
for i in range(len(fnames)):
    #open the file
    f = open("Datensatz nicht GE/"+"NGE_"+fnames[i] + ".xml", "r")
    Wahl=fnames[i][0] + fnames[i][1]
    sitz=fnames[i][2] + fnames[i][3] + fnames[i][4]
    blob = TextBlob(f.read())
    # Count the sentimental polarity of the debate
    sent.append(blob.polarity)
    # add a row to table per each debate
    t.add_row([Wahl, sitz , sent[i]])
# ploting the graph with x-axis = debate, y-axis = sentiment of each debate, linear form )
plt.plot(fnames, sent, "o--", color="b")
plt.xticks(rotation='vertical')
#give range to axis
plt.axis([0, len(fnames) + 1, -0.3, +0.3])
plt.title("Nicht Gleich Geschlecht Ehe")
#save the graphic
plt.savefig("ng2")
#show table
print(t)
#show graphic
plt.show()



