import matplotlib.pyplot as plt

even_numbers = [2, 4, 6, 8, 10, 12, 14]

fig, ax = plt.subplots()

ax.plot(even_numbers, linewidth = 3)

# set the title and axix labels

ax.set_title("Even numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Value of prime number", fontsize = 14)

ax.tick_params(labelsize= 14)

plt.show()
