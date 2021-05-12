import matplotlib.pyplot as plt

labels = ['USA', 'India', 'Brazil', 'Russia', 'UK']
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
# Highlight the USA rate
explode = (0.1, 0, 0, 0, 0)
colors = ['red', 'yellow', 'orange', 'blue', 'white']

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True)
# Make the plot rounder
plt.axis('equal')

plt.show()
