from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from datetime import *

class CustomerHomePage:

    def __init__(self, root=None):
        left_bg = "#FFFFFF"
        self.root = root
        self.root.title("Customer")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        self.root.maxsize(width=width, height=height)
        self.root.minsize(width=width, height=height)
        #self.root.config(background=("#9C27B0"))

        # ========================= =================================
        # Title Frame on the left side
        self.left_frame = Frame(self.root, bg=left_bg)

        self.bluejay_pic = ImageTk.PhotoImage(PIL.Image.open("bird.png").resize((90, 90), PIL.Image.ANTIALIAS))
        self.title_lab = Label(self.left_frame, text="BLUE JAY  ", font=("Goudy Old Style", "29", "bold italic"),
                               bg=left_bg, image=self.bluejay_pic, compound=LEFT)
        self.title_lab.pack(padx=5)

        self.tagline = Label(self.left_frame, text="Where shopping becomes easy! ", font=("Chiller", 22, "bold italic"),
                             fg="#2196F3", bg=left_bg)
        self.tagline.pack(pady=5)

        self.market_lab = Label(self.left_frame, text="Market", font=("Times", "20"), bg=left_bg)
        self.market_lab.pack(anchor=W, pady=18)

        self.left_frame.pack(fill=Y, side=LEFT, pady=1)
        # ========================================   =============================
        # category buttons frame
        self.cat_frame = Frame(self.left_frame, bg=left_bg)

        self.c1 = Button(self.cat_frame, text="Grocery", font=("Times", "15"), bg=left_bg, anchor="w")
        self.c2 = Button(self.cat_frame, text="Fashion", font=("Times", "15"), bg=left_bg, anchor="w")
        self.c3 = Button(self.cat_frame, text="Beauty products",  font=("Times", "15"), bg=left_bg, anchor="w")
        self.c4 = Button(self.cat_frame, text="Computers & Accessories", font=("Times", "15"), bg=left_bg, anchor="w")
        self.c5 = Button(self.cat_frame, text="Home Appliances", font=("Times", "15"), bg=left_bg, anchor="w")

        buttons = (self.c1, self.c2, self.c3, self.c4, self.c5)
        for i in range(5):
            b = buttons[i]
            b.pack(anchor=W, pady=5)

        self.cat_frame.pack(anchor=W)
        # =================================    =================================
        # bottom left pic
        self.left_pic_frame = Frame(self.left_frame)
        self.bottom_pic = ImageTk.PhotoImage(PIL.Image.open("images/category.png").resize((280, 290), PIL.Image.ANTIALIAS))
        self.bottom_pic_lab = Label(self.left_pic_frame, image=self.bottom_pic)
        self.bottom_pic_lab.pack()

        self.left_pic_frame.pack(side=LEFT)

        # =====================================   ===========================================
        self.top_frame = Frame(self.root, bg="#673AB7")
        self.heading_label = Label(self.top_frame, text="Every Item Mall", bg="#673AB7", fg="white",
                                   font=("Times New Roman", "25", "bold")).pack()
        self.top_frame.pack(fill=X, side=TOP)

        # login time details
        self.date_time = datetime.now()
        self.customer_info = ["1", "2", "My name"]
        self.time_details_frame = Frame(self.root, bg="#512DA8", pady=3, padx=125)

        self.user_lab = Label(self.time_details_frame, text=f"Username: {self.customer_info[2]}",
                              bg="#512DA8", fg="white",
                              font=("Times New Roman", 14)).grid(row=0, column=0)

        self.date_label = Label(self.time_details_frame, bg="#512DA8", fg="white",
                                text=f"Date: {self.date_time.day}/{self.date_time.month}/{self.date_time.year}",
                                font=("Times New Roman", 14),).grid(row=0, column=1, padx=125)

        self.time_label = Label(self.time_details_frame, bg="#512DA8", fg="white",
                                text=f"Login Time: {self.date_time.strftime('%I:%M:%S %p')}",
                                font=("Times New Roman", 14)).grid(row=0, column=2, padx=125)

        self.time_details_frame.pack(fill=X)
        # ===============================    =========================================






        # ======================================== ================================
        # self.top_frame = Frame(self.root, bg="black")
        # self.time_lab = Label(self.root, text="Time logins stuff", bg="pink")
        # self.time_lab.pack(fill=X, side=TOP)
        # self.top_frame.pack()

#
# #         ==================  Buttons of categories =====================
#         self.cat_frame = Frame(self.root)
#         self.cat_frame.pack()
#
#         self.c1 = Button(self.cat_frame, text="Grocery", pady=20, width=20, font=("Times", "22", "bold italic"), fg="white",
#                     bg="#9C27B0")
#         self.c2 = Button(self.cat_frame, text="Fashion", pady=20, width=20, font=("Times", "22", "bold italic"), fg="white",
#                     bg="#9C27B0")
#         self.c3 = Button(self.cat_frame, text="Beauty products", command=lambda: self.create_window("Beauty products"), pady=20, width=20, font=("Times", "22", "bold italic"),
#                     fg="white", bg="#9C27B0")
#         self.c4 = Button(self.cat_frame, text="Computers & Accessories", pady=20, width=20, font=("Times", "22", "bold italic"),
#                     fg="white", bg="#9C27B0")
#         self.c5 = Button(self.cat_frame, text="Home Appliances", pady=20, width=20, font=("Times", "22", "bold italic"),
#                     fg="white", bg="#9C27B0")
#
#         buttons = (self.c1, self.c2, self.c3, self.c4, self.c5)
#         for i in range(5):
#             b = buttons[i]
#             b.grid(row=i, column=0, pady=8)
#
#         self.root.mainloop()
#
#     def create_window(self, category):
#         self.root.destroy()
#         self.new_window = Toplevel()
#         self.new_window.title(category)
#         width = self.new_window.winfo_screenwidth()
#         height = self.new_window.winfo_screenheight()
#         self.new_window.geometry(f"{width}x{height}")
#         # super().iconbitmap(icon)
#         self.new_window.maxsize(width=1366, height=768)
#         self.new_window.minsize(width=1366, height=768)
#         self.new_window.config(background=("#9C27B0"))
#         self.new_window.new_window.mainloop()
#
#     def care_product_screen(self):
#         # [["S.No", "Product ID", "Category", "Product Name", "Product Price", "Quantity", "Description"]]
#         # productlist = [[1, "1234", "Beauty products", "eye liner", 350, 100, "for all skin types"],
#         #                [2, "5678", "Beauty products", "blush", 200, 100, "Pink and shiney"]]
#         # productpics = [[]]
#         # self.create_window("Beauty products", productlist, productpics)
#         self.c = CategoryProducts("Beauty products")
#         self.c.mainloop()


# class CategoryProducts(Tk):
#     def __init__(self, category):
#         super().__init__()
#         # def create_window(self, category, productlist, picslist):
#         self.title(category)
#         width = self.winfo_screenwidth()
#         height = self.winfo_screenheight()
#         self.geometry(f"{width}x{height}")
#         # super().iconbitmap(icon)
#         self.maxsize(width=1366, height=768)
#         self.minsize(width=1366, height=768)
#         # super().config(background=("#9C27B0"))
#
#         self.can_frame = Frame(self, bg="black")
#         self.canvas = Canvas(self.can_frame, height=30, width=30)
#         self.canvas.pack()
#
#         lab = Label(self.canvas, text="I am beauty products inside canvassss")
#         lab.pack()
#         self.mainloop()
#




root = Tk()
o = CustomerHomePage(root=root)
root.mainloop()












