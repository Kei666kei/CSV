from tkinter import *
from tkinter import ttk
import csv


GUI = Tk()
GUI.title('บันทึกประจำวัน')
GUI.geometry('800x600')

L1 = Label(GUI,text='บันทึก',font=('Sukhumvit',40),fg='green')
L1.pack()

LF1=ttk.LabelFrame(GUI)
LF1.pack()

v_data= StringVar()
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Sukhumvit',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def Savedata():
    t = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    data = v_data.get()
    text = [data,t]
    writecsv(text)
    v_data.set('')

B1 = ttk.Button(LF1,text='บันทึก',command=Savedata)
B1.pack(ipadx=20,ipady=20)

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data=list(fr)
    return data
data = readcsv()

B2 = ttk.Button(LF1,text='สรุป',command=readcsv)
B2.pack(ipadx=20,ipady=20)

print(data)




GUI.mainloop()


#data=['หนังสือการ์ตูน',70,'7.00น.']
#writecsv(data)