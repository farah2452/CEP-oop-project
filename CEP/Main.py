# ************************************** Importing Modules ********************************************

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from signin_class import *
from signup_class import *





class Main(Tk):
    
    def __init__(self, geosize="985x720+250+25", title="My Window", icon="",
                 minsize=(900, 650), maxsize=(900, 650), windowbg="#9C27B0"):
        super().__init__()
        super().title(title)
        super().geometry(geosize)
        #super().iconbitmap(icon)
        super().maxsize(width=minsize[0], height=minsize[1])
        super().minsize(width=maxsize[0], height=maxsize[1])
        super().config(background=(windowbg))

        # title pic
        self.titlepiccan = Canvas(self, width=400, height=650, bg="white")
        self.titlepiccan.pack(side=LEFT)
        self.titlepic = Image.open("phone.png")
        self.titlepic = self.titlepic.resize((400, 500), Image.ANTIALIAS)
        self.titlepic = ImageTk.PhotoImage(self.titlepic)
        self.titlepiccan.create_image(0, 0, anchor="nw", image=self.titlepic)

        # title name and login part
        self.titlelab = Label(self, text="Welcome To\nVirtual shoping Cart",
                       font=("Times", "30", "italic"), bg=windowbg).pack(pady=10)
        
        
        self.options = ("Customer","Seller")
        self.option = StringVar()
        self.frame_option = ttk.Combobox(self, textvar=self.option, values=self.options, font=("goudy old style",13),justify=CENTER,state="readonly")
        self.frame_option.current(0)
        self.frame_option.bind("<<ComboboxSelected>>", self.comboclick)
        self.frame_option.place(x=520, y=115)
        
        
        

        # user icon image in the username frame
        self.sign_in_form = Signin()
        self.sign_in_form.signin_form(self, user_image="login.png", user_icon="user_icon.png", pass_icon="pass_icon.png", place_x=460, place_y=150)
        self.sign_in_form.signup_ask(self, place_x=460, place_y=580)
        
        
    def comboclick(self,event):
        
        self.login_system = self.option.get()
        if self.login_system == "Seller":
            self.usernameframe.destroy()
        
        




if __name__ == '__main__':
    
    Gui = Main()
    Gui.mainloop()
    

