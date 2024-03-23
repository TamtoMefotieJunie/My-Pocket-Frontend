import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os  # Import the os module
from Data import expense_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess


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
        self.content.place(x=450,y=20,width=1400,height=935)
        
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
        self.logo.place(x=-60,y=115,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Dashboard",cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#B69216")
        self.dashboard_text.place(x=20,y=115)
        
        
        
        #Research
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "research.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=178,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Research",cursor="hand2",activebackground="#B69216",command=show_expense,font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=178)
        
         #analysis
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "analysis.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=241,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="Analysis",cursor="hand2",command=show_actions,activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=241)
        
        #history
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "history.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.dash_icon = ImageTk.PhotoImage(self.iconImage)
        self.logo = Label(self.sidebar, image= self.dash_icon,bg="#BEC7C8")
        self.logo.image_names=self.dash_icon
        self.logo.place(x=-60,y=304,height=50,width=50)
        self.dashboard_text = Button(self.sidebar,text="History", command=show_history,cursor="hand2",activebackground="#B69216",font=("", 16, "bold"),bg="#BEC7C8",bd=0,fg="#000000")
        self.dashboard_text.place(x=20,y=304)
        
        #==================== navbar =================#
        self.navbar = Frame(self.window, bd=50)
        self.navbar.place(x=450,y=25,width=1400,height=90)
        
        #search bar
       

        # Create the search entry
        entry = tk.Entry(self.navbar, width=30)
           
        entry.place(x=270,y=0,width=250)

        # Create the search button
        search_button = Button(self.navbar,text="Search", command=search)
        search_button.place(x=570,y=-6)
        
   
        
        self.person_text = Label(self.navbar,text="Tamto Mefotie Junie",font=("", 16, "normal"),bd=0,fg="#000000")
        self.person_text.place(x=950,y=0)
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "junie.png")
        self.personImage = Image.open(image_path)
        self.person_icon = ImageTk.PhotoImage(self.personImage)
        self.person = Label(self.navbar, image= self.person_icon,bg="#FDE48E")
        self.person.image_names=self.person_icon
        self.person.place(x=700,y=-50,height=120,width=200)
        
        #=======================================================
        #========================Body==========================#
        
        self.heading = Label(self.window, bg="#FFFFFF", text='Welcome', font=("", 20, "bold"), fg="#000000")
        self.heading.place(x=470,y=130)
        self.person = Label(self.window, bg="#FFFFFF", text='Junie', font=("", 18, "bold"), fg="#BEC7C7")
        self.person.place(x=470,y=175)
         #================Bodyframe1================#
       
        self.bodyFrame1 = Frame(self.window, bg="#B69216")
        self.bodyFrame1.place(x=470,y=220,width=400,height=300)
        
        # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "income.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.income_icon = ImageTk.PhotoImage(self.iconImage)
        self.income = Label(self.bodyFrame1, image= self.income_icon,bg="#FDE48E")
        self.income.image_names=self.income_icon
        self.income.place(x=20,y=15,height=150,width=200)
        self.income_text = Label(self.bodyFrame1,text="Income",font=("", 20, "bold"),bg="#B69216",bd=0,fg="#FDE48E")
        self.income_text.place(x=250,y=210)
        self.income_price = Label(self.bodyFrame1,text="250000XFA",font=("", 20, "bold"),bg="#B69216",bd=0,fg="#FDE48E")
        self.income_price.place(x=250,y=243)
        
         #================Bodyframe2================#
        
        self.bodyFrame2 = Frame(self.window, bg="#6AA6C3")
        self.bodyFrame2.place(x=932,y=220,width=400,height=300)
        
         # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "expense.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.exp_icon = ImageTk.PhotoImage(self.iconImage)
        self.exp = Label(self.bodyFrame2, image= self.exp_icon,bg="#ACCDDE")
        self.exp.image_names=self.exp_icon
        self.exp.place(x=20,y=15,height=150,width=200)
        self.exp_text = Label(self.bodyFrame2,text="Expense",font=("", 20, "bold"),bg="#6AA6C3",bd=0,fg="#ACCDDE")
        self.exp_text.place(x=250,y=210)
        self.exp_price = Label(self.bodyFrame2,text="200000XFA",font=("", 20, "bold"),bg="#6AA6C3",bd=0,fg="#ACCDDE")
        self.exp_price.place(x=250,y=243)
         #================Bodyframe3================#
        
        self.bodyFrame3 = Frame(self.window, bg="#77EE59")
        self.bodyFrame3.place(x=1400,y=220,width=400,height=300)
        
        # Construct the absolute path to the image file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir,"images", "savings.png")

        # Load the image
       
        self.iconImage = Image.open(image_path)
        self.save_icon = ImageTk.PhotoImage(self.iconImage)
        self.save = Label(self.bodyFrame3, image= self.save_icon,bg="#B1EFA1")
        self.save.image_names=self.save_icon
        self.save.place(x=20,y=15,height=150,width=200)
        self.save_text = Label(self.bodyFrame3,text="Savings",font=("", 20, "bold"),bg="#77EE59",bd=0,fg="#B1EFA1")
        self.save_text.place(x=250,y=210)
        self.save_price = Label(self.bodyFrame3,text="50000XFA",font=("", 20, "bold"),bg="#77EE59",bd=0,fg="#B1EFA1")
        self.save_price.place(x=250,y=243)
         #================Bodyframe4================#
        
        self.bodyFrame4 = Frame(self.window, bg="#ffffff", highlightthickness=2, 
                 highlightbackground='#BEC7C7', highlightcolor='#BEC7C7')
        self.bodyFrame4.place(x=470,y=530,width=1300,height=400)
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#6AA6C3","#BE96FF","#957DAD","#5E366E","#A98CCC","#BEC7C8"]
        )
        #chart
        chart, ax1 = plt.subplots()
        ax1.bar(expense_data.keys(), expense_data.values())
        ax1.set_title("statistics of the year")
        ax1.set_xlabel("Months")
        ax1.set_ylabel("amounts in FCFA")
        # plt.show()
        canvas1 = FigureCanvasTkAgg(chart,self.bodyFrame4)
        canvas1.draw()
        canvas1.get_tk_widget().place(width=1270,height=400)

        
def show_history():
    subprocess.call(["python", "History.py"])     
def show_expense():
    subprocess.call(["python", "Expense.py"])     
def show_actions():
    subprocess.call(["python", "Frontend/View/Action.py"])     

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