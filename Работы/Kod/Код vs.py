from email.mime import image
from tkinter import ttk
from tkinter import *
import tkinter as tk






class SampleApp(tk. Tk):
    def __init__(self,*arg,**kwargs):
        tk.Tk.__init__(self,*arg,**kwargs)
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in(StartPage, MenuPage,  Shop,  Menejer, BUY):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame

            frame.grid(row=0,column=0,sticky='nsew')

            self.show_frame('StartPage')

    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.controller.title('Welcome to  Al-Burj hotel')
        self.controller.geometry("1280x900")
        self.controller.resizable(0, 0)

        self.controller.iconbitmap('11.ico')


        self.backGroundImage = PhotoImage(file = r'1.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x = 0, y = 0)






        big_lable=tk.Label(self,text='Welcome to Al-Burj hotel', font=('Goudy Stout',25,'bold'),fg='white',bg='#6f304b')
        big_lable.pack(pady=30)

        login_lable=tk.Label(self,text='Entry login', font=('Goudy Stout',15,'bold'), bg='#6f304b', fg='white')
        login_lable.pack(pady=30)

        my_login=tk.StringVar()
        login_entry=tk.Entry(self,textvariable=my_login, font=('Candara',15,'bold'), bg='white', fg='black')
        login_entry.pack(pady=30)

        password_lable=tk.Label(self,text='Entry password', font=('Goudy Stout',15,'bold'),bg='#6f304b',fg='white')
        password_lable.pack(pady=30)

        my_password= tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Candara', 15, 'bold'), bg='white',fg='black')
        password_entry.pack(pady=30)


        def check_password():
            if my_password.get()=='burj' and my_login.get()=='al':
                controller.show_frame('MenuPage')



            else:
                right_lable['text']='Invalid password or login'

        password_button=tk.Button(self,text='Sign in',command=check_password,
                                  font=('Goudy Stout',10,'bold'),bg='#6f304b',fg='white')
        password_button.pack()
        right_lable=tk.Label(self,font=('Goudy Stout',10,'bold'), bg='#6f304b',fg='red')
        right_lable.pack(pady=30)

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,)
        self.controller=controller

        
        self.backGroundImage = PhotoImage(file = r'2.png')
        self.backGroundImageLabel = Label(self, width=0, height=0,  image=self.backGroundImage)
        self.backGroundImageLabel.place(x =40, y = 0)

        big_lable = tk.Label(self, text='Welcome to Al-Burj', font=('Candara', 50, 'bold'), fg='white', bg='#6f304b')
        big_lable.pack(pady=30)
        big_lable.place(x=300, y=40)






        def Menejer():
            controller.show_frame('Menejer')

        contact_button = tk.Button(self, text="Manager", command=(Menejer), font=('Candara', 30, 'bold'), fg='white', bg='#6f304b')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=200)

      
        

        def Shop():
            controller.show_frame('Shop')

        contact_button = tk.Button(self, text="Online-Shop", command=(Shop), font=('Candara', 30, 'bold'), fg='white', bg='#6f304b')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=300)





        def exit():
            controller.show_frame('StartPage')

        i_button = tk.Button(self, text=" Back ",  command=exit, bg="#6f304b",  width = 20,  font=('Candara', 30, 'bold'),  fg="white")
        i_button.pack()
        i_button.place(x = 10, y=400)



        



class Shop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, )
        self.controller = controller

        self.backGroundImage = PhotoImage(file=r'6.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        big_lable = tk.Label(self, text='Rooms Number', font=('Candara', 50, 'bold'), fg='white', bg='#6f304b')
        big_lable.pack(pady=30)


        def nomer():
            result_contact_lable = tk.Checkbutton(self,
                                             text="For Famaly \n Lux \n Mini bar \n Play Zona \n Swimming pool ", font=('Wide Latin', 15, 'bold'), bg='#6f304b',
                                             fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=320, y=250)
            result_contact_lable = tk.Checkbutton(self, 
                                             text="For Lovers \n Lux \n Bar\n Rest zone \n Spa", font=('Wide Latin', 15, 'bold'), bg='#6f304b',
                                             fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=670, y=250)
            result_contact_lable = tk.Checkbutton(self, 
                                             text="For President \n Lux \n Golf zone \n Mini bar \n Spa \n Swimming pool", font=('Wide Latin', 15, 'bold'), bg='#6f304b',
                                             fg='black')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=925, y=250)

        contact_button = tk.Button(self, text="Numbers ", command=(nomer),
                                   font=('Bernard MT condensed', 20, 'bold'), bg='#6f304b', fg='white',
                                   width=20)
        contact_button.pack(pady=25)
        contact_button.place(x=10, y=250)

  

        def BUY():
            controller.show_frame('BUY')

        contact_button = tk.Button(self, text="BUY", command=(BUY), font=('Candara', 25, 'bold'), fg='white', bg='#6f304b')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=350)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 25, 'bold'), fg='white', bg='#6f304b')
        return_button.pack(pady=300)
        return_button.place(x=10, y=450)






class Menejer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, )
        self.controller = controller
        self.backGroundImage = PhotoImage(file=r'5.png')
        self.backGroundImageLabel = Label(self, width=0, height=0, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=40, y=0)
        

        big_lable = tk.Label(self, text='Best Manager', font=('Candara', 50, 'bold'), fg='white', bg='#6f304b')
        big_lable.pack(pady=30)

        def Manager():
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="David", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=350, y=205)
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="Anna", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=730, y=205)

        contact_button = tk.Button(self, text='Manager', command=(Manager),
                                   font=('Bernard MT condensed', 25, 'bold'), bg='#6f304b', fg='white',
                                   width=20)
        contact_button.pack(pady=50)
        contact_button.place(x=10, y=200)

        def Money():
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<per hour 10$>", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=350, y=305)
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<per hour 20$>", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=760, y=305)

        contact_button = tk.Button(self, text= "Services per hour" , command=(Money),
                                   font=('Bernard MT condensed', 25, 'bold'), bg='#6f304b', fg='white',
                                   width=20)
        contact_button.pack(pady=50)
        contact_button.place(x=10, y=300)

        def Timetable():
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<Monday \n Friday>", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=350, y=390)
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<Tuesday \n Saturday>", font=('Wide Latin', 20, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=760, y=390)

        contact_button = tk.Button(self, text= "Timetable " , command=(Timetable),
                                   font=('Bernard MT condensed', 25, 'bold'), bg='#6f304b', fg='white',
                                   width=20)
        contact_button.pack(pady=50)
        contact_button.place(x=10, y=400)

        def Telnomer():
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<+99893333-00-00>", font=('Wide Latin', 13, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=350, y=505)
            result_contact_lable = tk.Button(self, activebackground="#6f304b", activeforeground="white",
                                             text="<+99895656-65-65>", font=('Wide Latin', 13, 'bold'), bg='#6f304b',
                                             fg='white')
            result_contact_lable.pack(pady=50)
            result_contact_lable.place(x=760, y=505)

        contact_button = tk.Button(self, text="Phone nomber ", command=(Telnomer),
                                   font=('Bernard MT condensed', 25, 'bold'), bg='#6f304b', fg='white',
                                   width=20)
        contact_button.pack(pady=50)
        contact_button.place(x=10, y=500)



        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='back', command=return_MenuPage,font=('Candara', 35, 'bold'), fg='white', bg='#6f304b')
        return_button.pack(pady=300)
        return_button.place(x=10, y=600)


    
class BUY(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.backGroundImage=PhotoImage(file=r'5.png')  
        self.backGroundImageLabel=Label(self,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0,y=0)
        self.backGroundImageLabel.place(x =40, y =0)
        self.controller=controller

        def pay():
            totall = float(tot.cget("text"))
            pay = float(e11.get())
            bal = pay - totall
            balText.set(bal)

        def show():

            tot = 0
            if (var1.get()):
                price = int(e1.get())
                qty = int(e6.get())
                tot = int(price * qty)
                tempList = [['товар', e1.get(), e6.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

            if (var2.get()):
                price = int(e2.get())
                qty = int(e7.get())
                tot = int(price * qty)
                tempList = [['Товар2', e2.get(), e7.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

            if (var3.get()):
                price = int(e3.get())
                qty = int(e8.get())
                tot = int(price * qty)
                tempList = [['Товар3', e3.get(), e8.get(), tot]]
                tempList.sort(key=lambda e: e[1], reverse=True)
                for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                    listBox.insert("", "end", values=(item, price, qty, tot))

        

            sum1 = 0.0
            for child in listBox.get_children():
                sum1 += float(listBox.item(child, 'values')[3])
            totText.set(sum1)

        global e1
        global e2
        global e3
        global e4
        global totText
        global balText

        totText = StringVar()
        balText = IntVar()

        Label(self, text="Hotel Al-Burj", font="arial 35 bold", bg="#6f304b").place(x=70, y=10)
        

        var1 = IntVar()
        Checkbutton(self, text="For Famaly=350$", font="arial 15 bold", variable=var1 , bg="#6f304b").place(x=55, y=100)
      

        var2 = IntVar()
        Checkbutton(self, text="For Lovers=150$",font="arial 15 bold", variable=var2, bg="#6f304b").place(x=55, y=150)

        var3 = IntVar()
        Checkbutton(self, text="For President=800$", font="arial 15 bold", variable=var3, bg="#6f304b").place(x=55, y=200)
        Label(self, text="Надо платить:" ,  font="arial 12 bold", bg="#6f304b").place(x=750, y=150)

        Label(self, text="Оплата", font="arial 12 bold", bg="#6f304b").place(x=800, y=100)
        Label(self, text="Баланс", font="arial 12 bold", bg="#6f304b").place(x=800, y=200)

        e1 = Entry(self, font="arial 12 bold", bg="#6f304b")
        e1.place(x=280, y=100)

        e2 = Entry(self , font="arial 12 bold", bg="#6f304b")
        e2.place(x=280, y=150)

        e3 = Entry(self, font="arial 12 bold", bg="#6f304b")
        e3.place(x=280, y=200)

        
        e6 = Entry(self,  font="arial 12 bold",bg="#6f304b")
        e6.place(x=500, y=100)

        e7 = Entry(self, font="arial 12 bold", bg="#6f304b")
        e7.place(x=500, y=150)

        e8 = Entry(self, font="arial 12 bold", bg="#6f304b")
        e8.place(x=500, y=200)

        

        tot = Label(self, text="", font="arial 12 bold", textvariable=totText , bg="#6f304b")
        tot.place(x=900, y=100)

        e11 = Entry(self,font="arial 12 bold", bg="#6f304b")
        e11.place(x=900, y=150)


        e12 = Entry(self ,font="arial 12 bold", bg="#6f304b")

        balance = Label(self, text="", font="arial 22 bold", textvariable=balText, bg="#6f304b").place(x=900, y=200)
        Button(self, text="Счет:", command=show, height=3, width=13, bg="#6f304b").place(x=55, y=300)
        Button(self, text="Оплата", command=pay, height=3, width=13, bg="#6f304b").place(x=650, y=300)

        cols = (' Numbers', ' Price', ' Day', ' Check',)
        listBox = ttk.Treeview(self, columns=cols,  show='headings')

        for col in cols:
            listBox.heading(col,  text=col)
            listBox.pack()
            listBox.place(x=55, y=350)

          
            def return_MenuPage():
             controller.show_frame('Shop')

        return_button = tk.Button(self, text='back', command=return_MenuPage,font=('Candara', 35, 'bold'), fg='black', bg='#6f304b')
        return_button.pack(pady=300)
        return_button.place(x=55, y=600)



if __name__=='__main__':
    app = SampleApp()
    app.mainloop()

