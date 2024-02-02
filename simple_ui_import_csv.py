import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.pdfgen import canvas

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cure Analysis Tool")
        self.root.geometry("1024x768")

        # Load Button
        load_button = tk.Button(root, text="Select Load", comman=self.load_csv)
        load_button.grid(row=0, column=0, padx=10, pady=10)

        # Tabs
        self.notebook = ttk.Notebook(root)
        tabs = ["Load Overview", "Temperature", "Pressure", "Vacuum", "Heat Rate", "Dwell Time", "Report"]
        for tab in tabs:
            frame =tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab)

        self.notebook.grid(row=0, column=1, padx=10, pady=10)

        # Save Reports button
        save_reports_button = tk.Button(root, text="Save Report", command=self.save_reports)
        save_reports_button.grid(row=5, column=0, padx=10, pady=10)

        # Frame withing the "Data" tab
        data_frame = tk.Frame(self.notebook)
        data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Text widget for displaying data in the "Data" tab
        self.data_tree = ttk.Treeview(data_frame)
        self.data_tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Configure the horizontal scrollbar
        data_scrollbar_x = ttk.Scrollbar(data_frame, orient="horizontal", command=self.data_tree.xview)
        data_scrollbar_y = ttk.Scrollbar(data_frame, orient="vertical", command=self.data_tree.xview)
        #data_scrollbar_x.grid(row=1, column=0, sticky="we")

        self.data_tree.configure(xscrollcommand=data_scrollbar_x.set, yscrollcommand=data_scrollbar_y.set)

        # Add the Frame to the "Data" tab
        self.notebook.insert(6, data_frame, text="Data")

    # Function to import CSV data
    def load_csv(self):
        file_path = filedialog.askopenfilename(title="Select Load file", filetypes=[("CSV file", "*.csv")])

        if file_path:
            temp = pd.read_csv(file_path, skiprows=8, nrows=1, header=None)
            temp = temp.dropna(axis=1, how='all')
            df = pd.read_csv(file_path, header=None, skiprows=10)
            df = df.dropna(axis=1, how='all')
            df.columns = temp.iloc[0]

            print(df.columns)
            # Add cumulative time column
            time_column = 'Time'
            tc_columns = [col for col in df.columns if 'TC' in col]

            df['Cumulative time'] = df[time_column].cumsum()

            # Add rate column for each TC column
            for tc_col in tc_columns:
                rate_col_name = f"{tc_col} Rate"
                df[rate_col_name] = df[tc_col].diff() / df[time_column].diff()

            self.data_tree.delete(*self.data_tree.get_children())
            self.data_tree["columns"] = tuple(df.columns)

            # Insert data into the Treeview
            for _, row in df.iterrows():
                self.data_tree.insert("", tk.END, values=row.tolist())
    
    def save_reports(self):
        pass

        

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
    