self.top_frame = Frame(self, bg="#483d8b")
self.heading_label = Label(self.top_frame, text="Every Item Mall", bg="#483d8b", fg="white", font=("Times New Roman", "35", "bold")).pack()
self.top_frame.pack(fill=X, side=TOP)

# ===============================    =====================================================

self.time_details_frame = Frame(self, bg="#090149", pady=3, padx=125)

self.user_lab = Label(self.time_details_frame, text=f"Username: {self.customer_info[2]}", fg="white", bg="#090149").grid(row=0, column=0, padx=125)
self.date_label = Label(self.time_details_frame, text=f"Date: {self.date_time.day}/{self.date_time.month}/{self.date_time.year}", fg="white", bg="#090149").grid(row=0, column=1, padx=125)
self.time_label = Label(self.time_details_frame, text=f"Login Time: {self.date_time.strftime('%I:%M:%S %p')}", fg="white", bg="#090149").grid(row=0, column=2, padx=125)

self.time_details_frame.pack(fill=X)