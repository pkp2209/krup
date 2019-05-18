#12
from tkinter import *

root = Tk()
root.geometry("500x400+300+60")

intxt = Entry(root)
intxt["width"] = 500
intxt.pack(side = TOP)

button1 = Button(root)
button1["text"] = "perform programm"
button1.pack(side = TOP)

outtxt = Text(root)
outtxt["width"] = 500
outtxt.pack(side = TOP)

def string_value(string: str):
    value = 0
    for c in string:
        if c.isdigit():
            value += int(c)
        elif c.isalpha():
            value += ord(c.lower()) - 96
        else:
            value += 1
    return value

def perfomance(event):
    outtxt.delete('1.0', END)
    file_name = intxt.get()
    open_file = open(file_name, "r", encoding='utf-8')
    str_list = [string.rstrip('\n') for string in open_file if string != '\n']
    str_list_with_value = list(map(lambda s: (s, string_value(s)), str_list))
    open_file.close()
    for string in sorted(str_list_with_value, key=lambda s: s[1], reverse=True):
        outtxt.insert(END, "\"" + string[0] + " = " + str(string[1]) + "\"\n")
    return 0

button1.bind('<Button-1>', perfomance)
button1.pack()

root.mainloop()
