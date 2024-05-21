import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = ([x **3 for x in x_values])

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s=100)

#set the title and axis labels
ax.set_title("Cubes", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Value of cubes", fontsize = 14)

#set the tick labelsiize
ax.tick_params(labelsize=14)
ax.axis([0,100, 0, 1_100_000])

plt.show()

plt.savefig("cubes.png", bbox_inches="tight")

