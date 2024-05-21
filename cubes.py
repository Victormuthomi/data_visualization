import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = ([x **3 for x in x_values])

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c = y_values, cmp = plt.cm.Blues, s=10)

