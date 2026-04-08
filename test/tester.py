#Testing for personal finance features

#Testing for personal finance features

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def show_pie_chart():
    sizes = [15, 30, 45, 10]
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Favorite Fruits Distribution')
    plt.show()

def show_line_graph():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    y2 = np.array([2, 4, 2, 13, 0])
    
    plt.figure()
    plt.plot(x, y, label='Savings Added')
    plt.plot(x, y2, label='Spending')
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title("Simple Line Graph")
    plt.legend()
    plt.show()

# Main Window Setup
root = tk.Tk()
root.title("Graph Menu")
root.geometry("300x200")

# Create a Menu Bar
menubar = tk.Menu(root)

# Create the "Graphs" dropdown
graph_menu = tk.Menu(menubar, tearoff=0)
graph_menu.add_command(label="Show Pie Chart", command=show_pie_chart)
graph_menu.add_command(label="Show Line Graph", command=show_line_graph)
graph_menu.add_separator()
graph_menu.add_command(label="Exit", command=root.quit)

# Attach the dropdown to the Menu Bar
menubar.add_cascade(label="Select Graph", menu=graph_menu)

# Set the menu on the window
root.config(menu=menubar)






# Set the menu on the window
root.config(menu=menubar)

# Add a simple instruction label
label = tk.Label(root, text="Select a graph from the menu above", pady=20)
label.pack()

root.mainloop()
