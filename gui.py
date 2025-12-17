import tkinter as tk
from tkinter import ttk
from convertor import convert_currency, get_currency_list
from historical_trends import show_trends_gui


root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x400")

#Fetch currency options
try:
    currency_options = get_currency_list()
except Exception as e:
    currency_options = []
    print("Error fetching currency list:", e)

tk.Label(root, text="Amount").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="From Currency").pack(pady=5)
from_currency = tk.StringVar(value="USD")
from_combo = ttk.Combobox(root, textvariable=from_currency, values=currency_options)
from_combo.pack()

tk.Label(root, text="To Currency").pack(pady=5)
to_currency = tk.StringVar(value="INR")
to_combo = ttk.Combobox(root, textvariable=to_currency, values=currency_options)
to_combo.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        converted_amount = convert_currency(amount, from_curr, to_curr)
        result_label.config(text=f"{amount} {from_curr} = {converted_amount:.2f} {to_curr}")
    except ValueError:
        result_label.config(text="Enter a valid amount!")
    except Exception as e:
        result_label.config(text=str(e))

tk.Label(root, text="Select Days of History").pack(pady=5)
days_var = tk.StringVar(value="7")  # Default to 7
days_combo = ttk.Combobox(root, textvariable=days_var, values=["7", "14", "30"])
days_combo.pack()
days_combo.current(0)

tk.Button(root, text="Convert", command=on_convert).pack(pady=10)

def show_trends():
    base = from_currency.get()
    target = to_currency.get()
    try:
        days = int(days_var.get())
    except ValueError:
        days = 7
    show_trends_gui(base, target, days)

tk.Button(root, text="📈 Show Trends", command=show_trends).pack(pady=5)

root.mainloop()
