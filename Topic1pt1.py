from tkinter import *
from tkinter.ttk import *
import tkinter.scrolledtext
import time
import math

def hello():
    print('Hello')

app = Tk()
# 1)
app.title('Topic 1.1')
app.geometry('500x700')

# 2) exit/hello button
exit_btn = Button(app, text='exit', width=12, command=exit)
exit_btn.grid(row=2,column=0,pady=20)

hello_btn = Button(app, text='hello', width=12, command=hello)
hello_btn.grid(row=2,column=1,pady=20)

# 3) combo box
current_var = StringVar()
combobox = Combobox(app, textvariable=current_var)
combobox['values'] = ('value1','value2','value3')
combobox['state'] = 'readonly'
combobox.grid(row=3,column=1)
Label(app, text='combo box:').grid(row=3,column=0)

# 4) check button
check_btn = Checkbutton(app, text='check button:')
check_btn.grid(row=4, column=0)


# 5) spinbox
spinbox = Spinbox(app, from_=-10, to=10)
spinbox.grid(row=4, column=1)

# 6) text widget

text = Text(app, height=3, width=25)

def crop_text(text=text):
    content = text.get(1.0, END)
    text.delete(1.0,END)
    if len(str(content)) > 1:
        text.insert(END, str(content)[1:-2])

text.insert(END, 'Sample text')
text.grid(row=5, column=0)
text_btn = Button(app, text='crop text', width=12, command=crop_text)
text_btn.grid(row=5,column=1,pady=20)

# 7) accept values
name = Entry(app)
name_label = Label(app, text='name')
name.grid(row=6, column=1)
name_label.grid(row=6, column=0)

age = Entry(app)
age_label = Label(app, text='age')
age.grid(row=7, column=1)
age_label.grid(row=7, column=0)

occupation = Entry(app)
occupation_label = Label(app, text='occupation')
occupation_label.grid(row=8, column=0)
occupation.grid(row=8, column=1)

def submit():
    values = {}
    values['name'] = str(name.get()) if str(name.get()) else None
    name.delete(0,END)
    values['age'] = int(age.get()) if int(age.get()) else None
    age.delete(0,END)
    values['occupation'] = str(occupation.get()) if str(occupation.get()) else None
    occupation.delete(0,END)
    print(values.items())

submit_btn = Button(app, text='submit', command=submit)
submit_btn.grid(row=9, column=1)

# 8) radio buttons
radio_btns = {
    "RadioButton 1" : "1",
    "RadioButton 2" : "2",
    "RadioButton 3" : "3",
    }
 
for (text, value) in radio_btns.items():
    Radiobutton(app, text=text, value=value).grid(row=9+int(value), column=0)

# 9) scrolled text
scrolled_text = tkinter.scrolledtext.ScrolledText(app, width=30, height=10)
scrolled_text.grid(row=13, column=1)
Label(app, text='scrolled textbox').grid(row=13,column=0)

# 10) progress bar
prog_bar = Progressbar(app, orient=HORIZONTAL, length=200, mode='determinate')
prog_bar.grid(row=14, column=1)
def step():
    if prog_bar['value'] > 0:
        return
    for i in range(210):
        app.update_idletasks()
        prog_bar['value'] += 0.5
        time.sleep(0.01)
    time.sleep(3)
    prog_bar['value'] = 0
Button(app, text='start', command=step).grid(row=14,column=0)

# 11) find the volume of a rectangular box
width = Entry(app)
width.grid(row=15,column=1)
Label(app,text='width').grid(row=15,column=0)
height = Entry(app)
height.grid(row=16,column=1)
Label(app,text='height').grid(row=16,column=0)
length = Entry(app)
length.grid(row=17,column=1)
Label(app,text='length').grid(row=17,column=0)
vol = Entry(app)
vol.grid(row=19, column=0)
tsa = Entry(app)
tsa.grid(row=19, column=1)
def get_vals():
    try:
        w = float(width.get())
        h = float(height.get())
        l = float(length.get())
    except:
        print('Please input valid numbers')
        return
    if not (w*h*l):
        return
    vals = {}
    vals['width'] = w
    vals['height'] = h
    vals['length'] = l
    return vals

def volume():
    vals = get_vals()
    if not vals:
        return
    vol.delete(0,END)
    vol.insert(END,str(math.prod(list(vals.values()))))
def TSA():
    vals = get_vals()
    if not vals:
        return
    surface_area = (vals['width']*vals['height']*2) + (vals['width']*vals['length']*2) + (vals['height']*vals['length']*2)
    tsa.delete(0,END)
    tsa.insert(END, str(surface_area))

Button(app, text='Calculate Volume', command=volume).grid(row=18, column=0)
Button(app, text='Calculate TSA', command=TSA).grid(row=18, column=1)


app.mainloop()