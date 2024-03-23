import tkinter as tk

def open_modal():
    modal_window.deiconify()

def close_modal():
    modal_window.withdraw()

def handle_frequency_change():
    if frequency_var.get() == 1:
        open_modal()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x400")

# Container
container_frame = tk.Frame(root, bg="grey", padx=15, pady=15)
container_frame.pack(expand=True, fill="both")

# Navbar
navbar_frame = tk.Frame(container_frame)
navbar_frame.grid(row=0, column=0)

# Content
content_frame = tk.Frame(container_frame, bg="white", padx=15, pady=15)
content_frame.grid(row=0, column=1)

# Navbar Elements
links = ["Dashboard", "Finance", "Analysis", "History"]

for i, link_text in enumerate(links):
    link_label = tk.Label(navbar_frame, text=link_text, font=("Arial", 12, "bold"), padx=5)
    link_label.grid(row=i, column=0)

# Content Elements
top_frame = tk.Frame(content_frame)
top_frame.pack()

welcome_label = tk.Label(top_frame, text="Welcome", font=("Arial", 16, "bold"))
welcome_label.grid(row=0, column=0)

name_label = tk.Label(top_frame, text="Steve", font=("Arial", 12), fg="grey")
name_label.grid(row=0, column=1)

frequency_var = tk.IntVar()
weekly_radio = tk.Radiobutton(top_frame, text="Weekly", variable=frequency_var, value=1, command=handle_frequency_change)
weekly_radio.grid(row=1, column=0)
monthly_radio = tk.Radiobutton(top_frame, text="Monthly", variable=frequency_var, value=2, command=handle_frequency_change)
monthly_radio.grid(row=1, column=1)

search_entry = tk.Entry(content_frame, bd=1, relief="solid", width=40)
search_entry.insert(0, "Quick search...")
search_entry.pack(pady=10)

username_label = tk.Label(content_frame,  font=("Arial", 12, "bold"))
username_label.pack(side="right")

revenue_button = tk.Button(content_frame, text="Enter your revenue", bg="#B8860B", bd=1, relief="solid", command=open_modal)
revenue_button.pack()

food_check = tk.Checkbutton(content_frame, text="Food category ⇦ Amount Spent: 20,000XFA")
food_check.pack()

descboard_label1 = tk.Label(content_frame, text="Desc", bg="lightyellow", padx=15, pady=15)
descboard_label1.pack()

food_check2 = tk.Checkbutton(content_frame, text="transport category ⇦ Amount Spent:")
food_check2.pack()

food_check3 = tk.Checkbutton(content_frame, text="Food category ⇦ Amount Spent:")
food_check3.pack()

descboard_label2 = tk.Label(content_frame, text="Desc", bg="lightyellow", padx=15, pady=15)
descboard_label2.pack()

next_button = tk.Button(content_frame, text="Next", bg="#B8860B", bd=1, relief="solid")
next_button.pack()

# Modal Window
modal_window = tk.Toplevel(root)
modal_window.title("Enter Revenue")
modal_window.geometry("400x200")
modal_window.protocol("WM_DELETE_WINDOW", close_modal)
modal_window.withdraw()

modal_content_frame = tk.Frame(modal_window)
modal_content_frame.pack(padx=20, pady=20)

revenue_label = tk.Label(modal_content_frame, text="Please provide us your revenue:")
revenue_label.pack()

revenue_entry = tk.Entry(modal_content_frame)
revenue_entry.pack()

submit_button = tk.Button(modal_content_frame, text="Submit", bg="#B8860B", bd=1, relief="solid")
submit_button.pack()

root.mainloop()
