from tkinter import *

class Application(object):
    def __init__(self,master):
        self.master =master
        self.top = Frame(master,height = 150 ,bg = '#fff2e6')
        self.top.pack(fill=X)

        self.bottom = Frame(master,height = 500,bg ='#0077b3')
        self.bottom.pack(fill=X)

        # self.top_image = PhotoImage(file ='/logo.png')
        # self.top_image_label =Label(self.top ,image=self.top_image)
        # self.top_image_label.place(x=20,y=50)


        self.heading = Label(self.top,text = 'Faiz Garments' ,font = 'Monospace 30 bold',bg ='#fff2e6',fg ='#663300')
        self.heading.place(x=200,y=50)







def main():
    root = Tk()
    app = Application(root)
    root.geometry("650x650")
    root.title("Business Data")
    root.mainloop()
    


if __name__ == "__main__":
    main()


