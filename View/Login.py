import tkinter
from customtkinter import * 
from PIL import ImageTk, Image
from tkinter import messagebox

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

def button_function():
    root.destroy()
    btn= customtkinter.CTk()

def validate_form(app, entry1, entry2,):
    email = entry1.get()
    password = entry2.get()
    
    if not email:
        messagebox.showerror("Error", "email or password incorrect")
    elif not password:
        messagebox.showerror("Error", "email or password incorrect")
    else:
        button_function()

app = CTk()
app.geometry("900x550")
app.title("Registration")
app.configure (fg_color="silver")



def login():
    email = email_entry.get()
    password = password_entry.get()
# generate gradient in frame1
start_color3 = (255, 215, 0, 0)    # Yellow
end_color3 = (102, 102, 102, 1)       # Red
gradient = generate_gradient_color(start_color3, end_color3, 500, 499)


frame1 = CTkFrame(master=app,fg_color="#FFD700",border_width=0.5, width=4000, height=1000)
frame1.place(relx=0.5,rely=0.5,relwidth=0.25,relheight=0.5,anchor="center")
# Display gradient in frame1

# label1 = CTkLabel(frame1, image=gradient)
# label1.pack()

frame2 = CTkFrame(master=app,fg_color="red", width=400, height=2000, corner_radius=35)
frame2.place(relx=0.5, rely=0.5, anchor="center")

label1 = CTkLabel(frame1, image=gradient)
label1.pack()

CTkLabel(master=app, text="register", font=('arial',20), )
frame2.place(x=1200,y=300,relx=0.5,rely=0.5,relwidth=0.5,relheight=0.5,anchor="center")


frame2= CTkLabel(master=frame1, text="LOGIN", font=('time new roman',20), anchor="center",)
frame2.place(x=135, y=30) 

frame2= CTkLabel(master=frame1, text="My Pocket Sign In.\n stay up to date with your expenses", font=('time new roman',12), anchor="center",)
frame2.place(x=70, y=60) 


frame2= CTkLabel(master=frame1, text="Email", font=('time new roman',16), anchor="center",)
frame2.place(x=45, y=110) 

entry1 = CTkEntry(master=frame1, width=220, placeholder_text="email")
entry1.place(x=45, y=140)

frame2 = CTkLabel(master=frame1, text="Password", font=('time new roman',16),anchor="center", )
frame2.place(x=45, y=170) 

entry2 = CTkEntry(master=frame1, width=220, placeholder_text="surname")
entry2.place(x=45, y=200)

button1 = CTkButton(master=frame1, width=220, text="LOGIN",anchor="center",command=lambda: validate_form(app, entry1, entry2))
button1.place(x=45, y=260)

app.mainloop()