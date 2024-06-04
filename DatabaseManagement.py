import customtkinter as ctk
import mysql.connector as Myconn
from tkinter import *
from tkinter import messagebox

# Colors
color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'

userr = ""
passw = ""

def login_details(username, password):
    global userr, passw
    userr = username
    passw = password

def details(user, pass2, app):
    global userr, passw
    userr = user
    passw = pass2
    try:
        # Attempt to connect to MySQL to verify credentials
        Mydb = Myconn.connect(
            host='localhost',
            user=userr,
            password=passw,
            auth_plugin="mysql_native_password"
        )
        Mydb.close()
        app.destroy()
    except Myconn.Error as e:
        messagebox.showerror("Error", f"Failed to login: {e}")

def log():
    # Selecting GUI theme - dark, light, system (for system default)
    ctk.set_appearance_mode("dark")

    # Selecting color theme - blue, green, dark-blue
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Log-In Page")

    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    label = ctk.CTkLabel(master=frame, text='Enter MySQL Username And Password')
    label.pack(pady=12, padx=10)

    user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
    user_entry.pack(pady=12, padx=10)

    user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    user_pass.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Login', command=lambda: details(user_entry.get(), user_pass.get(), app))
    button.pack(pady=12, padx=10)

    checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=12, padx=10)

    app.mainloop()

try:
    log()
    root = Tk()
    root.geometry('1222x700')
    root.configure(bg="#4A4A4A")

    database = StringVar()
    info = StringVar()
    var2 = StringVar()
    datab = StringVar()
    varnames=[]
    datat2 = ''
    dname = ''
    cn = ''
    e1 = ''
    list = []
    count = 0
    string = []
    b = 0
    qr = ""
    dename = StringVar()

    def column_name():
        try:
            global count
            global b
            global datab
            global datat2
            global cn
            global varnames
            
            Mydb=Myconn.connect(host='Localhost',
                            user=userr,
                            password=passw,
                            auth_plugin="mysql_native_password",
                            database=datab)
            cursor=Mydb.cursor()
            cursor.execute("desc "+datat2)
            cn=cursor.fetchall()
            a=20
            j=0
            varnames.clear()
            f5=Frame(root,height=40,width=800,bg="#4A4A4A")
            for i in cn:
                l1=Label(f5,text=i[0],font=("Arial",20),fg="Yellow",bg="#4A4A4A").place(x=a,y=b)
                a=a+170
                count=count+1
                varnames.append("var"+str(j))
                j=j+1
            stringvar()
            
            f5.pack_propagate()
            f5.place(x=580,y=0)
            Mydb.commit()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to retrieve column names: {e}")

    def stringvar():
        global string, varnames
        string.clear()
        for _ in varnames:
            string.append(StringVar())

    def convertor(tup):
        return ''.join(tup)

    database1 = Listbox(root, height=20, width=20, activestyle='dotbox', font="Helvetica", fg="Yellow", bg="#4A4A4A")
    database1.grid(row=1, column=0, padx=10, pady=10)

    def ShowDatabase():
        try:
            global userr, passw
            Mydb = Myconn.connect(
                host='localhost',
                user=userr,  # Use .get() to retrieve the string value from StringVar
                password=passw,  # Use .get() to retrieve the string value from StringVar
                auth_plugin="mysql_native_password"
            )
            cursor = Mydb.cursor()
            cursor.execute("SHOW DATABASES")
            data = cursor.fetchall()
            database1.delete(0, END)
            button=Button(root,text='Select Database',height=1,width=12,command=SelectDatabase,
                  background=color2,foreground=color4,highlightthickness=2,
                    highlightbackground=color2,highlightcolor='WHITE'
                    ,cursor='hand1',font=('Arial',12,'bold'),fg="Yellow",bg="#4A4A4A").place(x=55,y=530)
            for db in data:
                database1.insert(END, db[0])
            Mydb.close()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to show databases: {e}")


    Button(root, text='Show Databases', command=ShowDatabase, background=color2, foreground=color4, highlightthickness=2,
           highlightbackground=color2, highlightcolor='WHITE', width=13, height=2, cursor='hand1', font=('Arial', 15, 'bold'),
           fg="Yellow", bg="#4A4A4A").place(x=400, y=600)
    tables = Listbox(root, height = 20,width = 20,activestyle = 'dotbox', 
                                    font = "Helvetica",
                                    fg = "Yellow",selectmode=SINGLE,bg="#4A4A4A")
    tables.grid(row=1,column=2)
    def SelectTables():
        global datat2
        values = tables.curselection()[0]
        val = tables.get(values)
        datat2 = convertor(val)
      
        table_data()
        Button(root, text='INSERT', height=1, width=10,
               background=color2, foreground=color4, highlightthickness=2,
               highlightbackground=color2, highlightcolor='WHITE',
               fg="Yellow", bg="#4A4A4A", cursor='hand2', font=('Arial', 12, 'bold'), command=AddButton).place(x=500, y=400)
        Button(root, text='DELETE', height=1, width=10,
               background=color2, foreground=color4, highlightthickness=2,
               highlightbackground=color2, highlightcolor='WHITE',
               fg="Yellow", bg="#4A4A4A", cursor='hand2', font=('Arial', 12, 'bold'), command=Delete_data).place(x=650, y=400)
        Button(root, text='UPDATE', height=1, width=10,
               background=color2, foreground=color4, highlightthickness=2,
               highlightbackground=color2, highlightcolor='WHITE',
               fg="Yellow", bg="#4A4A4A", cursor='hand2', font=('Arial', 12, 'bold'), command=delete_update).place(x=800, y=400)


    def SelectDatabase():
        try:
            global datab
            values=database1.curselection()[0]
            val=database1.get(values)
            datab=convertor(val)
            Mydb=Myconn.connect(host='Localhost',
                            user='root',
                            password='root',
                            auth_plugin="mysql_native_password",
                            database=datab)
            buttontable=Button(root,text='Select Table',height=1,width=12,command=SelectTables,
                        background=color2,foreground=color4,highlightthickness=2,
                        highlightbackground=color2,highlightcolor='WHITE'
                        ,cursor='hand2',font=('Arial',12,'bold'),fg="Yellow",bg="#4A4A4A").place(x=280,y=530)
            cursor=Mydb.cursor()
            cursor.execute("show tables")
            tables.delete(0,END)
            data=cursor.fetchall()
            for i in data:
                tables.insert(END,i)
            Mydb.commit()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to select database: {e}")

    def Delete():
        global datat2, dname
        try:
            Mydb = Myconn.connect(
                host='localhost',
                user=userr,
                password=passw,
                auth_plugin="mysql_native_password",
                database=datab
            )
            cursor = Mydb.cursor()
            dname = dename.get()
            query = ("DELETE FROM " + datat2 + " WHERE " + cn[0][0] + " = %s")
            cursor.execute(query, (dname,))
            Mydb.commit()
            clear_text_fields()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to delete data: {e}")

    def Delete_data():
        f3=Frame(root,height=130,width=800,bg="#4A4A4A")
        for i in cn:
            new=i[0]
            break  
        label_name=Label(f3,text=new,font=("times new roman",15,"bold"),bg="#4A4A4A",fg="Yellow").place(x=100,y=30)
        en_name=Entry(f3,textvariable=dename,fg="Yellow",bg="#4A4A4A").place(x=190,y=40)
        Submit1=Button(f3,text='SUBMIT',height=1,width=10,
                  background=color2,foreground=color4,highlightthickness=2,
                    highlightbackground=color2,highlightcolor='WHITE'
                    ,cursor='hand2',font=('Arial',12,'bold'),fg="Yellow",bg="#4A4A4A",command=Delete).place(x=370,y=40)
        f3.pack_propagate()
        f3.place(x=500,y=460)
    def clear_text_fields():
        for var in string:
            var.set("")
        dename.set("")

    def delete_update():
        table_data()

    def table_data():
        global datab
        global datat2
        try:
            Mydb=Myconn.connect(host='Localhost',
                            user=userr,
                            password=passw,
                            auth_plugin="mysql_native_password",
                            database=datab
                            )
            cursor=Mydb.cursor()
            query = "SELECT * FROM "+datat2+" LIMIT 0,10"
            cursor.execute(query)
            f2=Frame(root,height=300,width=800,bg="#4A4A4A")
            tableprint=Listbox(f2, height = 15,width = 60,activestyle = 'dotbox', 
                                        font = "Helvetica",
                                        fg = "Yellow",bg="#4A4A4A")
            tableprint.place(x=0,y=0)
            f2.pack_propagate()
            f2.place(x=500,y=40)
            i=0
            for datat in cursor:
                for j in range(len(datat)):
                    e = Entry(tableprint, width=15, fg='Yellow',bg="#4A4A4A",font=(2))
                    e.grid(row=i, column=j)
                    e.insert(END, datat[j])
                i=i+1
            column_name()
            Mydb.commit()
            clear_text_fields()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to retrieve table data: {e}")

   
    def add_item():
        try:
            Mydb = Myconn.connect(
                host='localhost',
                user=userr,
                password=passw,
                auth_plugin="mysql_native_password",
                database=datab
            )
            cursor = Mydb.cursor()
            qr = ','.join(['%s'] * len(cn))
            tdata = [i.get() for i in string]
            query = "INSERT INTO " + datat2 + " VALUES(" + qr + ")"
            cursor.execute(query, tdata)
            Mydb.commit()
            clear_text_fields()
            delete_update()
        except Myconn.Error as e:
            messagebox.showerror("Error", f"Failed to insert data: {e}")

    def AddButton():
        global cn
        global string
        global count
        y1 = 10
        f4=Frame(root,height=130,width=800,bg="#4A4A4A")
        
        j=0
        stop=0
        print(cn)
       
        for i in cn:
            l1=Label(f4,text=i[0],font=("Arial",15),fg="Yellow",bg="#4A4A4A").place(x = 0, y = y1)
            y1 = y1 + 30
            stop=stop+1
        #info.set(varnames)
        y2=10
        j=0
        count=0
        for i in string:
            e1=Entry(f4,textvariable=i,font=("Arial",15),fg="Yellow",bg="#4A4A4A").place(x = 120, y = y2)
            y2=y2+30
            count=count+1
            if(stop==count):
                break
        
        Submit_Button=Button(f4,text='SUBMIT',height=1,width=10,
                  background=color2,foreground=color4,highlightthickness=2,
                    highlightbackground=color2,highlightcolor='WHITE'
                    ,fg="Yellow",bg="#4A4A4A",cursor='hand2',font=('Arial',12,'bold'),command=add_item).place(x=370,y=40)
        f4.pack_propagate()
        f4.place(x=500,y=460)

    root.mainloop()

   
except Exception as e:
    messagebox.showerror("Error", f"INVALID ACTION: {e}")
    print(e)
