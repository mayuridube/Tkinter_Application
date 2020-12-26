# import everything from tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkcalendar import DateEntry
# database Package
import mysql.connector


def warning_message(header, message):
    mb.showwarning(header, message)


def info_message(header, message):
    mb.showinfo(header, message)


def mysql_connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    return mydb


def submit_register_form():
    name = entry_1.get()
    gender = var.get()
    selected_class = entry_3.get()
    date = cal.get()
    mentor_name = c.get()
    print(mentor_name)
    complaint_type = d.get()
    entered_complaint = complaint.get()

    if "" in (name, selected_class, entered_complaint)\
            or mentor_name == "Select Name of Teacher" or complaint_type == "Select Type of complaint" or gender == 0:
        warning_message("Empty", "fields are empty")
    else:
        print("not empty")
        connection = mysql_connect()
        cursor = connection.cursor()
        sql = "INSERT INTO complaint_management.register_complaint " \
              "(Name, Gender, Class, Date, Mentor_name, Type, Complaint)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s )"
        val = (name, gender, selected_class, date, mentor_name, complaint_type, entered_complaint)
        cursor.execute(sql, val)
        connection.commit()
        info_message("Success", "Successfully Registered your complaint")
        new_window.destroy()


def register_form():
    global entry_1, var, entry_3, cal, c, d, complaint, new_window
    # Creating object 'root' of Tk()
    new_window = Toplevel(root)
    # Providing Geometry to the form
    new_window.geometry("600x600")

    # Providing title to the form
    new_window.title('Registration Form')

    # this creates 'Label' widget for Registration Form and uses place() method.
    label_01 = Label(new_window, text="Register Your Complaint", width=20, font=("bold", 20))
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_01.place(x=50, y=60)

    # this creates 'Label' widget for name and uses place() method.
    label_1 = Label(new_window, text="Name", width=20, font=("bold", 10))
    label_1.place(x=50, y=130)
    # this will accept the input string text from the user.
    entry_1 = Entry(new_window)
    entry_1.place(x=240, y=130, width=280)

    # this creates 'Label' widget for Gender and uses place() method.
    label_2 = Label(new_window, text="Gender", width=20, font=("bold", 10))
    label_2.place(x=50, y=180)
    # the variable 'var' mentioned here holds Integer Value, by deault 0
    var = StringVar()
    # this creates 'Radio button' widget and uses place() method
    Radiobutton(new_window, text="Male", variable=var, value="Male").place(x=235, y=180)
    Radiobutton(new_window, text="Female",  variable=var, value="Female").place(x=320, y=180)

    # this creates 'Label' widget for Email and uses place() method.
    label_3 = Label(new_window, text="Class", width=20, font=("bold", 10))
    label_3.place(x=50, y=230)
    entry_3 = Entry(new_window)
    entry_3.place(x=240, y=230, width=280)

    # this creates 'Label' widget for Email and uses place() method.
    label_4 = Label(new_window, text="Date", width=20, font=("bold", 10))
    label_4.place(x=50, y=280)

    cal = DateEntry(new_window, width=30, bg="darkblue", fg="white", year=2020)
    cal.place(x=240, y=280, width=280)

    # this creates 'Label' widget for Email and uses place() method.
    label_5 = Label(new_window, text="Mentor Name", width=20, font=("bold", 10))
    label_5.place(x=50, y=330)

    list_of_teacher = ['', 'suresh', 'mahesh', 'ganesh', 'rajesh', 'others']
    # the variable 'c' mentioned here holds String Value, by default ""
    c = StringVar()
    droplist = OptionMenu(new_window, c, *list_of_teacher)
    droplist.config(width=30)
    c.set('Select Name of Teacher')
    droplist.place(x=240, y=330)

    # this creates 'Label' widget for country and uses place() method.
    label_6 = Label(new_window, text="Type Of Complaint", width=20, font=("bold", 10))
    label_6.place(x=50, y=380)
    # this creates list of countries available in the drop down list.
    list_of_type = ['', 'Study-Related', 'Others']
    # the variable 'c' mentioned here holds String Value, by default ""
    d = StringVar()
    droplist1 = OptionMenu(new_window, d, *list_of_type)
    droplist1.config(width=30)
    d.set('Select Type of complaint')
    droplist1.place(x=240, y=380)

    # this creates 'Label' widget for Email and uses place() method.
    label_7 = Label(new_window, text="Complaint", width=20, font=("bold", 10))
    label_7.place(x=50, y=430)
    complaint = StringVar()
    complaint = Entry(new_window, width=35, textvariable=complaint)
    complaint.place(x=240, y=430, height=50)

    # this creates button for submitting the details provides by the user
    Button(new_window, text='Submit', width=20, command=submit_register_form).place(x=180, y=550)

    # this will run the mainloop.
    mainloop()


def submit_teacher_login():
    # t_name = teacher_name.get()
    t_pass = password.get()

    if t_pass == "":
        warning_message("Empty", "fields are empty")
    else:
        if t_pass == "123456":
            info_message("Success", "your are Login!!!")
            new_window.destroy()
            complaint_report()
        else:
            warning_message("Incorrect", "Password is incorrect")
        # connect to mysql
        # connection = mysql_connect()
        # # fetch password using the entered name
        # sql_select_query = "select * from complaint_management.teacher where name = \'" + t_name + "\'"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_query)
        # records = cursor.fetchall()

        # if len(records) != 0:
        #     s_password = records[0][1]
        #     if t_pass == s_password:
        #         info_message("Success", "your are Login!!!")
        #     else:
        #         warning_message("Incorrect", "Password is incorrect")
        # else:
        #     warning_message("Incorrect", "Name is incorrect")


def teacher_login():
    global password, new_window
    new_window = Toplevel(root)

    # Providing Geometry to the form
    new_window.geometry("500x500")

    # Providing title to the form
    new_window.title('Teacher Login')

    # this creates 'Label' widget for Registration Form and uses place() method.
    label = Label(new_window, text="Teacher Login", width=20, font=("bold", 20))
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label.place(x=50, y=60)

    # this creates 'Label' widget for name and uses place() method.
    # label_1 = Label(new_window, text="Name", width=20, font=("bold", 10))
    # label_1.place(x=50, y=130)
    # # this will accept the input string text from the user.
    # teacher_name = Entry(new_window)
    # teacher_name.place(x=240, y=130)

    # this creates 'Label' widget for Email and uses place() method.
    label_3 = Label(new_window, text="Password", width=20, font=("bold", 10))
    label_3.place(x=50, y=180)
    password = Entry(new_window, show="*")
    password.insert(0, "123456")
    password.place(x=240, y=180)

    Button(new_window, text='Submit', width=20, command=submit_teacher_login).place(x=180, y=250)
    mainloop()


def update_report():
    connection = mysql_connect()
    cursor = connection.cursor()
    for j in range(len(var_dict)):
        var_obj = var_dict.get(j)
        j = j+1
        print(j)
        sql_update = "UPDATE complaint_management.register_complaint" \
                     " SET status = \'" + var_obj.get() + "\' WHERE No = " + str(j)
        cursor.execute(sql_update)
        connection.commit()
    info_message("Success", "Successfully apply changes")
    my_w.destroy()
    complaint_report()


def complaint_report():
    global var_dict,my_w
    my_w = Toplevel(root)

    my_w.geometry("1000x500")

    # add text
    # this creates 'Label' widget for Registration Form and uses place() method.
    label_1 = Label(my_w, text="Complaint Report", width=20, font=("bold", 20))
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_1.place(x=400, y=10)

    connection = mysql_connect()
    x = 30
    y = 80
    # check data in db
    # fetch password using the entered name    e.place(x=x, y=y)
    sql_select_query = "SELECT * FROM complaint_management.register_complaint "
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    if len(records) != 0:
        # fetch column name
        sql_select_query = "SHOW columns FROM complaint_management.register_complaint"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        records_1 = cursor.fetchall()
        for i, row in enumerate(records_1):
            header = Label(my_w, text=row[0])
            header.grid(row=i + 10, column=i + 10)
            header.place(x=x, y=y)
            # header.insert(END, row[0])
            if i < 4:
                x = x + 60
            elif i == 7:
                x = x + 250
            else:
                x = x + 100

    i = 0
    y = 100
    x = 30
    if len(records) == 0:
        y = 120
        label_1 = Label(my_w, text="No Data Present", width=60, font=("bold", 10))
        label_1.place(x=340, y=y)

    var_dict = dict()
    # for child in range(len(records)):
    for student in records:
        for j in range(len(student)):
            print(j,student[j])
            if j == 8:
                if student[j] == "solved":
                    var_dict[i] = StringVar()
                    var_dict[i].set('solved')

                    Checkbutton(my_w, variable=var_dict[i], onvalue="solved", offvalue="unsolved",
                                textvariable=var_dict[i]).place(x=x, y=y)
                else:
                    var_dict[i] = StringVar()
                    var_dict[i].set('unsolved')
                    Checkbutton(my_w, variable=var_dict[i], onvalue="solved", offvalue="unsolved",
                                textvariable=var_dict[i]).place(x=x, y=y)
            elif j <= 7:
                e = Entry(my_w, width=30)
                e.grid(row=i+10, column=j+10)
                e.place(x=x, y=y)
                e.insert(END, student[j])
            else:
                pass
            if j < 4:
                x = x+60
            elif j == 7:
                x = x+250
            else:
                x = x+100

        x = 30
        y = y + 20
        i = i + 1

    # Create a Button
    if not len(records) == 0:
        btn3 = Button(my_w, text='Apply', command=update_report)
        btn3.grid(row=1200, column=30, pady=10, padx=50)
        btn3.place(x=500, y=y+30)

    # button 2
    btn4 = Button(my_w, text='OK', command=my_w.destroy)
    btn4.grid(row=1200, column=90, pady=10, padx=100)
    btn4.place(x=650, y=y+30)
    my_w.mainloop()


# create a tkinter window
root = Tk()
root.title("Complaint Window")
# Open window having dimension 100x100
root.geometry('500x300')

# add text
# this creates 'Label' widget for Registration Form and uses place() method.
label_0 = Label(root, text="Complaint Window", width=20, font=("bold", 20))
# place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=100, y=10)

# this creates 'Label' widget for Registration Form and uses place() method.
label_0 = Label(root, text="Choose User Type", width=20, font=("bold", 15))
# place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=100, y=80)


# This will create style object
style = Style()
# Will add style to every available button
# even though we are not passing style
# to every button widget.
style.configure('TButton', font=('arebic', 10, 'bold'), foreground='Blue')

# Create a Button
btn1 = Button(root, text='Student', style='TButton', command=register_form)
btn1.grid(row=1200, column=30, pady=10, padx=50)
btn1.place(x=80, y=150)

# button 2
btn2 = Button(root, text='Teacher', command=teacher_login)
btn2.grid(row=1200, column=90, pady=10, padx=100)
btn2.place(x=300, y=150)

root.mainloop()

