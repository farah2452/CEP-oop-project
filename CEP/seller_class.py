from tkinter import *
from PIL import Image, ImageTk


class SellerGui(Tk):
    def __init__(self, shopname=" My Shop"):
        super().__init__()
        super().title("seller")
        width = super().winfo_screenwidth()
        height = super().winfo_screenheight()
        super().geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        super().maxsize(width=1366, height=768)
        super().minsize(width=1366, height=768)
        # super().config(background=("#9C27B0"))

        # Label for name of the shop
        self.shop_lab_image = Image.open("shop_label_image.png")
        self.shop_lab_image = self.shop_lab_image.resize((40, 40), Image.ANTIALIAS)
        self.shop_lab_image = ImageTk.PhotoImage(self.shop_lab_image)

        self.main_lab = Label(self, text=shopname, font=("Times", "23", "bold"),
                              bd=4, image=self.shop_lab_image,
                              bg="#CFD8DC", compound=LEFT)
        self.main_lab.pack(fill=X)

        # buttons inside the frame
        self.button_frame = Frame(self, height=150, pady=60, bd=5, bg="#BBDEFB")
        self.button_frame.pack(fill=X)

        # add product image on the button
        self.add_icon_pic = Image.open("add_icon.png")
        self.add_icon_pic = self.add_icon_pic.resize((20, 20), Image.ANTIALIAS)
        self.add_icon_pic = ImageTk.PhotoImage(self.add_icon_pic)

        self.add_product_button = Button(self.button_frame, text="Add product",
                                         padx=13, font=("Times", "18", "bold italic"),
                                         relief=GROOVE, bg="#03A9F4",
                                         fg="white", image=self.add_icon_pic, compound=LEFT)
        self.add_product_button.grid(row=0, column=0, padx=50)

        self.b2 = Button(self.button_frame, text="some button 2",
                         font=("Times", "18", "bold italic"),
                         relief=GROOVE, bg="#03A9F4", fg="white")
        self.b2.grid(row=0, column=1, padx=50)

        self.b3 = Button(self.button_frame, text="some button 3",
                         font=("Times", "18", "bold italic"),
                         relief=GROOVE, bg="#03A9F4", fg="white")
        self.b3.grid(row=0, column=2, padx=50)























        super().mainloop()


s = SellerGui()

