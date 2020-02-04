from Tkinter import * 


def save_info():
  date_info = date.get()
  name_info = name.get()
  itemName_info = itemName.get()
  quantity_info = quantity.get()
  price_info = price.get()
  amount_info = amount.get()


  date_info = str(date_info)
  itemName_info = str(itemName_info)
  quantity_info = str(quantity_info)
  price_info = str(price_info)
  amount_info = str(amount_info)
  
  
  file = open("data.txt", "a+")
  file.write(date_info + '   ')
  file.write(name_info + '   ')
  file.write(itemName_info + '   ')
  file.write(quantity_info + '   ')
  file.write(price_info + '   ')
  file.write(amount_info + '\n' )



  file.close()
  print(" User ", name_info, " has been registered successfully")  

'''  firstname_entry.delete(0, END)
  lastname_entry.delete(0, END)
  age_entry.delete(0, END)'''  



sft = Tk()
sft.geometry("1000x1000")
sft.title("Business Data")
heading = Label(text = "Faiz cutpeace", bg = "purple", fg = "white", width = "300", height = "2")
heading.pack()



date_text = Label(text="Date ")
name_text = Label(text="Name ")
item_name_text = Label(text="item name ")
qty_text = Label(text="Quantity ")
price_text = Label(text="Price ")
amount_text = Label(text="Total Amount ")



date_text.place(x= 780, y=70)
name_text.place(x= 40, y=140)
item_name_text.place(x= 330, y=140)
qty_text.place(x= 610, y=140)
price_text.place(x= 750, y=140)
amount_text.place(x= 750, y=180)



date = IntVar()
name = StringVar()
itemName = StringVar()
quantity = IntVar()
price = IntVar()
amount = IntVar()



date_entry = Entry(textvariable = date, width = "20")
name_entry = Entry(textvariable = name, width = "20")
itemName_entry = Entry(textvariable = itemName, width = "20")
quantity_entry = Entry(textvariable = quantity, width = "5")
price_entry = Entry(textvariable = price, width = "10")
amount_entry = Entry(textvariable = amount, width = "15")



date_entry.place(x=820,y=70)
name_entry.place(x=85,y=140)
itemName_entry.place(x=410,y=140)
quantity_entry.place(x=675,y=140)
price_entry.place(x=790,y=140)
amount_entry.place(x=845,y=180)

save = Button(sft,text = "Save", width = "30", height = "2", command = save_info, bg = "grey")
save.place(x = 650, y = 250)



sft.mainloop()
