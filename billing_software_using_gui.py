from tkinter import *
import random,os
from tkinter import messagebox
class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("Billing Software")
        title=Label(self.root,text="Billing Software",font=("calibri",30,"bold"),pady=2,bg="navy",bd=12,relief=GROOVE,fg="white").pack(fill=X)

        #variables
        #Cosmetics
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.Lotion=IntVar()

        #grocery

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #cold drinks

        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbps_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #total product price
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price=StringVar()

        #tax variable

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #customer details

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




        f1=LabelFrame(self.root,text="Customer Details ",font=("calibri",15,"bold"),pady=2,bg="navy",bd=12,relief=GROOVE,fg="white")
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer Name",font=("calibri",15,"bold")).grid(row=0,column=1,padx=20,pady=5)
        cname_txt=Entry(f1,width=15,textvariable=self.c_name,font="arial,15").place(x=170,y=7)

        cphone_lbl = Label(f1, text="Customer Phone No.", font=("calibri", 15, "bold")).place(x=370,y=7)
        cphone_txt = Entry(f1, width=15,textvariable=self.c_phone, font="arial,15").place(x=570, y=7)

        bill_no_lbl = Label(f1, text="Bill No.", font=("calibri", 15, "bold")).place(x=770,y=7)
        bill_no_txt = Entry(f1, width=15,textvariable=self.search_bill, font="arial,15").place(x=850, y=7)

        bill_btn=Button(f1,text="search",command=self.find_bill,width=7,bd=5,font="arialo 12 bold").place(x=1050,y=7)

        #cosmetics
        f2 = LabelFrame(self.root, text="Cosmetics ", font=("calibri", 15, "bold"), pady=2, bg="navy", bd=12,
                        relief=GROOVE, fg="white")
        f2.place(x=5, y=180,width=325,height=380)

        bath_soap_lbl=Label(f2,text="Bath Soap",font=("calibri", 15, "bold"), bg="navy", bd=5,
                        relief=GROOVE, fg="white").place(x=5,y=10)
        bath_soap_txt = Entry(f2, width=10, textvariable=self.soap,font="arial,15").place(x=170, y=12)

        face_cream_lbl = Label(f2, text="Face Cream", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=60)
        face_cream_txt = Entry(f2, width=10,textvariable=self.face_cream, font="arial,15").place(x=170, y=62)

        face_wash_lbl = Label(f2, text="Face Wash", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=110)
        face_wash_txt = Entry(f2, width=10,textvariable=self.face_wash, font="arial,15").place(x=170, y=112)

        hair_spray_lbl = Label(f2, text="Hair Spray", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=160)
        hair_spray_txt = Entry(f2, width=10,textvariable=self.spray, font="arial,15").place(x=170, y=162)

        hair_gel_lbl = Label(f2, text="Hair Gel", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=210)
        hair_gel_txt = Entry(f2, width=10,textvariable=self.gell, font="arial,15").place(x=170, y=212)

        body_Lotion_lbl = Label(f2, text="Body Lotion", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=260)
        body_Lotion_txt = Entry(f2, width=10,textvariable=self.Lotion, font="arial,15").place(x=170, y=262)


        # grocery frame
        f3 = LabelFrame(self.root, text="Grocery", font=("calibri", 15, "bold"), pady=2, bg="navy", bd=12,
                        relief=GROOVE, fg="white")
        f3.place(x=330, y=180, width=325, height=380)

        rice_lbl = Label(f3, text="Rice", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=10)
        rice_txt = Entry(f3, width=10,textvariable=self.rice, font="arial,15").place(x=170, y=12)

        food_oil_lbl = Label(f3, text="Food Oil", font=("calibri", 15, "bold"), bg="navy", bd=5,
                              relief=GROOVE, fg="white").place(x=5, y=60)
        food_oil_txt = Entry(f3, width=10,textvariable=self.food_oil, font="arial,15").place(x=170, y=62)

        daal_lbl = Label(f3, text="Daal", font=("calibri", 15, "bold"), bg="navy", bd=5,
                                relief=GROOVE, fg="white").place(x=5, y=110)
        daal_txt = Entry(f3, width=10,textvariable=self.daal, font="arial,15").place(x=170, y=112)

        wheat_lbl = Label(f3, text="Wheat", font=("calibri", 15, "bold"), bg="navy", bd=5,
                          relief=GROOVE, fg="white").place(x=5, y=160)
        wheat_txt = Entry(f3, width=10,textvariable=self.wheat, font="arial,15").place(x=170, y=162)

        sugar_lbl = Label(f3, text="Sugar", font=("calibri", 15, "bold"), bg="navy", bd=5,
                             relief=GROOVE, fg="white").place(x=5, y=210)
        sugar_txt = Entry(f3, width=10,textvariable=self.sugar, font="arial,15").place(x=170, y=212)

        tea_lbl = Label(f3, text="Tea", font=("calibri", 15, "bold"), bg="navy", bd=5,
                                relief=GROOVE, fg="white").place(x=5, y=260)
        tea_txt = Entry(f3, width=10,textvariable=self.tea, font="arial,15").place(x=170, y=262)

        #cold drinks

        f4 = LabelFrame(self.root, text="Cold Drinks", font=("calibri", 15, "bold"), pady=2, bg="navy", bd=12,
                        relief=GROOVE, fg="white")
        f4.place(x=655, y=180, width=325, height=380)

        maza_lbl = Label(f4, text="Maza", font=("calibri", 15, "bold"), bg="navy", bd=5,
                         relief=GROOVE, fg="white").place(x=5, y=10)
        maza_txt = Entry(f4, width=10,textvariable=self.maza, font="arial,15").place(x=170, y=12)

        coke_lbl = Label(f4, text="Coke", font=("calibri", 15, "bold"), bg="navy", bd=5,
                             relief=GROOVE, fg="white").place(x=5, y=60)
        coke_txt = Entry(f4, width=10,textvariable=self.coke, font="arial,15").place(x=170, y=62)

        frooti_lbl = Label(f4, text="Frooti", font=("calibri", 15, "bold"), bg="navy", bd=5,
                         relief=GROOVE, fg="white").place(x=5, y=110)
        frooti_txt = Entry(f4, width=10,textvariable=self.frooti, font="arial,15").place(x=170, y=112)

        thumbs_up_lbl = Label(f4, text="Thumbs Up", font=("calibri", 15, "bold"), bg="navy", bd=5,
                          relief=GROOVE, fg="white").place(x=5, y=160)
        thumbs_up_txt = Entry(f4, width=10,textvariable=self.thumbps_up, font="arial,15").place(x=170, y=162)

        limca_lbl = Label(f4, text="Limca", font=("calibri", 15, "bold"), bg="navy", bd=5,
                          relief=GROOVE, fg="white").place(x=5, y=210)
        limca_txt = Entry(f4, width=10,textvariable=self.limca, font="arial,15").place(x=170, y=212)

        sprite_lbl = Label(f4, text="Sprite", font=("calibri", 15, "bold"), bg="navy", bd=5,
                        relief=GROOVE, fg="white").place(x=5, y=260)
        sprite_txt = Entry(f4, width=10,textvariable=self.sprite, font="arial,15").place(x=170, y=262)

        #bill fram
        f5 = LabelFrame(self.root, text="Bill Area",font=("calibri",15,"bold"))
        f5.place(x=990, y=180, width=280, height=380)

        scroll_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        m1_lbl=Label(self.root,text="total Cosmetics price",font=("calibri",15,"bold"))
        m1_lbl.place(x=0,y=560)
        m1_txt=Entry(self.root,width=18,font="arial 10 bold",textvariable=self.cosmetic_price,borderwidth=3,relief="solid").place(x=180,y=560)

        m2_lbl = Label(self.root, text="total grocery price", font=("calibri", 15, "bold"))
        m2_lbl.place(x=0, y=590)
        m2_txt = Entry(self.root, width=18, font="arial 10 bold",textvariable=self.grocery_price, borderwidth=3, relief="solid").place(x=180, y=590)

        m3_lbl = Label(self.root, text="total Cold drink price", font=("calibri", 15, "bold"))
        m3_lbl.place(x=0, y=620)
        m3_txt = Entry(self.root, width=18, font="arial 10 bold",textvariable=self.cold_drink_price, borderwidth=3, relief="solid").place(x=190, y=620)

        #tax labels

        c1_lbl = Label(self.root, text=" Cosmetics tax", font=("calibri", 15, "bold"))
        c1_lbl.place(x=400, y=560)
        c1_txt = Entry(self.root, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", borderwidth=3, relief="solid").place(x=550, y=560)

        c2_lbl = Label(self.root, text="grocery tax", font=("calibri", 15, "bold"))
        c2_lbl.place(x=400, y=590)
        c2_txt = Entry(self.root, width=18, font="arial 10 bold",textvariable=self.grocery_tax, borderwidth=3, relief="solid").place(x=550, y=590)

        c3_lbl = Label(self.root, text="Cold drink tax", font=("calibri", 15, "bold"))
        c3_lbl.place(x=400, y=620)
        c3_txt = Entry(self.root, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, borderwidth=3, relief="solid").place(x=550, y=620)

        #buttons
        total_btn=Button(self.root,text="Total",command=self.total,bg="red",fg="black",width=10).place(x=800,y=570)
        gbill_btn = Button(self.root, text="generate Bill",command=self.bill_area, bg="red", fg="black", width=10).place(x=900, y=570)
        clear_btn = Button(self.root, text="clear",command=self.clear_bill, bg="red", fg="black", width=10).place(x=1000, y=570)
        exit_btn = Button(self.root, text="Exit",command=self.exit_app, bg="red", fg="black", width=10).place(x=1100, y=570)

        self.welcome_bill()



    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get() * 120
        self.c_fw_p=self.face_wash.get() * 60
        self.c_hs_p=self.spray.get() * 180
        self.c_hg_p=self.gell.get() * 140
        self.c_bl_p=self.loshan.get() * 180
        self.total_cosmetic_price=  float(  self.c_s_p+
                                            self.c_fc_p+
                                     self.c_fw_p +
                                      self.c_hs_p +
                                      self.c_hg_p +
                                            self.c_bl_p
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get() * 80
        self.g_f_p=self.food_oil.get() * 180
        self.g_d_p=self.daal.get() * 60
        self.g_w_p=self.wheat.get() * 240
        self.g_s_p=self.sugar.get() * 45
        self.g_t_p=self.tea.get() * 150

        self.total_grocery_price = float( self.g_r_p +
                                          self.g_f_p +
                                          self.g_d_p +
                                          self.g_w_p +
                                          self.g_s_p +
                                          self.g_t_p
                                          )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))


        self.d_m_p=self.maza.get() * 60
        self.d_c_p=self.coke.get() * 60
        self.d_f_p=self.frooti.get() * 50
        self.d_t_p=self.thumbps_up.get() * 40
        self.d_l_p=self.limca.get() * 40
        self.d_s_p=self.sprite.get() * 60

        self.total_cold_drink_price = float( self.d_m_p +
                                             self.d_c_p +
                                             self.d_f_p +
                                             self.d_t_p +
                                             self.d_l_p +
                                             self.d_s_p
                                          )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.cd_tax))

        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to retail")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number :{self.c_phone.get()}")
        self.txtarea.insert(END, "\n*******************************")
        self.txtarea.insert(END,"\n Products\t\tQty\tPrice")
        self.txtarea.insert(END, "\n*******************************")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Custumer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0" :
            messagebox.showerror("Error","No product purchased")
        else:
          self.welcome_bill()
          if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
          if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
          if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
          if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Spray\t\t{self.spray.get()}\t{self.c_hs_p}")
          if self.gell.get()!=0:
            self.txtarea.insert(END,f"\n Hair gell\t\t{self.gell.get()}\t{self.c_hg_p}")
          if self.loshan.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t{self.loshan.get()}\t{self.c_bl_p}")

          if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")
          if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_f_p}")
          if self.daal.get()!=0:
            self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t{self.g_d_p}")
          if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t{self.g_w_p}")
          if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.g_s_p}")
          if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t{self.g_t_p}")

          if self.maza.get()!=0:
            self.txtarea.insert(END,f"\n Maaza\t\t{self.maza.get()}\t{self.d_m_p}")
          if self.coke.get()!=0:
            self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t{self.d_c_p}")
          if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n Frooti\t\t{self.face_wash.get()}\t{self.d_f_p}")
          if self.thumbps_up.get()!=0:
            self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbps_up.get()}\t{self.d_t_p}")
          if self.limca.get()!=0:
            self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.d_l_p}")
          if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t{self.d_s_p}")
          self.txtarea.insert(END, "\n-------------------------------")
          if self.grocery_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END, f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
          if self.cosmetic_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END, f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
          if self.cold_drink_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END, f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")

          self.txtarea.insert(END, f"\n Total Bill\t\t Rs. {self.total_bill}")
          self.txtarea.insert(END, "\n-------------------------------")
          self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("d:/bills/"+str(self.bill_no.get())+" .txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill No.  :{self.bill_no.get()}saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("d:/bills/"):
            print(i)
            if i.split(' .')[0]==self.search_bill.get():

                f1=open(f"d:/bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"

        if present=="no":
            messagebox.showerror("Error","invalid bill no")

    def clear_bill(self):
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.Lotion.set(0)

        # grocery

        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        # cold drinks

        self.maza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.thumbps_up.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        # total product price
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        # tax variable

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        # customer details

        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj=Bill(root)
root.mainloop()
