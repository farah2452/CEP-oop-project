from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
from datetime import *
import os
from csv import *
from filing import *
import pickle
from seller_window_class import *
from tkinter import ttk


class CustomerHomePage(Tk):

    def __init__(self):
        # =========================== Setting up the Screen =======================
        left_bg = "#FFFFFF"
        super().__init__()
        super().title("seller")
        width = super().winfo_screenwidth()
        height = super().winfo_screenheight()
        super().geometry(f"{width}x{height}")
        # super().iconbitmap(icon)
        super().maxsize(width=width, height=height)
        super().minsize(width=width, height=height)
        super().config(background=("white"))


        # ========================= =================================
        # Title Frame on the left side
        self.left_frame = Frame(self, bg=left_bg)

        self.bluejay_pic = ImageTk.PhotoImage(PIL.Image.open("bird.png").resize((90, 90), PIL.Image.ANTIALIAS))
        self.title_lab = Label(self.left_frame, text="BLUE JAY  ", font=("Goudy Old Style", "29", "bold italic"),
                               bg=left_bg, image=self.bluejay_pic, compound=LEFT)
        self.title_lab.pack()

        self.tagline = Label(self.left_frame, text="Where shopping becomes easy!", font=("Chiller", 22, "bold italic"),
                             fg="#2196F3", bg=left_bg)
        self.tagline.pack()

        self.market_lab = Label(self.left_frame, text="Categories", font=("Times", "20", "bold italic"), bg=left_bg)
        self.market_lab.pack(anchor=W, pady=18)

        # ========================================   =============================
        # category buttons frame
        self.cat_frame = Frame(self.left_frame, bg=left_bg)

        self.c1 = Button(self.cat_frame, text="All Categories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c1)
        self.c2 = Button(self.cat_frame, text="Grocery", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c2)
        self.c3 = Button(self.cat_frame, text="Fashion", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c3)
        self.c4 = Button(self.cat_frame, text="Beauty products", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c4)
        self.c5 = Button(self.cat_frame, text="Computers & Accessories", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c5)
        self.c6 = Button(self.cat_frame, text="Home Appliances", font=("Times", "15"), bg=left_bg, anchor="w", width=27, relief=FLAT, command=self.func_c6)

        buttons = (self.c1, self.c2, self.c3, self.c4, self.c5, self.c6)
        for i in range(6):
            b = buttons[i]
            b.pack(anchor=W, pady=2)

        self.cat_frame.pack(anchor=W)
        # =================================    =================================
        # bottom left pic
        self.left_pic_frame = Frame(self.left_frame)
        self.bottom_pic = ImageTk.PhotoImage(PIL.Image.open("images/category.png").resize((290, 260), PIL.Image.ANTIALIAS))
        self.bottom_pic_lab = Label(self.left_pic_frame, image=self.bottom_pic)
        self.bottom_pic_lab.pack()

        self.left_pic_frame.pack(side=LEFT)
        self.left_frame.pack(fill=Y, side=LEFT, pady=1)

        #=============================== The Top Frame  ==================================
        self.top_frame = Frame(self, bg=left_bg)

        # ================================   ==============================

        self.top_frame1 = Frame(self.top_frame, bg=left_bg)
        self.cart_pic = ImageTk.PhotoImage(PIL.Image.open("images/logo1.png").resize((40, 40), PIL.Image.ANTIALIAS))
        self.account_pic = ImageTk.PhotoImage(PIL.Image.open("accountpic.png").resize((40, 40), PIL.Image.ANTIALIAS))

        self.user_info_button = Button(self.top_frame1, text="View Account", bg="#00BCD4", font=("Comic Sans MS", 16),
                                       image=self.account_pic, compound=LEFT, relief=GROOVE)
        self.history_button = Button(self.top_frame1, text="View Shopping History", bg="#F8BBD0",
                                     font=("Comic Sans MS", 16), relief=GROOVE)
        self.seecart_button = Button(self.top_frame1, image=self.cart_pic, bd=0, bg=left_bg)

        # ======================= log out =======================
        #
        # self.checkout_pic = ImageTk.PhotoImage(PIL.Image.open("checkout_pic.jpg").resize((140, 50), PIL.Image.ANTIALIAS))
        # self.checkout_button = Button(self.top_frame1, image=self.checkout_pic, bd=0, bg=left_bg)
        # self.checkout_button.place(x=900, y=0)
        # ======================   =========================
        self.user_info_button.grid(row=0, column=0, padx=35)
        self.history_button.grid(row=0, column=1, padx=35)
        self.seecart_button.grid(row=0, column=3,  padx=250)
        self.top_frame1.pack(fill=X)

        # ==================================      ==========================
        # login time details
        self.top_frame2 = Frame(self.top_frame, bg=left_bg)
        self.date_time = datetime.now()
        self.customer_info = ["1", "2", "My name"]
        self.time_details_frame = Frame(self.top_frame2, bg="#2196F3", pady=3, padx=125)

        self.user_lab = Label(self.time_details_frame, text=f"Username: {self.customer_info[2]}",
                              bg="#2196F3", fg="white",
                              font=("Times New Roman", 14)).grid(row=0, column=0)

        self.date_label = Label(self.time_details_frame, bg="#2196F3", fg="white",
                                text=f"Date: {self.date_time.day}/{self.date_time.month}/{self.date_time.year}",
                                font=("Times New Roman", 14), ).grid(row=0, column=1, padx=125)

        self.time_label = Label(self.time_details_frame, bg="#2196F3", fg="white",
                                text=f"Login Time: {self.date_time.strftime('%I:%M:%S %p')}",
                                font=("Times New Roman", 14)).grid(row=0, column=2, padx=125)

        self.time_details_frame.pack(fill=X)
        
        self.product_pic = ""
        self.categories_list = list(filter(lambda x: x.endswith(".csv"), os.listdir("Categories")))
        
        self.top_frame2.pack(fill=X, pady=3)

        self.top_frame.pack(fill=X)



        # ====================================  =====================================


        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        self.all_products_pic = []
        self.all_catetegories_data = []

        if os.path.isdir("Categories"):
            self.show_product()
    # ==========================   =======================

    def show_product(self, cat=""):
        
        # ---------------------    -------------------------------
        self.categories_list = list(filter(lambda x: x.endswith(".csv"), os.listdir("Categories")))
        if cat != "":
            if os.path.exists(f"Categories/{cat}.csv"):
                cat += ".csv"
                self.categories_list = [cat]
            else:
                self.categories_list = []
        
        
        # ---------------------    -------------------------------
        
        # inside product frame
        self.show_prod_canvas = Canvas(self.products_frame, bg="khaki")
        self.show_prod_canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=70, pady=50)
        
        self.scroll_bar = ttk.Scrollbar(self.products_frame, orient="vertical", command=self.show_prod_canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        
        self.show_prod_canvas.config(yscrollcommand=self.scroll_bar.set)
        self.show_prod_canvas.bind("<Configure>", lambda e: self.show_prod_canvas.configure(scrollregion=self.show_prod_canvas.bbox("all")))
        
        self.in_product_frame = Frame(self.show_prod_canvas, bg="khaki")
        self.show_prod_canvas.create_window((0,0), window=self.in_product_frame, anchor=NW)
        
        # -----------------------  ------------------------------
        self.all_products_pic = []
        self.all_catetegories_data = []    
        for i in self.categories_list:
            self.category_data = Filing.file_read(dir_name="Categories", file_name=i[:-4])
            for j in self.category_data[1:]:
                self.all_catetegories_data.append(j[1:])    # product : [id, name, shop name, price, quantity, description]

        for i in range(len(self.all_catetegories_data)):
            self.product_pic = ""
            if os.path.isdir("Product Pics"):
                if os.path.exists(f"Product Pics/{self.all_catetegories_data[i][0]}.pkl"):
                    self.product_pic = Filing.pic_file_read(dir_name="Product Pics",
                                                            file_name=self.all_catetegories_data[i][0])

                    self.product_pic = PIL.Image.open(self.product_pic)
                    self.product_pic = self.product_pic.resize((120, 120), PIL.Image.ANTIALIAS)
                    self.product_pic = ImageTk.PhotoImage(self.product_pic)

            if self.product_pic == "":
                self.product_pic = "addpic.png"
                self.product_pic = ImageTk.PhotoImage(PIL.Image.open(self.product_pic).resize((120, 120), PIL.Image.ANTIALIAS))

            self.all_products_pic.append(self.product_pic)

            if i % 2 == 0:
                self.product_button = Button(self.in_product_frame, image=self.all_products_pic[i],
                                             text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                             font=("Times", 16, "bold"), bg="khaki", justify=LEFT, anchor=W, padx=1, pady=8,
                                             compound=TOP, relief=FLAT, bd=2,
                                             command=self.prod_details)
                self.product_button.grid(row=int(i / 2), column=0, padx=23, pady=15, sticky=W)
                self.product_button.config(image=self.all_products_pic[i])
            else:
                self.product_button = Button(self.in_product_frame, image=self.all_products_pic[i],
                                             text=f"{self.all_catetegories_data[i][1]}\n{self.all_catetegories_data[i][2]}\nRs.{self.all_catetegories_data[i][3]}",
                                             font=("Times", 16, "bold"), justify=LEFT, anchor=W, padx=1, pady=8,
                                             compound=TOP, relief=FLAT, bd=2, bg="khaki",
                                             command=self.prod_details)
                self.product_button.grid(row=int(i / 2), column=1, padx=23, pady=15, sticky=W)
                self.product_button.config(image=self.all_products_pic[i])

        # =============================     =====================================
    def func_c1(self):
        """The function for all categories to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)

        self.show_product()

    def func_c2(self):
        """The function for grocery to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Grocery.csv"):
            self.show_product(cat="Grocery")
        else:
            self.show_product(cat=" ")

    def func_c3(self):
        """The function for fashion to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Fashion.csv"):
            self.show_product(cat="Fashion")
        else:
            self.show_product(cat=" ")

    def func_c4(self):
        """The function for beauty products to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Beauty Products.csv"):
            self.show_product(cat="Beauty Products")
        else:
            self.show_product(cat=" ")

    def func_c5(self):
        """The function for computer & Accessories to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Computers & Accessories.csv"):
            self.show_product(cat="Computers & Accessories")
        else:
            self.show_product(cat=" ")

    def func_c6(self):
        """The function for home appliances to show up"""
        self.products_frame.destroy()

        self.products_frame = Frame(self, bg="white")
        self.products_frame.pack(fill=BOTH, expand=1)
        if os.path.exists("Categories/Home Appliances.csv"):
            self.show_product(cat="Home Appliances")
        else:
            self.show_product(cat=" ")



        # ==================================    =========================================
    def prod_details(self):
        root = Toplevel(self)
        self.product_detail = ProductInfo(self, product_info=self.all_catetegories_data[0])
        root.mainloop()



        # Canvas for category products to show up

        # ==========================    ==================================


class ProductInfo:

    def __init__(self, root=None, title="", max_width=800, max_height=500, c_width=100, c_height=50, icon=None,
                 windowbg="#FFFFFF", product_info=[], seller_info=[], product_pic=None):
        # =============================================    ===============================

        self = root
        self.title(title)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self))

        self.geometry(f"{max_width}x{max_height}+{c_width}+{c_height}")
        self.maxsize(max_width, max_height)
        self.minsize(max_width, max_height)

        if icon != None:
            self.iconbitmap(icon)
        self.config(bg=windowbg)

        # ========================================    ======================================

        self.seller_info = seller_info
        self.product_info = product_info
        self.select_quant = StringVar()

        # ============================================    ================================

        self.heading = Label(self, text="Product Detail", font=("Times", 20, "bold"), bg="lightgrey").pack(
            side=TOP, fill=X)

        # ===========================================     =================================

        self.pic_prod_frame = Frame(self, bg=windowbg, pady=3)
        self.pic_prod_frame.pack(pady=17, padx=10, anchor=NW, fill=X)

        # -----------------------------    -------------------------------

        self.pic_canvas = Canvas(self.pic_prod_frame, width=230, height=200, bg=windowbg)
        self.pic_canvas.pack(side=LEFT, anchor=NW, padx=7)
        self.pic_canvas.create_image(0, 0, image=product_pic)

        # ------------------------------    ---------------------------------------

        self.pic_des_frame = Frame(self.pic_prod_frame, pady=5, padx=5, width=50, height=50, bg=windowbg)

        self.prod_name_label = Label(self.pic_des_frame, text=f"{self.product_info[1]}", font="Times 15",
                                     wraplength=520, anchor=NW, justify=LEFT, bg=windowbg).pack(anchor=W)
        self.prod_price_lab = Label(self.pic_des_frame, text=f"Rs.{self.product_info[3]}", font="Times 15 bold",
                                    fg="dark orange", bg=windowbg).pack(pady=15, anchor=W)

        ####################################    #########################################

        self.quant_frame = Frame(self.pic_des_frame, pady=3, bg=windowbg)
        self.quant_label = Label(self.quant_frame, text="Quantity:", font="Times 15", bg=windowbg).grid(row=0, column=0)
        self.quant_select = Spinbox(self.quant_frame, from_=1, to=int(self.product_info[-2]), font="Times 12",
                                    textvariable=self.select_quant, state="readonly", readonlybackground="white",
                                    selectbackground="white", selectforeground="black").grid(row=0, column=1, padx=30)
        self.quant_frame.pack(anchor=W, fill=X)

        self.pic_des_frame.pack(fill=X, anchor=NW, padx=7)

        # ----------------------------------    ---------------------------------------

        self.add_cart_button = Button(self.pic_des_frame, text="Add to Cart", font="Times 15", width=15, relief=FLAT,
                                      bg="DarkOrange1").pack(pady=12)

        # ======================================    =======================================

        self.prod_des_frame = Frame(pady=3, padx=5, bg=windowbg)

        self.prod_head_lab = Label(self.prod_des_frame, text=f"Product Details of {self.product_info[1]}",
                                   font="Times 15 bold", anchor=NW, justify=LEFT, bg=windowbg).pack(fill=X, pady=5,
                                                                                                    anchor=NW)
        self.prod_desc = Label(self.prod_des_frame, text=f"{self.product_info[-1]}", font="Times 13", anchor=NW,
                               justify=LEFT, wraplength=720, bg=windowbg).pack(pady=5, anchor=W, fill=X)

        self.prod_des_frame.pack(pady=20, fill=BOTH, padx=10, anchor=NW, side=LEFT)


if __name__ == '__main__':
    o = CustomerHomePage()
    o.mainloop()












