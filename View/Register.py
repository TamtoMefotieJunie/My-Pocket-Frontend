from PIL import Image, ImageTk
import bcrypt
import sqlite3
import subprocess
import tkinter as tk
import customtkinter
from tkinter import messagebox
import sys
import os

from ..constants import Users

# from Backend.Models.Users import *
# import Backend


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'..','Backend')))


def generate_gradient_color(start_color, end_color, width, height):
    gradient = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            # Interpolate between start and end colors based on y position
            r = int(start_color[0] + (end_color[0] - start_color[0]) * y / height)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * y / height)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * y / height)
            gradient.putpixel((x, y), (r, g, b))

    return ImageTk.PhotoImage(gradient)
#button_function
def button_function():
    window.destroy()
    w = customtkinter.CTk()
    w.geometry('1280x720')
    w.title('Welcome')
    l1 = customtkinter.CTkLabel(master=window, text="Home Page", font=('arial', 70))
    l1.pack()
    w.mainloop()
    

def register_user(name, email, password):
    # Connect to the database
    conn = sqlite3.connect("db.sqlite")
    
    cursor = conn.cursor()

    # Insert the user's data into the database
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   (name, email, password))
    conn.commit()

    # Close the database connection
    conn.close()

    # Display a success message
    messagebox.showinfo("Registration", "Registration successful!")
    
    # Open login.py in a new process
    subprocess.Popen(["python", "Login.py"])

#validate form
def validate_form(window, entry1, entry2, entry3, entry4):
    name = entry1.get()
    email = entry2.get()
    password = entry3.get()
    confirm_password = entry4.get()

    if not name:
        messagebox.showerror("Error", "Please enter your name")
    elif not email:
        messagebox.showerror("Error", "Please enter your email")
    elif not password:
        messagebox.showerror("Error", "Please enter your password")
    elif not confirm_password:
        messagebox.showerror("Error", "Please confirm your password")
    else:
        register_user(name, email, password)
        button_function()
        

# Create a tkinter window
window = tk.Tk()
window.title("Gradients")
window.geometry("600x400")



window1 = tk.Frame(window, width=4000, height=2500, bg="",)
window1.place(x=0, y=0)

window0 = tk.Frame(window, width=4000, height=2500, bg="Light Gray",padx=200, pady=5)
window0.place(x=-90, y=-115, )
image = Image.open("images/wallet.jpg")

# Resize the image
resized_image = image.resize((600, 650))

# Create a PhotoImage from the resized image
img1 = ImageTk.PhotoImage(resized_image)

l1 = customtkinter.CTkLabel(master=window0, image=img1)
l1.place(x=300, y=233)

# Frame 1 (with more depth)
frame1 = tk.Frame(window0, width=300, height=400, bg="lightblue", borderwidth='0',)
frame1.place(x=740, y=230 )

# Generate gradient in frame3 1
start_color1 = (201, 196, 196, 1)  # Red
end_color1 = (201, 196, 196, 1)    # Blue
gradient1 = generate_gradient_color(start_color1, end_color1, 450, 650)

# Display gradient in frame3 1
label1 = tk.Label(frame1, image=gradient1)
label1.pack()

# Frame 2 (with a little less depth)
frame2 = tk.Frame(window0, width=250, height=350, bg="lightgray")
frame2.place(x=769, y=255)

# Generate gradient in frame3 2
start_color2 =(201, 196, 196, 1)    # Green
end_color2 =(201, 196, 196, 1)    # Yellow
gradient2 = generate_gradient_color(start_color2, end_color2, 390, 600)

# Display gradient in frame3 2
label2 = tk.Label(frame2, image=gradient2)
label2.pack()

# Frame 3 (with the least depth)
frame3 = tk.Frame(window0, width=200, height=300, bg="lightyellow")
frame3.place(x=769, y=255)

# Generate gradient in frame3 3
start_color3 = (255, 215, 0, 0)    # Yellow
end_color3 = (102, 102, 102, 1)       # Red
gradient3 = generate_gradient_color(start_color3, end_color3, 390, 600)

# Display gradient in frame3 3
label3 = tk.Label(frame3, image=gradient3)
label3.pack()

l2 = customtkinter.CTkLabel(master=frame3, text="REGISTER", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1,anchor=tk.CENTER, x=-195,y=-560)

l2 = customtkinter.CTkLabel(master=frame3, text="My Pocket signup form.\nStay up" "to date with your expenses", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1,anchor=tk.CENTER, x=-195,y=-500)

l2 = customtkinter.CTkLabel(master=frame3, text="Name", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1, x=-320,y=-440)

entry1 = customtkinter.CTkEntry(master=frame3, width=280, placeholder_text="Name", bg_color="#C9C4C4")
entry1.place(relx=1, rely=1, x=-320,y=-390)
print(sys.path)

l2 = customtkinter.CTkLabel(master=frame3, text="Email", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1, x=-320,y=-340)

entry2 = customtkinter.CTkEntry(master=frame3, width=280, placeholder_text="Email",bg_color="#C9C4C4" )
entry2.place(relx=1, rely=1, x=-320,y=-280)

l2 = customtkinter.CTkLabel(master=frame3, text="Password", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1, x=-320,y=-230)

entry3 = customtkinter.CTkEntry(master=frame3, width=280, placeholder_text="Password",show="*", bg_color="#C9C4C4")
entry3.place(relx=1, rely=1, x=-320,y=-180)

l2 = customtkinter.CTkLabel(master=frame3, text="Confirm password", font=('Times New Roman',20,"italic"), )
l2.place(relx=1, rely=1, x=-320,y=-130)

entry4 = customtkinter.CTkEntry(master=frame3, width=280, placeholder_text="Confirm password",show="*", bg_color="#C9C4C4")
entry4.place(relx=1, rely=1, x=-320,y=-80)

button1 = customtkinter.CTkButton(master=frame3, width=280, text="Register", command=lambda: validate_form(window, entry1, entry2,entry3, entry4))
button1.place(relx=1, rely=1, x=-320,y=-30)


# Start the tkinter event loop
window.mainloop()