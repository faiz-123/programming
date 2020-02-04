from tkinter import *
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

total_amount = 0

# global data= []

def genratebill():
    file = open("faizcutpeace.txt", "a+")
    billno_info = billno.get()  
    date_info = date.get()
    customer_name_info = customerName.get()
    file.write('\n                                                    ' + 'Oreder No: '+ str(billno_info)) 
    file.write('\n                                                    Date     : '+date_info)
    file.write('\nName: '+ customer_name_info + '\n\n')

    def infog(itemName,quantity,price,amount,no):
        
        global total_amount  
        itemName_info  =itemName.get()
        quantity_info  =quantity.get()
        price_info        =price.get()
        amount_info     =amount.get()
        
        itemName_info_l=len(itemName_info)
        quantity_info_l=len(str(quantity_info))
        price_info_l = len(str(price_info))
        amount_info_l =len(str(amount_info))

        total_amount = total_amount + amount_info        
       
        itemName_info_s=22-itemName_info_l
        quantity_info_s=7-quantity_info_l
        price_info_s = 7-price_info_l
        gst_s=13

        file.write('   '+no +'   '+'|'+itemName_info+itemName_info_s*' '+ '|  ' + str(quantity_info)+quantity_info_s*' '+'|  '+str(price_info)+price_info_s*' '+'|  '+gst_s*' '+'|  '+str(amount_info))
        file.write('\n----------------------------------------------------------------------------------\n')
        
    infog(itemName0,quantity0,price0,amount0,'1')
    infog(itemName1,quantity1,price1,amount1,'2')
    infog(itemName2,quantity2,price2,amount2,'3')
    infog(itemName3,quantity3,price3,amount3,'4')
    


def save_info():
    t =0 
    width_list= [8,30,10,10,15,16]
    x_list = [602,665,845,927,1010,1133]
    heading_label_name=["No","Item Name","Quantity","Price","Gst Rate","Amount"]
    textbox = Text(height=25, width=82)
    textbox.place(x=602,y=280)
    

    billno_info = billno.get()  
    date_info = date.get()
    customer_name_info = customerName.get()
    textbox.insert(END,'\n                                                    ' + 'Oreder No: '+ str(billno_info),END) 
    textbox.insert(END,'\n                                                    Date     : '+date_info)
    textbox.insert(END,'\nName: '+ customer_name_info)
    for i in range(6):
        heading_label = Label(text=heading_label_name[i],relief=RIDGE, bg="skyblue",fg="black",width=width_list[i])
        heading_label.place(x=x_list[i],y=360)

    textbox.insert(END,'\n\n\n')    
    
    def info(itemName,quantity,price,amount,no):
        global total_amount  
        itemName_info  =itemName.get()
        quantity_info  =quantity.get()
        price_info        =price.get()
        amount_info     =amount.get()
        
        itemName_info_l=len(itemName_info)
        quantity_info_l=len(str(quantity_info))
        price_info_l = len(str(price_info))
        amount_info_l =len(str(amount_info))

        total_amount = total_amount + amount_info        
       
        itemName_info_s=22-itemName_info_l
        quantity_info_s=7-quantity_info_l
        price_info_s = 7-price_info_l
        gst_s=13
        textbox.insert(END,'   '+no +'   '+'|'+itemName_info+itemName_info_s*' '+ '|  ' + str(quantity_info)+quantity_info_s*' '+'|  '+str(price_info)+price_info_s*' '+'|  '+gst_s*' '+'|  '+str(amount_info))
        textbox.insert(END,'\n----------------------------------------------------------------------------------\n')
    
    total_amount_text = Text(state='disabled',width=15,height=1)
    total_amount_text.place(x=417,y=357)
    
    info(itemName0,quantity0,price0,amount0,'1')
    info(itemName1,quantity1,price1,amount1,'2')
    info(itemName2,quantity2,price2,amount2,'3')
    info(itemName3,quantity3,price3,amount3,'4')
    
    total_amount_text.config(state='normal')
    total_amount_text.insert(END,total_amount)
    textbox.config(state='disabled')
    total_amount_text.config(state='disabled')
  










root =Tk()
lblwidth = 1055
root.geometry("{}x700".format(lblwidth))
root.configure(bg='violet')
labelfont = ('times', 30, 'bold')
fontmob = ('times',13,'bold')
l = Label(root, text = "", bg = "purple", fg = "yellow", width =lblwidth, height = "1",font=labelfont)
l.place(x=0,y=0)
shop_name_label = Label(root, text = "Faiz Cutpeace", bg = "purple", fg = "yellow",font=labelfont)
shop_name_label.place(x=530,y=0)
mob_no_label = Label(root, text = "Mob:- 7405552500", bg = "purple", fg = "yellow",font=fontmob)
mob_no_label.place(x=1150,y=1)


search = StringVar()
billno = IntVar()
date = StringVar()
customerName = StringVar()
itemName0 = StringVar()
itemName1 = StringVar()
itemName2 = StringVar()
itemName3 =StringVar()
itemName4 = StringVar()
quantity0 =IntVar()
quantity1 =IntVar() 
quantity2 =IntVar()
quantity3 =IntVar()
quantity4 = IntVar()
price0 =IntVar()
price1 =IntVar()
price2 =IntVar()
price3 =IntVar()
price4 = IntVar()
amount0 = IntVar()
amount1 =IntVar()
amount2 =IntVar()
amount3 =IntVar()
amount4 = IntVar()
subtotal= IntVar()

search_entry = Entry(root,textvariable=search, width="40")
search_entry.place(x=500,y=60)


search_button=Button(text="Search" ,bd='1')
search_button.place(x=829,y=56)



customer_label =  Label(root, text = "",bg="olive",font=labelfont,width=lblwidth)
customer_label.place(x=0,y=100)

customer_label =  Label(root, text = "Customer Detail",bg="olive" ,fg = "white",font=labelfont)
customer_label.place(x=530,y=100)





customer_name_lable = Label(text='Customer Name', relief=RIDGE, bg="skyblue",fg="black",width="20")
customer_name_lable.place(x=5,y=170)

customer_name_entry = Entry(textvariable=customerName,width="23")
customer_name_entry.place(x=172,y=170)

bill_no_label = Label(text='Bill-NO',relief=RIDGE, bg="skyblue",fg="black")
bill_no_label.place(x=380,y=149)

bill_no_entry = Entry(textvariable=billno,width="5")
bill_no_entry.place(x=434,y=149)


date_label = Label(text='Date    ',relief=RIDGE, bg="skyblue",fg="black")
date_label.place(x=380,y=170)

date_entry = Entry(textvariable=date,width="12")
date_entry.place(x=434,y=170)


heading_label_name=["Item Name","Quantity","Price","Amount"]
width_list= [30,10,10,15]
x_list = [10,253,335,418]

for i in range(4):
    heading_label = Label(text=heading_label_name[i],relief=RIDGE, bg="skyblue",fg="black",width=width_list[i])
    heading_label.place(x=x_list[i],y=220)

def create_entry(variablename1,variablename2,variablename3,variablename4,x1,y1,x2,y2,x3,y3,x4,y4):
    item_name_entry = Entry(textvariable=variablename1,width=30)
    item_name_entry.place(x=x1,y=y1)

    Quantity_entry = Entry(textvariable = variablename2,width=10)
    Quantity_entry.place(x=x2,y=y2)

    price_entry = Entry(textvariable = variablename3,width=10)
    price_entry.place(x=x3,y=y3)

    amount_entry = Entry(textvariable = variablename4,width=15)
    amount_entry.place(x=x4,y=y4)

create_entry(itemName0,quantity0,price0,amount0,9,241,252,241,334,241,417,241)
create_entry(itemName1,quantity1,price1,amount1,9,264,252,264,334,264,417,264)
create_entry(itemName2,quantity2,price2,amount2,9,287,252,287,334,287,417,287)
create_entry(itemName3,quantity3,price3,amount3,9,310,252,310,334,310,417,310)




sub_total_label=Label(text="Sub Total",width="19",relief=RIDGE, bg="skyblue",fg="black",)
sub_total_label.place(x=255,y=357)


sub_total_entry=Text(state='disabled',width="15",height=1)
sub_total_entry.place(x=417,y=357)

# save = Button(text="Save",width=12,bg='goldenrod' ,fg="white",command = save_info)
# save.place(x=417,y=387)

# genrate_bill = Button(text="Genrate Bill",width="15",bg='maroon',fg="white",command=genratebill)
# genrate_bill.place(x=252,y=387)


side_label =Label(text = "Bill Review",font = ('arial',30),width=30,bg="green",fg='white')
side_label.place(x=602,y=150)






invoice_label = Label(width=82,bg='pink',height=5)
invoice_label.place(x=602,y=200)

def label(text_str,fg_clr,bg_clr,font_no,x,y):
    taxinvoice = Label(text=text_str,fg=fg_clr,bg=bg_clr,font=('arial',font_no))
    taxinvoice.place(x=x,y=y)


label("TAX INVOICE",'black','pink',15,880,230)
label("NO: ",'black','pink',10,1150,210)
label("001",'red','pink',10,1180,210)


textbox = Text(height=25, width=82)
textbox.place(x=602,y=280)




save = Button(text="Save",width=12,bg='goldenrod' ,fg="white",command = save_info)
save.place(x=417,y=387)


genrate_bill = Button(text="Genrate Bill",width="15",bg='maroon',fg="white",command=genratebill)
genrate_bill.place(x=252,y=387)


root.mainloop()


