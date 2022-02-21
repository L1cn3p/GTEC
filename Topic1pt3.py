from tkinter import *
from tkinter.ttk import *
import csv
import os
import sqlite3

id_count = 0
conn = sqlite3.connect('student.db')
c = conn.cursor()
try:
    c.execute("""CREATE TABLE students (
            name text,
            course text,
            institute text,
            fees text,
            id int
        )""")
except:
    pass

app = Tk()
app.title('Topic 1.3')
app.geometry('700x500')

# 12 - 16)
# students is a dict with key=pk, val=student
students = {}
name = Entry(app)
name.grid(row=0,column=1)
Label(app, text='Student Name').grid(row=0, column=0)

course = Entry(app)
course.grid(row=1,column=1) 
Label(app, text='Course').grid(row=1, column=0)

institute = Entry(app)
institute.grid(row=2,column=1) 
Label(app, text='Institute').grid(row=2, column=0)

fees = Entry(app)
fees.grid(row=3,column=1) 
Label(app, text='Fees').grid(row=3, column=0)

my_tree = Treeview(app)
my_tree['columns'] = ('name', 'course', 'institute', 'fees', 'id')
my_tree.column("#0",anchor=W, width=35)
my_tree.column("name",anchor=W, width=120)
my_tree.column("course",anchor=W, width=120)
my_tree.column("institute",anchor=W, width=120)
my_tree.column("fees",anchor=W, width=120)
my_tree.column("id",anchor=W, width=35)
my_tree.heading("#0",text="#", anchor=W)
my_tree.heading("name",text="name", anchor=W)
my_tree.heading("course",text="course", anchor=W)
my_tree.heading("institute",text="institute", anchor=W)
my_tree.heading("fees",text="fees", anchor=W)
my_tree.heading("id",text="id", anchor=W)

my_tree.grid(row=9, column=1)

def remove_all():
	my_tree.delete(*my_tree.get_children())

def get_queryset():
    remove_all()
    c.execute("SELECT rowid, * FROM students")
    records = c.fetchall()
    for rec in records:
        my_tree.insert(parent='', index='end', text=str(rec[0]), values=(rec[1],rec[2],rec[3],rec[4],rec[0]))
    
    conn.commit()
    app.update()

def select_record(e):
    name.delete(0,END)
    course.delete(0,END)
    institute.delete(0,END)
    fees.delete(0,END)

    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    name.insert(0, values[0])
    course.insert(0, values[1])
    institute.insert(0, values[2])
    fees.insert(0, values[3])


def add_record():
    c.execute("INSERT INTO students VALUES (?,?,?,?,?)", (str(name.get()), str(course.get()), str(institute.get()), str(fees.get()), None))
    name.delete(0,END)
    course.delete(0,END)
    institute.delete(0,END)
    fees.delete(0,END)
    get_queryset()

def update_record():
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    c.execute("UPDATE students SET name = :name, course = :course, institute = :institute, fees = :fees, id = :id WHERE oid = :oid",
    {
        'name': name.get(),
        'course': course.get(),
        'institute': institute.get(),
        'fees': fees.get(),
        'id': values[4],
        'oid': values[4]
    })
    conn.commit()
    name.delete(0,END)
    course.delete(0,END)
    institute.delete(0,END)
    fees.delete(0,END)
    get_queryset()
    

def remove_record():
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')
    print(values[4])
    c.execute("DELETE from students WHERE oid=(?)",(values[4],))
    conn.commit()
    my_tree.delete(selected)
    name.delete(0,END)
    course.delete(0,END)
    institute.delete(0,END)
    fees.delete(0,END)
    get_queryset()

my_tree.bind("<ButtonRelease-1>", select_record)
add_btn = Button(app, text='add', command=add_record)
add_btn.grid(row=4, column=1) 
remove_btn = Button(app, text='remove', command=remove_record)
remove_btn.grid(row=10, column=1) 
update = Button(app, text='update', command=update_record)
update.grid(row=5, column=1) 



get_queryset()
app.mainloop()
conn.close()
