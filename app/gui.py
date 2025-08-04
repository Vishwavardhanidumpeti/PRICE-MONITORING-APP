import tkinter as tk
from tkinter import messagebox
from main import run_monitor

def start_monitoring():
    product = product_entry.get()
    budget = budget_entry.get()
    duration = duration_entry.get()

    if not product or not budget or not duration:
        messagebox.showerror("Error", "Please enter all fields.")
        return

    try:
        budget = float(budget)
        duration = int(duration)
    except ValueError:
        messagebox.showerror("Error", "Budget must be a number. Duration must be an integer.")
        return

    messagebox.showinfo("Started", f"Monitoring for '{product}' under ₹{budget} for {duration} mins.")
    run_monitor(product, budget, duration)

# GUI setup
root = tk.Tk()
root.title("Product Price Monitor")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="🔍 Product Name").pack(pady=5)
product_entry = tk.Entry(root, width=40)
product_entry.pack()

tk.Label(root, text="💰 Budget (₹)").pack(pady=5)
budget_entry = tk.Entry(root, width=40)
budget_entry.pack()

tk.Label(root, text="⏱️ Duration (Minutes)").pack(pady=5)
duration_entry = tk.Entry(root, width=40)
duration_entry.pack()

tk.Button(root, text="Start Monitoring", command=start_monitoring, bg="green", fg="white").pack(pady=20)

root.mainloop()
