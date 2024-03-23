import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os  # Import the os module
from Data import expense_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        



class Dashboard:
    
    def __init__(self,window):
        self.window = window
        self.window.title = ('My pocket Dashboard')
        self.window.config(background = '#BEC7C8')
        self.window.state('zoomed')
        
        
        #window icon
        # icon = PhotoImage(file='image')
        #==================== main content =================#
        self.content = Frame(self.window, bg="#FFFFFF", bd=50)
        self.content.place(x=420,y=20,width=1400,height=935)
        
        #==================== sidebar =================#
        self.sidebar = Frame(self.window,bg="#BEC7C8", bd=50,padx=50,pady=50)
        self.sidebar.place(x=30,y=20,width=360,height=750)
        
        #logo
        # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "logo.png")

        # Load the image
       
        self.logoImage = Image.open(image_path)
        self.logo_photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image= self.logo_photo,bg="#BEC7C8")
        self.logo.image_names=self.logo_photo
        self.logo.place(x=-70,y=-20,height=100,width=300)
        
         #dashboard
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "dashboard.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=100,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Dashboard",cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#B69216")
        self.dashboard_text.place(x=20,y=105)
        
        
        
        #Research
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "research.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=160,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Research",cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=168)
        
         #analysis
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "analysis.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=220,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Analysis",cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=231)
        
        #history
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "history.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=280,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="History",cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=294)
        
        #==================== navbar =================#
        self.navbar = Frame(self.window, bd=50)
        self.navbar.place(x=420,y=25,width=1070,height=90)
        
        #search bar
       

        # Create the search entry
        entry = tk.Entry(self.navbar, width=30)
           
        entry.place(x=270,y=0,width=200)

        # Create the search button
        search_button = Button(self.navbar,text="Search", command=search)
        search_button.place(x=480,y=-6)
        
   
        
        self.person_text = Label(self.navbar,text="Tamto Mefotie Junie",font=("", 16, "normal"),bd=0,fg="#000000")
        self.person_text.place(x=750,y=0)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "junie.png")
        self.personImage = Image.open(image_path)
        self.person_icon = ImageTk.PhotoImage(self.personImage)
        self.person = Label(self.navbar, image= self.person_icon,bg="#FDE48E")
        self.person.image_names=self.person_icon
        self.person.place(x=570,y=-50,height=120,width=150)
        
        #=======================================================
        #========================Body==========================#
        
      
        
        
def search():
    query = entry.get()
    # Perform search action here
    print("Searching for:", query) 
     
        
def win():
    window = tk.Tk()
    window.title('My pocket Dashboard')
    Dashboard(window)
    window.mainloop()
    

win()