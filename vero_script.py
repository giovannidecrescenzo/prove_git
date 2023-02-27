import numpy as np
import matplotlib.pyplot as plt

#I want to do some real shit on the cluster.

x = np.random.normal(0,3.1, 100000)
y = np.random.normal(10,2.1, 100000)

fig, ax = plt.subplot()
ax.hist(x,bins = 1000, alpha = 0.8, label = "SSSSEEEEEE", color = "skyblue")
ax.hist(y,bins = 1000, alpha = 0.8, label = "SSSSEEEEEE", color = "red")
plt.label()
plt.show()

