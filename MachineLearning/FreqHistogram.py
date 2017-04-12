from Preprocessing import *
import matplotlib.pyplot as plt

plt.hist(Y,bins=10)
plt.title("Ratings distributioin")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()