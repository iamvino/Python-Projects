import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def import_csv_data():
    global df
    csv_file_path = filedialog.askopenfilename()
    df = pd.read_csv(csv_file_path)
    print(df)

# Function to perform calculations
def perform_calculations():
    # Perform your calculations here
    # For example, calculate the mean of a column
    mean_value = df['Time'].mean()
    print(mean_value)

# Function to plot chart
def plot_chart():
    # Create figure and axis
    fig, ax = plt.subplots()
    # Plot a histogram using pandas plot function
    df['Time'].plot(kind='hist', ax=ax)
    # Create tkinter canvas with figure
    chart = FigureCanvasTkAgg(fig, root)
    # Draw the canvas
    chart.draw()
    # Get the canvas widget and pack it into the window
    chart_widget = chart.get_tk_widget()
    chart_widget.pack()

# Create a new Tkinter window
root = tk.Tk()

# Set the window size
root.geometry("600x300") # Width X Height

# Create 'Import CSV' button
import_button = tk.Button(root, text="Import CSV", command=import_csv_data)
import_button.pack()

# Create 'Perform Calculations' button
calculate_button = tk.Button(root, text="Perform Calculations", command=perform_calculations)
calculate_button.pack()

# Create 'Plot Chart' button
plot_button = tk.Button(root, text="Plot Chart", command=plot_chart)
plot_button.pack()

# Start the Tkinter event loop
root.mainloop()
