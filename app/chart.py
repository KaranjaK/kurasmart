from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

nominees = [7, 3]
labels = ['nm1', 'nm2']

plt.pie(nominees, labels=labels,autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Results pie chart")
plt.tight_layout()
plt.show()