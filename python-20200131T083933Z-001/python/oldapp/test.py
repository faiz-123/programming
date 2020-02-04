# from Tkinter import *

 
# window = Tk()
# window.title("List")
# window.geometry("700x450")
# window.configure(bg="orange red")
 
# #center this label
# Label (window, text="List", bg="orange red", fg="white", font="none 24 bold").grid(row=0, column=0)
 
 
# Label (window, text="Enter something here:", bg="orange red", fg="white", font="none 12 bold").grid(row=0, column=3, sticky=W)
 
name=['itemName1','itemName2','itemName3']

 
# window.mainloop()
variable_list=['itemName','quantity','price','amount']
name=[]
for i in range(4):
    a=[]
    for j in range(5):        
        a.append(variable_list[i]+str(j))
    name.append(a)        


print(name)