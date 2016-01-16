import pandas as pd
import os.path
import heapq
import numpy as np
import matplotlib.pyplot as plt
#'C:/Purchase_Orders__ADPICS__-_Jan_2008_to_current'
df = pd.read_csv(os.path.normpath("C:/Purchase_Orders__ADPICS__-_Jan_2008_to_current.csv"))
#df = df.head(20)
#print(df.values)
#print(df.columns)
print("----------------------")
print(df.columns.values.tolist()) # put the each of the columns into an array of a multi-dimensional array
d = df["Amount"] # get amount of each company
d = zip(df.Amount, df.VendorName)
d = list(d)


d = [( float(x[0]), x[1] ) for x in d if str(x[0]) != 'nan']
#d = [float(i) for i in d]
#print(sorted(list(d)))
#df.sort(reverse=True)

print("HEAP")
topTen = heapq.nlargest(10, d)
print(topTen)

print("----------")

N = 10
ind = np.arange(N)    # the x locations for the groups
width = 0.7       # the width of the bars: can also be len(x) sequence

#ind is the x coordinates of the left sides of the bars
#second is a list containing all values of bars
#third is just color
p1 = plt.bar(ind, [x[0] for x in topTen] , width, color='r')

#label of y axis

plt.ylabel('Amount')

#title of graph
plt.title('The Top Ten Companies of Miami Dade by Revenue')

#distance between markers of x-axis
#second argument are x labels for each marker
plt.xticks(ind + .35, [x[1][:3] for x in topTen])

#yticks is the distance between y values on plot
#Uses np.arange which takes in a start value, an end value, and the intervals in between these values that should be marked.
plt.yticks(np.arange(0, 250000000, 20000000))

plt.show()

