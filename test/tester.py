#Testing for personal finance features

import matplotlib.pyplot as plt

# Data for the pie chart
sizes = [15, 30, 45, 10]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # Optional: define custom colors

# Create the pie chart
plt.figure(figsize=(6, 6)) # Optional: adjust figure size
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90) #

# Add a title
plt.title('Favorite Fruits Distribution')

# Display the plot
plt.show()


#Examples for line graph
import numpy as np

# 1. Prepare data for the x-axis and y-axis
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
z = np.array([1, 3, 5, 7, 9])
f = np.array([2, 4, 6, 8, 10])
# 2. Use the plot() function to create the line chart
plt.plot(x, y)
plt.plot(z, f)
# 3. Add labels and a title for clarity (optional, but recommended)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Graph")

# 4. Display the chart
plt.show()