from tkinter import *
from PIL import Image, ImageTk


class Login_gui(Tk):
    def __init__(self, geosize="985x720+250+40", title="My Window", icon="",
                 minsize=(850, 600), maxsize=(850, 600), windowbg="#9C27B0"):
        super().__init__()
        super().title(title)
        super().geometry(geosize)
        super().iconbitmap(icon)
        super().maxsize(width=minsize[0], height=minsize[1])
        super().minsize(width=maxsize[0], height=maxsize[1])
        super().config(background=(windowbg))

        # title pic
        self.titlepiccan = Canvas(self, width=350, height=600)
        self.titlepiccan.pack(side=LEFT)
        self.titlepic = Image.open("t2.png")
        self.titlepic = self.titlepic.resize((360, 600), Image.ANTIALIAS)
        self.titlepic = ImageTk.PhotoImage(self.titlepic)
        self.titlepiccan.create_image(0, 0, anchor=NW, image=self.titlepic)

        # title name and login part
        self.titlelab = Label(self, text="Welcome To\nVirtual shoping Cart",
                       font=("Times", "30", "italic"), bg=windowbg).pack(pady=25)

        # user icon image in the username frame
        self.usernameframe = Frame(self, bg=windowbg)  # frame for username & password
        self.usericon = ImageTk.PhotoImage(Image.open("usericon.png").resize((90, 90), Image.ANTIALIAS))
        self.usericonlab = Label(self.usernameframe, image=self.usericon).grid(columnspan=4, pady=35)

        self.username = StringVar()
        self.password = StringVar()

        self.usernamelab = Label(self.usernameframe, text="Username", font="Times 15", bg=windowbg).grid(row=1, column=1, padx=25)
        self.enterusername = Entry(self.usernameframe, textvariable=self.username, relief=SOLID).grid(row=1, column=2, padx=25)
        self.passwordlab = Label(self.usernameframe, text="Password", font="Times 15", bg=windowbg).grid(row=2, column=1)
        self.enterpassword = Entry(self.usernameframe, textvariable=self.password, relief=SOLID).grid(row=2, column=2)
        self.usernameframe.place(x=450, y=130)

root = Login_gui()

root.mainloop()

