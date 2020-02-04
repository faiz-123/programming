from tkinter import *


name = 0
orderno = 0
gstno = str
date = str
no=0
width_list= [7,30,10,10,12,12,15]
x_list = [60,119,602,685,768,867,966]


no=[]
descritption = str
qty = 0
rate = 0
gstrate = 0
amount = 0

values ={}







def topframe(root):
    top_fram = Frame(root,height = 120,bg='#fcc2ec')
    top_fram.pack(fill = X)

    top_icon_fram =Frame(top_fram,height = 100,bg="white",width=400)
    top_icon_fram.place(x=30,y=35)

    top_logo= Label(top_icon_fram,text="FZ",bg="white",fg="#9394c7",font=" Fixedsys 60 bold italic")
    top_logo.place(x=10,y=5)

    top_icon_label = Label(top_icon_fram,text="FAIZ \n GARMENTS",bg="white",fg="#94006c",font="roman 25 bold")
    top_icon_label.place(x=110,y=10)

    top_label = Label(top_fram,text = "TAX INOICE",fg='#000000',font= "arial 30",bg="#fcc2ec")
    top_label.place(x=500,y=50)

    top_label_no = Label(top_fram,text = "No.:",fg='#000000',font= "arial 15 bold",bg="#fcc2ec")
    top_label_no.place(x=850,y=30)

    top_label_no = Label(top_fram,text = "C/N No.:\nPAN No.:\nGst No.:",fg='#000000',font= "arial 13",bg="#fcc2ec")
    top_label_no.place(x=850,y=53)

    

def middleframe(root):
    global name,orderno,date,gstno
    middle_frame = Frame(root,height=130,bg="white")
    middle_frame.pack(fill=X)
    middle_label = Label(middle_frame,text="Shop No - 1,amdavadi bazar,station road,nadiad, Pin Code:387001 State/country: gujrat/india \nMob.: 7405552500, 8780146337, Email: faizbabuna55@gmail.com web:www.faizgarments.com",bg="white",fg="black",font="arial 10")
    middle_label.place(x=30,y=5)

    name_label = Label(middle_frame,text = "To",bg='white',fg='black',font="arial 10 bold")
    name_label.place(x=60,y=50)
    name_entry = Entry(middle_frame,textvariable=name,width=88)
    name_entry.place(x=80,y=50)

    order_label = Label(middle_frame,text="Order No.",font="arial 12 bold",bg="white")
    order_label.place(x=800,y=50)

    order_entry=Entry(middle_frame,textvariable=orderno,width=20)
    order_entry.place(x=880,y=50)

    gst_label = Label(middle_frame,text = "Gst No.",font="arial 12 bold",bg="white")
    gst_label.place(x=60,y=80)
    gst_entry=Entry(middle_frame,textvariable=gstno,width=83)
    gst_entry.place(x=120,y=80)


    date_label = Label(middle_frame,text="Date:",font="arial 12 bold",bg="white")
    date_label.place(x=800,y=80)
    date_entry=Entry(middle_frame,textvariable=date,width=20)
    date_entry.place(x=845  ,y=80)

def headinglabel(last_fram):

    heading_label_name=["No.","DESCRIPTION","QTY.","RATE","HSN/SAC","GST RATE","AMOUNT"]
    # width_list= [7,60,10,10,12,12,15]
    # x_list = [60,119,602,685,768,867,966]

    global width_list,x_list
    for i in range(len(heading_label_name)):
        last_heading_label = Label(last_fram,text=heading_label_name[i],relief=RIDGE, bg="skyblue",fg="black",width=width_list[i])
        last_heading_label.place(x=x_list[i],y=10)
    


def getvalue():
    for i in range(7):
        print(no[0][i].get())


def lastframe(root):
    global width_list,x_list,no,descritption,qty,rate,gstrate,amount
    last_fram = Frame(root,height=760,bg='white')
    last_fram.pack(fill=X)

    headinglabel(last_fram)
    t=30
    for i in range(10):
        col=[]
        no_entry = Entry(last_fram,text='',width=width_list[0])
        no_entry.place(x=x_list[0],y=t)    
        col.append(no_entry)
    
        description_entry = Entry(last_fram,text="",width=width_list[1])
        description_entry.place(x=x_list[1],y=t)    
        col.append(description_entry)

        qty_entry = Entry(last_fram,text = "",width=width_list[2])
        qty_entry.place(x=x_list[2],y=t)    
        col.append(qty_entry)

        rate_entry = Entry(last_fram,text = "",width=width_list[3])
        rate_entry.place(x=x_list[3],y=t)
        col.append(rate_entry)    

        no_entry = Entry(last_fram,text = "",width=width_list[4])
        no_entry.place(x=x_list[4],y=t)    

        gst_entry = Entry(last_fram,text = "",width=width_list[5])
        gst_entry.place(x=x_list[5],y=t)    
        col.append(gst_entry)

        amount_entry = Entry(last_fram,text = "",width=width_list[6])
        amount_entry.place(x=x_list[6],y=t)   
        col.append(amount_entry)

        no.append(col)
        t=t+20

        
     



def main():
    root = Tk()
    root.geometry('1130x650')
    root.title('Bill Book')
    topframe(root)
    middleframe(root)
    lastframe(root)
    t1 =Button(root,command = getvalue,height = 10)
    t1.place(x=10,y=550)

    root.mainloop()

if __name__== "__main__":
    main()

















