from tkinter import *
from tkinter.ttk import *
import csv
import os

app = Tk()
app.title('Topic 1.2')
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

# 13) submit adds students to the students dict:
def submit():
    values = {}
    values['name'] = str(name.get()) if str(name.get()) else None
    name.delete(0,END)
    values['course'] = str(course.get()) if str(course.get()) else None
    course.delete(0,END)
    values['institute'] = str(institute.get()) if str(institute.get()) else None
    institute.delete(0,END)
    values['fees'] = str(fees.get()) if str(fees.get()) else None
    fees.delete(0,END)

    # 14) keeps adding students to the students dict:
    students[str(len(students.keys()))] = values


submit_btn = Button(app, text='Submit', command=submit)
submit_btn.grid(row=4, column=1)

# 14) to CSV file
def to_csv():
    file_exists = os.path.isfile("students.csv")
    values = {}
    values['name'] = str(name.get()) if str(name.get()) else None
    name.delete(0,END)
    values['course'] = str(course.get()) if str(course.get()) else None
    course.delete(0,END)
    values['institute'] = str(institute.get()) if str(institute.get()) else None
    institute.delete(0,END)
    values['fees'] = str(fees.get()) if str(fees.get()) else None
    fees.delete(0,END)
    
    with open("students.csv", "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name','course','institute','fees'])
        if not file_exists:
            writer.writeheader()
        writer.writerow(values)

def csv_treeview():
    n = 0
    my_tree.delete(*my_tree.get_children())
    with open("students.csv", "r") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        header = ['name', 'course', 'institute', 'fees']
        for row in reader:
            if not row or row[0].split(',') == header:
                continue
            print(row[0].split(','))
            line = row[0].split(',')
            my_tree.insert(parent='', index='end', text=str(n), values=(line[0],line[1],line[2],line[3]))
            n += 1
    app.update()

my_tree = Treeview(app)
my_tree['columns'] = ('name', 'course', 'institute', 'fees')
my_tree.column("#0",anchor=W, width=35)
my_tree.column("name",anchor=W, width=120)
my_tree.column("course",anchor=W, width=120)
my_tree.column("institute",anchor=W, width=120)
my_tree.column("fees",anchor=W, width=120)
my_tree.heading("#0",text="#", anchor=W)
my_tree.heading("name",text="name", anchor=W)
my_tree.heading("course",text="course", anchor=W)
my_tree.heading("institute",text="institute", anchor=W)
my_tree.heading("fees",text="fees", anchor=W)

my_tree.grid(row=9, column=1)
csv_btn = Button(app, text='To CSV', command=to_csv)
csv_tree_btn = Button(app, text='CSV Treeview', command=csv_treeview)
csv_tree_btn.grid(row=8, column=2)
csv_btn.grid(row=5, column=1) 




app.mainloop()
