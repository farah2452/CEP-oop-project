
from tkinter import *
from PIL import Image, ImageTk

# ************************** Sign-in class ***************************
class Signin:
    def signin_form(self, master=None, user_image=None, user_icon=None, pass_icon=None, bg = "white", bd=2, relief=RIDGE, place_x=0, place_y=0):

        # user icon image in the username frame
        self.login_frame = Frame(master, bg=bg, relief=relief, bd=bd)  # frame for username & password
       
        if user_image != None:
            self.usericon = ImageTk.PhotoImage(Image.open(user_image).resize((90, 90), Image.ANTIALIAS))
            self.usericonlab = Label(self.login_frame, image=self.usericon, bg=bg, bd=0).pack(pady=20)

        self.usernameframe = Frame(self.login_frame, bg=bg)
    
        self.username = StringVar()
        self.password = StringVar()
        
        if user_icon != None:
            self.user_icon = PhotoImage(file=user_icon)
            self.usernamelab = Label(self.usernameframe, image=self.user_icon, text="Username", font="Times 15", compound=LEFT, bg=bg).grid(sticky="w", row=0, column=0, padx=25, pady=10)
        else:
            self.usernamelab = Label(self.usernameframe, text="Username", font="Times 15", bg=bg).grid(sticky="w", row=0, column=0, padx=25, pady=10)    
        
        self.enter_username = Entry(self.usernameframe, textvariable=self.username, relief=SOLID, font=("Times New Roman",15))
        self.enter_username.grid(row=1, column=0, pady=15)
        
        if pass_icon != None:
            self.pass_icon = PhotoImage(file=pass_icon)
            self.passwordlab = Label(self.usernameframe, image=self.pass_icon, text="Password", font="Times 15", compound=LEFT, bg=bg).grid(sticky="w", row=2, column=0, padx=25, pady=15)
        else:
            self.passwordlab = Label(self.usernameframe, text="Password", font="Times 15", bg=bg).grid(sticky="w", row=2, column=0, padx=25, pady=10)
            
        self.enter_password = Entry(self.usernameframe, textvariable=self.password, relief=SOLID, font=("Times New Roman",15))
        self.enter_password.grid(row=3, column=0, pady=10, padx=30)
        
        self.usernameframe.pack(padx=25)
        
        self.login_button = Button(self.login_frame, text="Sign In", font="Times 16",
                                      relief=SUNKEN, bd=3, padx=20, width=14, fg="white", bg="#1976D2").pack(pady=20)
        
        
        # self.f1 = Frame(self.login_frame, bg=bg)
        
        # self.l1 = Label(self.f1, bg="lightgrey", bd=0, width=13).grid(row=0, column=0)
        # self.l2 = Label(self.f1, text="OR", fg="lightgrey", bg=bg, font= ("Times New Roman", 13)).grid(row=0, column=1, padx=3)
        # self.l3 = Label(self.f1, bg="lightgrey", height=0, bd=0, width=13).grid(row=0, column=2)
        
        # self.f1.pack(pady=10)
        
        # self.f2 = Frame(self.login_frame)
        
        
        # self.f2.pack(pady=10)
        
        self.login_frame.place(x=place_x, y=place_y)
        
        
    def signup_ask(self, master=None, width=320, height=60, bg="white", bd=2, relief=RIDGE, place_x=0, place_y=0):
        
        self.ask_signup = Frame(master, bg=bg, bd=bd, relief=relief)
        
        self.ask_label = Label(self.ask_signup, text="Don't have an account?", font=("Times New Roman",13,"bold"), bg=bg).grid(row=0, column=0, pady=15, padx=15)
        self.sign_up_button = Button(self.ask_signup, text="Sign Up", font=("Times New Roman",13,"bold"), bg=bg, fg="#00759E", relief=FLAT, activebackground=bg, activeforeground="#00759E").grid(row=0, column=1, pady=15)
        
        self.ask_signup.place(x=place_x, y=place_y, width=width, height=height)
        

