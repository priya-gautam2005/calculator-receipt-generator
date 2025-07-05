import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# === Data Storage ===
item_counts = {}
item_prices = {}
button_refs = {}
total = 0

# === Predefined Items ===
available_items = [
    ("Dairy Milk", 40),
    ("Maggi", 15),
    ("Amul Butter", 52),
    ("Bread", 25),
    ("Milk (1L)", 50),
    ("Toothpaste", 30),
    ("Soap", 20),
    ("Shampoo", 60),
    ("Pen Pack", 35),
    ("Notebook", 55)
]

# === Add Item Function ===
def add_predefined_item(name, price):
    global total
    item_prices[name] = price
    item_counts[name] = item_counts.get(name, 0) + 1
    total += price
    total_label.config(text=f"🧾 Total: ₹{total}")
    update_button(name)

# === Update Button Text and Color ===
def update_button(name):
    btn = button_refs.get(name)
    if btn:
        count = item_counts[name]
        new_text = f"{name}\n₹{item_prices[name]}\nQty: {count}"
        btn.config(text=new_text)
        if count == 1:
            btn.config(bg="#cce0ff")  # First click turns button blue

# === Show Receipt ===
def show_receipt():
    if not item_counts:
        messagebox.showinfo("No Items", "🛒 No items selected yet!")
        return

    receipt_win = tk.Toplevel(root)
    receipt_win.title("🧾 Final Receipt")
    receipt_win.configure(bg="#fffbe6")

    # Header
    tk.Label(receipt_win, text="🛍️ Shree Ram General Store 🛍️", font=("Arial", 16, "bold"), bg="#fffbe6", fg="#9933ff").pack(pady=5)
    tk.Label(receipt_win, text=f"🕒 {datetime.now().strftime('%d-%m-%Y  %I:%M %p')}", font=("Arial", 10), bg="#fffbe6").pack()

    # Item List
    tk.Label(receipt_win, text="\n🧾 Your Items:", font=("Arial", 13, "bold"), fg="#333", bg="#fffbe6").pack(anchor="w", padx=20)

    for i, (item, qty) in enumerate(item_counts.items(), 1):
        price = item_prices[item]
        line_total = qty * price
        tk.Label(receipt_win, text=f"{i}. {qty} x {item} @ ₹{price} = ₹{line_total}", font=("Arial", 12), bg="#fffbe6").pack(anchor="w", padx=40)

    # Total
    tk.Label(receipt_win, text=f"\n🧾 Total Bill: ₹{total}", font=("Arial", 13, "bold"), fg="#004d00", bg="#fffbe6").pack(pady=10)

    # Footer
    tk.Label(receipt_win, text="🙏 Thank you for shopping! Visit Again 🙏", font=("Arial", 11, "italic"), fg="#800000", bg="#fffbe6").pack(pady=10)

# === GUI Setup ===
root = tk.Tk()
root.title("🧾 Shree Ram Store")
root.geometry("520x520")
root.configure(bg="#f0f8ff")

# === Stylish Header and Instruction ===
tk.Label(root, 
         text="🛍️✨ Welcome to Shree Ram General Store ✨🛍️", 
         font=("Arial", 16, "bold"), 
         bg="#f0f8ff", 
         fg="#003366").pack(pady=(10, 2))

tk.Label(root, 
         text="🧾 Select your favourite items below !", 
         font=("Arial", 11, "bold"), 
         bg="#f0f8ff", 
         fg="#444", 
         justify="center").pack(pady=(0, 8))

# === Items Grid ===
item_frame = tk.Frame(root, bg="#f0f8ff")
item_frame.pack()

for i, (name, price) in enumerate(available_items):
    btn = tk.Button(item_frame,
                    text=f"{name}\n₹{price}",
                    font=("Arial", 10),
                    width=16,
                    height=3,
                    bg="#ffe6e6",  # Default color
                    fg="#000000",
                    command=lambda n=name, p=price: add_predefined_item(n, p))
    btn.grid(row=i // 2, column=i % 2, padx=8, pady=5)
    button_refs[name] = btn

# === Total Label ===
total_label = tk.Label(root, text="🧾 Total: ₹0", font=("Arial", 13, "bold"), fg="#006666", bg="#f0f8ff")
total_label.pack(pady=10)

# === Show Receipt Button ===
tk.Button(root, text="🧾 Show Receipt", font=("Arial", 12), bg="#ffcccc", fg="#800000", command=show_receipt).pack(pady=10)

# === Footer ===
tk.Label(root, text="🔸 Shree Ram Store - Est. 2024 🔸", font=("Arial", 10, "italic"), fg="#888", bg="#f0f8ff").pack(side="bottom", pady=5)

root.mainloop()