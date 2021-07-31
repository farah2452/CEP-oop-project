from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class SellerInfo:
    
    def __init__(self, root=None, title="User", max_width=1100, max_height=600, seller_info=[]):
        
        # ================================= Setting Screen =============================================
        
        self.root = root
        self.root.title(f"{title} - Edit Info")
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.center_width = int((self.screen_width/2) - (max_width/2))
        self.center_height = int((self.screen_height/2) - (max_height/2))
        
        self.root.geometry(f"{max_width}x{max_height}+{self.center_width}+{self.center_height}")
        self.root.maxsize(max_width, max_height)
        self.root.minsize(max_width, max_height)
        self.root.configure(bg="#FFFFFF")
        # ======================================= Heading ================================================= 
        # heading pic
        edit_pic = ImageTk.PhotoImage(Image.open("edit_icon_pic.png").resize((32, 32), Image.ANTIALIAS))

        self.l1 = Label(self.root, text="  Edit Account Info", image=edit_pic, compound=LEFT, font=("Times New Roman", 20, "bold"), bg="light grey").pack(fill=X)

        # ====================================== Assigning Variables ======================================
        
        self.seller_name = StringVar()
        self.seller_username = StringVar()
        self.seller_email = StringVar()
        self.seller_password = StringVar()
        self.seller_shopname = StringVar()
        self.seller_age = StringVar()
        self.seller_dob = StringVar()
        self.seller_contact = StringVar()
        self.seller_gender = StringVar()
        
        
        # self.seller_name.set(f"{seller_info[0]}")
        # self.seller_username.set(f"{seller_info[2]}")
        # self.seller_shopname.set(f"{seller_info[1]}")
        # self.seller_email.set(f"{seller_info[3]}")
        # self.seller_password.set(f"{seller_info[4]}")
        #
        
        
        # ====================================== Fields Name ==========================================
        
        # seller list is like [name, mall name, username, email, password]
        self.fields_frame = Frame(self.root, bd=3, relief=GROOVE)
        
        # Setting Entry Labels
        seller_info_lab = ("Name", "Gender", "Age", "Shop Name", "Contact No.", "D.O.B", "Username", "Email", "Password", "Address")
        for i in range(3):
            for j in range(3):
                self.seller_info_entry_lab = Label(self.fields_frame, text=f"{seller_info_lab[3 * i + j]}", font="Times 16").grid(row=i, column=2 * j, padx=20, pady=15)
                    
        self.seller_info_entry_lab = Label(self.fields_frame, text=f"{seller_info_lab[-1]}", font="Times 16").grid(row=3, column=0, padx=8, pady=15, sticky=N)
        
        # ------------------------ Setting Entries ----------------------
        seller_entry_var = (self.seller_name, self.seller_age, self.seller_username, self.seller_email, self.seller_password, self.seller_shopname, self.seller_contact, self.seller_dob)
        
        for i in range(3):
            self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[2 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=2, column=2 * i + 1, padx=8, pady=15)
            if i != 0:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[-3 + i], font="Times 16", width=15).grid(row=1, column=2 * i + 1, padx=8, pady=15)
            else:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[-3 + i], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=1, column=2 * i + 1, padx=8, pady=15)
            if i == 0:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[0], font="Times 16", width=15, state=DISABLED, disabledbackground="white", disabledforeground="black").grid(row=0, column=2 * i + 1, padx=8, pady=15)
            elif i == 2:
                self.seller_info_entry = Entry(self.fields_frame, relief=RIDGE, textvariable=seller_entry_var[1], font="Times 16", width=15).grid(row=0, column=2 * i + 1, padx=8, pady=15)
            
        # Creating Combobox for gender
        self.gender_sel = ttk.Combobox(self.fields_frame, textvar=self.seller_gender, values=("Male", "Female"), font="Times 12", justify=CENTER, state="readonly")
        self.gender_sel.grid(row=0, column=3, padx=8, pady=15)
        self.seller_gender.set("Male")
        
        # Textbox for Address
        self.seller_address_info = Text(self.fields_frame, width=80, height=7, relief=RIDGE, bd=3)
        self.seller_address_info.grid(row=3, column=1, sticky=W, pady=15, columnspan=8)
        
        
        
        self.fields_frame.pack(pady=55, padx=10)
        
        # =================================== Save Button =============================
        
        self.save_seller_info_button = Button(self.root, text="Save changes", font=("Times", "20"), fg="white",  padx=20, width=10, bg="#FF4081", pady=5).pack(pady=10)
        # self.save_seller_info_button = Button(self.root, text="Save Info", font="Times 15", width=11, command=self.save_seller_info).pack(pady=10)

        
    # def save_seller_info(self):
    #
    #     self.nam = self.seller_name.get()
    #     self.user = self.seller_username.get()
    #     self.mail = self.seller_email.get()
    #     self.passw = self.seller_password.get()
    #     self.shop_name = self.seller_shopname.get()
    #     self.age = self.seller_age.get()
    #     self.dob = self.seller_dob.get()
    #     self.cont = self.seller_contact.get()
    #     self.gender = self.seller_gender.get()
    #     self.address = self.seller_address_info.get(1.0, END)[:-1]
    #
    #
    #     if os.path.exists("Accounts Info/Seller Accounts.csv"):
    #
    #         self.all_seller_data = Filing.file_read(dir_name="Accounts Info", file_name="Seller Accounts")
    #         self.all_seller_data = self.all_seller_data[1:]
    #         self.seller_data = []
    #
    #         for sell_dat in self.all_seller_data:
    #             if (sell_dat[7] == self.user and sell_dat[9] == self.passw) or (sell_dat[8] == self.user and sell_dat[9] == self.passw):
    #                 self.seller_data = sell_dat
    #
    #         print(self.seller_data)
    #
    #         if len(self.seller_data) != 0:
    #
    #             self.all_seller_data.remove(self.seller_data)
    #
    #             self.seller_data_all = []
    #             for i in self.all_seller_data:
    #                 self.seller_data_all.append(i[1:])
    #             print(self.all_seller_data)
    #
    #             self.seller_data_all.append([self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address])
    #             print(self.all_seller_data)
    #
    #             for i in self.seller_data_all:
    #                 for j in range(1,len(i)+len(i)-2,2):
    #                     i.insert(j, " ")
    #             print(self.seller_data_all)
    #
    #             with open("Accounts Info/Seller Accounts.csv", "w+", newline="") as f:
    #                 write = writer(f)
    #                 write.writerow(["S.No", " ", "Name", " ", "Gender", " ", "Age", " ", "Date of Birth", " ", "Shop Name", " ", "Contact No.", " ", "Username", " ", "Email", " ", "Password", " ", "Address"])
    #                 write.writerow([])
    #                 for i in range(1, len(self.seller_data_all)+1):
    #                     write.writerow([str(i), " "]+self.seller_data_all[i-1])
    #
    #         else:
    #             self.seller_info_file = Filing("Accounts Info")
    #             self.seller_info_file.general_filing(file_name="Seller Accounts", data_list=[self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address], col_list=["Name", "Gender", "Age", "Date of Birth", "Shop Name", "Contact No.", "Username", "Email", "Password", "Address"])
    #
    #     else:
    #         self.seller_info_file = Filing("Accounts Info")
    #         self.seller_info_file.general_filing(file_name="Seller Accounts", data_list=[self.nam, self.gender, self.age, self.dob, self.shop_name, self.cont, self.user, self.mail, self.passw, self.address], col_list=["Name", "Gender", "Age", "Date of Birth", "Shop Name", "Contact No.", "Username", "Email", "Password", "Address"])
        root.mainloop()



r = Tk()
s = SellerInfo(r)

r.mainloop()