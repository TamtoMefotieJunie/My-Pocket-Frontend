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


root.geometry("1150x1150")
# Container
container_frame = tk.Frame(root, bg="grey", padx=15, pady=15)
container_frame.pack(expand=True, fill="both")

# Navbar
navbar_frame = tk.Frame(container_frame,bg="grey")
navbar_frame.grid(row=0, column=0)

# Content
content_frame = tk.Frame(container_frame, bg="white", padx=15, pady=15)
content_frame.grid(row=0, column=1)

# Navbar Elements
links = ["Dashboard", "Finance", "Analysis", "History"]

for i, link_text in enumerate(links):
    link_label = tk.Label(navbar_frame,bg="grey", text=link_text, font=("Arial", 12, "bold"), padx=5,)
    link_label.grid(row=i, column=0,pady=5,padx=5)
    

# Content Elements
top_frame = tk.Frame(content_frame,bg="white")
top_frame.pack()
search_entry = tk.Entry(top_frame, bd=0,bg="#e0e0e0", relief="solid", width=20,font=("Arial",15))
search_entry.grid(row=1,column=1,pady=20,padx=0)
search_entry.insert(0, "Quick search...")

welcome_label = tk.Label(top_frame, text="Welcome",bg="white", font=("Arial", 12, "bold"))
welcome_label.grid(row=7, column=0)

name_label = tk.Label(top_frame, text="Ostie",bg="white" ,font=("Arial", 10), fg="grey")
name_label.grid(row=8, column=0)

frequency_var = tk.IntVar()
weekly_radio = tk.Radiobutton(top_frame,bg="white", text="Weekly", variable=frequency_var, value=1, command="")
weekly_radio.grid(row=7, column=2)
monthly_radio = tk.Radiobutton(top_frame,bg="white", text="Monthly", variable=frequency_var, value=2, command="")
monthly_radio.grid(row=7, column=3)



username_label = tk.Label(top_frame, text="Ostie Brown",bg="white", font=("Arial", 9, "bold"))
username_label.grid(row=1,column=3)
extx_label = tk.Label(top_frame, text="EXPENSES",bg="white", font=("Arial", 14, "bold"))
extx_label.grid(row=9,column=1,pady=5)

revenue_button = tk.Button(top_frame,text="Enter your revenue", bg="#B8860B", bd=0,font=("Arial",10,"bold") ,relief="solid", command=open_modal,height=2,width=20)
revenue_button.grid(row=10,column=0,pady=10)

food_check = tk.Checkbutton(top_frame,bd=0)
food_check.grid(row=11,column=0)
check_textf = tk.Label(top_frame, text="Food",bg="white", font=("Arial", 9))
check_textf.grid(row=11, column=1,pady=15)
check_textc = tk.Label(top_frame, text="Category                             Amount Spent: 20,000XFA",bg="white", font=("Arial", 9, "bold"))
check_textc.grid(row=11, column=2)
descboard_label1 = tk.Label(top_frame, text="Desc", bg="#FCD77D", padx=15, pady=15,width=30)
descboard_label1.grid(row=12,column=0,pady=10)

food_check2 = tk.Checkbutton(top_frame,bd=0)
food_check2.grid(row=13,column=0,pady=15)
check_textf2 = tk.Label(top_frame, text="Food",bg="white", font=("Arial", 9))
check_textf2.grid(row=13, column=1)
check_textc2 = tk.Label(top_frame, text="Category                             Amount Spent: ",bg="white", font=("Arial", 9, "bold"))
check_textc2.grid(row=13, column=2,pady=15)

food_check3 = tk.Checkbutton(top_frame,bd=0)
food_check3.grid(row=14,column=0,pady=15)
check_textf3 = tk.Label(top_frame, text="Food",bg="white", font=("Arial", 9))
check_textf3.grid(row=14, column=1)
check_textc3 = tk.Label(top_frame, text="Category                             Amount Spent:",bg="white", font=("Arial", 9, "bold"))
check_textc3.grid(row=14, column=2)

descboard_label1 = tk.Label(top_frame, text="Desc", bg="#FCD77D", padx=15, pady=15,width=30)
descboard_label1.grid(row=15,column=0,pady=10)

next_button = tk.Button(top_frame, text="Next", bg="#B8860B", bd=0, relief="raised",width=25,height=2, command=open_modal)
next_button.grid(row=16,column=3)

# Modal Window
modal_window = tk.Toplevel(root)
modal_window.title("Enter Revenue")
modal_window.geometry("250x100")
modal_window.protocol("WM_DELETE_WINDOW", close_modal)
modal_window.withdraw()

modal_content_frame = tk.Frame(modal_window)
modal_content_frame.pack(padx=20, pady=20)

revenue_label = tk.Label(modal_content_frame, text="Please provide us your revenue:")
revenue_label.pack()

revenue_entry = tk.Entry(modal_content_frame,font=("Arial",14))
revenue_entry.pack()

submit_button = tk.Button(modal_content_frame, text="Submit", bg="#B8860B", bd=0, relief="solid",width=10)
submit_button.pack(pady=10)
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
container_frame.grid_columnconfigure(0,weight=1)
container_frame.grid_rowconfigure(0,weight=1)
root.mainloop()
