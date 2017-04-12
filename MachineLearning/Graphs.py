from Preprocessing import *
import matplotlib.pyplot as plt
from sys import exit

xco = str(raw_input("Enter desired feature : "))
col = 0
try:
	col = df.columns.get_loc(xco)
except KeyError:
	print("Invalid key")
	exit()
xMat = X[:,col]
plt.plot(Y_OrgI,xMat,"bs")
title = "Rating Vs "+ xco
plt.title(title)
plt.xlabel("Ratings")
plt.ylabel(xco)
plt.show()