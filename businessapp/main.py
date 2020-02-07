from tkinter import *
from bill_book import *
import database



root = Tk()
list1=0

def get_selected_row(event):
    global selected_tuple,list1,customer_name_entry,date_entry,grand_total_entry,mo_no_entry
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

    customer_name_entry.delete(0,END)
    customer_name_entry.insert(END,selected_tuple[1])

    date_entry.delete(0,END)
    date_entry.insert(END,selected_tuple[2])    

    grand_total_entry.delete(0,END)
    grand_total_entry.insert(END,selected_tuple[3])

    mo_no_entry.delete(0,END)
    mo_no_entry.insert(END,selected_tuple[4])

def layout():
    root.title("Khata Book")
    root.geometry("850x550")
    root.resizable(0, 0)

def search():
    search_frame = Frame(root,height=50,bg="#dbfcff")
    search_frame.pack(fill = X)
    
    search_entry = Entry(search_frame,text="",width=50)
    search_entry.place(x=225,y=15)

    search_buttaon = Button(search_frame,text="Search",width=10,bg="royalblue1")
    search_buttaon.place(x=535,y=13)


def button():
    button_frame = Frame(root,height=500,width=400,bg="#91ccdb")
    button_frame.place(x=0,y=50)

    create_bill = Button(button_frame,text="Create Bill",width=20,height = 3 ,bg="#54cc4b",font="arail 10 bold",command = billbook)
    create_bill.place(x=20,y=100)

    edit_bill = Button(button_frame,text="Edit Bill",width=20,height = 3,bg="#54cc4b",font="arail 10 bold")
    edit_bill.place(x=200,y=100)

    viewall = Button(button_frame,text="ViewAll",width=20,height = 3,bg="#54cc4b",font="arail 10 bold")
    viewall.place(x=20,y=200)

    delete_bill = Button(button_frame,text="Delete Bill",width=20,height = 3,bg="#54cc4b",font="arail 10 bold")
    delete_bill.place(x=200,y=200)

def listbox():
    global list1
    list1=Listbox(root,height=35,width=75,bg="#edd8a4")
    list1.place(x=400,y=50)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)


    list1.bind('<<ListboxSelect>>',get_selected_row)


layout()
search()
button()
listbox()
root.mainloop()