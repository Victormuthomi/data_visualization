import matplotlib.pyplot as plt

prime = [2, 3, 5, 7, 11, 13, 17]


fig, ax = plt.subplots()

ax.plot(prime, linewidth = 3)

ax.set_title("Prime Numbers", fontsize = 14)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("value of prime number", fontsize = 14)

ax.tick_params(labelsize=14)

plt.show()

