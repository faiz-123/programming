from tkinter import *
import sqlite3


name = 0
orderno = 0
gstno = str
date = str
no=0

width_list= [7,70,10,10,12,12,15]
width_list2= [9,82,12,12,15,15,18]
x_list = [60,114,609,684,759,848,937]


no=[]
descritption = str
qty = 0
rate = 0
gstrate = 0
amount = 0

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

    adress_label = Label(middle_frame,text="Shop No - 1,amdavadi bazar,station road,nadiad, Pin Code:387001 State/country: gujrat/india \nMob.: 7405552500, 8780146337, Email: faizbabuna55@gmail.com web:www.faizgarments.com",bg="white",fg="black",font="arial 10")
    adress_label.place(x=30,y=5)

    customer_name_label = Label(middle_frame,text = "To: ",font="arial 12 bold",bg="white")
    customer_name_label.place(x=60,y=50)

    customer_name_entry = Entry(middle_frame,textvariable=name,width=83,relief=SOLID)
    customer_name_entry.place(x=120,y=52)

    order_label = Label(middle_frame,text="Order No.",font="arial 12 bold",bg="white")
    order_label.place(x=890,y=50)

    order_entry=Entry(middle_frame,textvariable=orderno,width=20,relief=SOLID)
    order_entry.place(x=970,y=50)

    gst_label = Label(middle_frame,text = "Gst No.",font="arial 12 bold",bg="white")
    gst_label.place(x=60,y=80)

    gst_entry=Entry(middle_frame,textvariable=gstno,width=83,relief=SOLID)
    gst_entry.place(x=120,y=80)


    date_label = Label(middle_frame,text="Date:",font="arial 12 bold",bg="white")
    date_label.place(x=890,y=80)

    date_entry=Entry(middle_frame,textvariable=date,width=20,relief=SOLID)
    date_entry.place(x=970  ,y=80)

def headinglabel(last_fram):

    heading_label_name=["No.","DESCRIPTION","QTY.","RATE","HSN/SAC","GST RATE","AMOUNT"]

    global width_list,x_list
    for i in range(len(heading_label_name)):
        last_heading_label = Label(last_fram,text=heading_label_name[i],relief=RIDGE, bg="skyblue",fg="black",width=width_list[i])
        last_heading_label.place(x=x_list[i],y=10)


def thirdframe(root):
    global width_list,x_list,no,descritption,qty,rate,gstrate,amount
    third_frame = Frame(root,height=212,bg='white')
    third_frame.pack(fill=X)

    headinglabel(third_frame)
    t=30
    for i in range(10):
        col=[]
        no_entry = Entry(third_frame,text='',width=width_list2[0],relief=SOLID)
        no_entry.place(x=x_list[0],y=t)    
        col.append(no_entry)
    
        description_entry = Entry(third_frame,text="",width=width_list2[1],relief=SOLID)
        description_entry.place(x=x_list[1],y=t)    
        col.append(description_entry)

        qty_entry = Entry(third_frame,text = "",width=width_list2[2],relief=SOLID)
        qty_entry.place(x=x_list[2],y=t)    
        col.append(qty_entry)

        rate_entry = Entry(third_frame,text = "",width=width_list2[3],relief=SOLID)
        rate_entry.place(x=x_list[3],y=t)
        col.append(rate_entry)    

        no_entry = Entry(third_frame,text = "",width=width_list2[4],relief=SOLID)
        no_entry.place(x=x_list[4],y=t)    
        col.append(no_entry)

        gst_entry = Entry(third_frame,text = "",width=width_list2[5],relief=SOLID)
        gst_entry.place(x=x_list[5],y=t)    
        col.append(gst_entry)

        amount_entry = Entry(third_frame,text = "",width=width_list2[6],relief=SOLID)
        amount_entry.place(x=x_list[6],y=t)   
        col.append(amount_entry)

        no.append(col)
        t=t+18

def getvalue():
    for i in range(7):
        print(i,no[0][i].get())


def lastframe(root):
    last_fram = Frame(root,height=230,bg='white')
    last_fram.pack(fill=X)

    amount_words_label = Label(last_fram,text="Amount in Words:",font="arial 12 bold",bg="white")
    amount_words_label.place(x=60,y=-1)

    amount_words_entry = Entry(last_fram,text="",width=50,relief=RIDGE)
    amount_words_entry.place(x=205,y=-1)

    cash = IntVar()
    account = IntVar()
    paid = IntVar()

    cash_check = Checkbutton(last_fram, text="Cash", variable=cash,bg="white",font="arial 12 bold")
    cash_check.place(x=60,y=40)

    account_check = Checkbutton(last_fram, text="Ammount", variable=account,bg="white",font="arial 12 bold")
    account_check.place(x=140,y=40)

    paid_check = Checkbutton(last_fram, text="Paid", variable=paid,bg="white",font="arial 12 bold")
    paid_check.place(x=260,y=40)


    subtotal_entry = Entry(last_fram,text="",width=18,relief=SOLID)
    subtotal_entry.place(x=937,y=-1)





def main():
    root = Tk()
    root.geometry('1130x650')
    root.title('Bill Book')
    topframe(root)
    middleframe(root)
    thirdframe(root)
    lastframe(root)
    # t1 =Button(root,command = getvalue,height = 10)
    # t1.place(x=10,y=550)
    root.mainloop()

    


if __name__== "__main__":
    main()