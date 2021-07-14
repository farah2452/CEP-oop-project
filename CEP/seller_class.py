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

        self.buttons_tup = ("Add product", "b2", "b3")
        for button in range(len(self.buttons_tup)):

            self.b = Button(self.button_frame, text=self.buttons_tup[button],
                            width=23, font=("Times", "18", "bold italic"),
                            relief=GROOVE, bg="#03A9F4", fg="white")
            self.b.grid(row=0, column=button, padx=50)























        super().mainloop()


s = SellerGui()

