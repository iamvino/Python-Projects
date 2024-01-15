# Importing modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Creating database connection
conn = sqlite3.connect("restaurant.db")
c = conn.cursor()

# Creating tables for menu and orders
c.execute("""CREATE TABLE IF NOT EXISTS menu (
            item TEXT,
            price REAL
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            item TEXT,
            quantity INTEGER,
            total REAL
            )""")

# Inserting some sample menu items
menu_items = [
    ("Hawaiian", 7.50),
    ("Champagne Ham & Cheese", 7.50),
    ("Beef & Onion", 7.50),
    ("Pepperoni", 7.50),
    ("Simply Cheese", 7.50),
    ("Bacon & Mushroom", 7.50),
    ("Italiano", 7.50),
    ("The Deluxe", 13.50),
    ("Ham, Egg & Hollandaise", 13.50),
    ("Americano", 13.50),
    ("Mr Wedge", 13.50),
    ("BBQ Meatlovers", 13.50)
]

c.executemany("INSERT INTO menu VALUES (?, ?)", menu_items)
conn.commit()

# Creating the main window
root = tk.Tk()
root.title("Restaurant POS System")
root.geometry("800x600")

# Creating the frames for menu, order and summary
menu_frame = tk.LabelFrame(root, text="Menu", padx=10, pady=10)
menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

order_frame = tk.LabelFrame(root, text="Order", padx=10, pady=10)
order_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

summary_frame = tk.LabelFrame(root, text="Summary", padx=10, pady=10)
summary_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Creating the treeview for menu
menu_tree = ttk.Treeview(menu_frame, columns=(1,2), show="headings", height=12)
menu_tree.pack(side="left")

menu_tree.heading(1, text="Item")
menu_tree.heading(2, text="Price")

menu_tree.column(1, width=200)
menu_tree.column(2, width=100)

# Creating the scrollbar for menu
menu_scroll = ttk.Scrollbar(menu_frame)
menu_scroll.pack(side="right", fill="y")

menu_tree.configure(yscrollcommand=menu_scroll.set)
menu_scroll.configure(command=menu_tree.yview)

# Inserting the menu items into the treeview
c.execute("SELECT * FROM menu")
menu_records = c.fetchall()

for record in menu_records:
    menu_tree.insert("", "end", values=record)

# Creating the treeview for order
order_tree = ttk.Treeview(order_frame, columns=(1,2,3), show="headings", height=12)
order_tree.pack(side="left")

order_tree.heading(1, text="Item")
order_tree.heading(2, text="Quantity")
order_tree.heading(3, text="Total")

order_tree.column(1, width=200)
order_tree.column(2, width=100)
order_tree.column(3, width=100)

# Creating the scrollbar for order
order_scroll = ttk.Scrollbar(order_frame)
order_scroll.pack(side="right", fill="y")

order_tree.configure(yscrollcommand=order_scroll.set)
order_scroll.configure(command=order_tree.yview)

# Creating the labels and entries for summary
subtotal_label = tk.Label(summary_frame, text="Subtotal:")
subtotal_label.grid(row=0, column=0)

subtotal_entry = tk.Entry(summary_frame)
subtotal_entry.grid(row=0, column=1)

tax_label = tk.Label(summary_frame, text="Tax:")
tax_label.grid(row=1, column=0)

tax_entry = tk.Entry(summary_frame)
tax_entry.grid(row=1, column=1)

total_label = tk.Label(summary_frame, text="Total:")
total_label.grid(row=2, column=0)

total_entry = tk.Entry(summary_frame)
total_entry.grid(row=2, column=1)

# Creating the buttons for adding, removing and paying
add_button = tk.Button(summary_frame, text="Add", width=10)
add_button.grid(row=3, column=0, padx=10, pady=10)

remove_button = tk.Button(summary_frame, text="Remove", width=10)
remove_button.grid(row=3, column=1, padx=10, pady=10)

pay_button = tk.Button(summary_frame, text="Pay", width=20)
pay_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Defining the functions for the buttons
def add_item():
    # Getting the selected menu item
    selected_item = menu_tree.focus()
    item_values = menu_tree.item(selected_item, "values")

    # Checking if the item is already in the order
    order_items = order_tree.get_children()
    for item in order_items:
        if order_tree.item(item, "values")[0] == item_values[0]:
            # Updating the quantity and total of the existing item
            new_quantity = int(order_tree.item(item, "values")[1]) + 1
            new_total = round(new_quantity * float(item_values[1]), 2)
            order_tree.item(item, values=(item_values[0], new_quantity, new_total))
            update_summary()
            return

    # Inserting the new item into the order with quantity 1 and total equal to price
    order_tree.insert("", "end", values=(item_values[0], 1, item_values[1]))
    update_summary()

def remove_item():
    # Getting the selected order item
    selected_item = order_tree.focus()
    item_values = order_tree.item(selected_item, "values")

    # Checking if the quantity is more than 1
    if int(item_values[1]) > 1:
        # Reducing the quantity and total of the existing item
        new_quantity = int(item_values[1]) - 1
        new_total = round(new_quantity * float(item_values[2]) / int(item_values[1]), 2)
        order_tree.item(selected_item, values=(item_values[0], new_quantity, new_total))
        update_summary()
    else:
        # Deleting the item from the order
        order_tree.delete(selected_item)
        update_summary()

def pay_order():
    # Getting the order items
    order_items = order_tree.get_children()

    # Checking if the order is empty
    if len(order_items) == 0:
        messagebox.showerror("Error", "The order is empty.")
        return

    # Inserting the order items into the database
    for item in order_items:
        item_values = order_tree.item(item, "values")
        c.execute("INSERT INTO orders (item, quantity, total) VALUES (?, ?, ?)", item_values)

    # Committing the changes and showing a success message
    conn.commit()
    messagebox.showinfo("Success", "The order has been paid.")

    # Clearing the order and summary
    order_tree.delete(*order_tree.get_children())
    subtotal_entry.delete(0, "end")
    tax_entry.delete(0, "end")
    total_entry.delete(0, "end")

def update_summary():
    # Getting the order items
    order_items = order_tree.get_children()

    # Calculating the subtotal, tax and total
    subtotal = 0
    for item in order_items:
        subtotal += float(order_tree.item(item, "values")[2])

    tax_rate = 0.05 # Change this according to your location
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    # Updating the summary entries
    subtotal_entry.delete(0, "end")
    subtotal_entry.insert(0, subtotal)

    tax_entry.delete(0, "end")
    tax_entry.insert(0, tax)

    total_entry.delete(0, "end")
    total_entry.insert(0, total)

# Binding the buttons to the functions
add_button.configure(command=add_item)
remove_button.configure(command=remove_item)
pay_button.configure(command=pay_order)

# Running the main loop
root.mainloop()

# Closing the database connection
conn.close()