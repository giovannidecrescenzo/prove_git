import numpy as np
import matplotlib.pyplot as plt

#I want to do some real shit on the cluster.

x = np.random.normal(0,3.1, 100000)
y = np.random.normal(10,2.1, 100000)
plt.hist(x,bins = 1000, alpha = 0.8, label = "SSSSEEEEEE", color = "skyblue")
plt.hist(y,bins = 1000, alpha = 0.8, label = "SSSSEEEEEE", color = "red")
plt.savefig("megaplot.png")

