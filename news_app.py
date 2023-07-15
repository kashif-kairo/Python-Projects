import requests
from tkinter import *
from urllib.request import urlopen
from io import BytesIO
import webbrowser


from PIL import Image, ImageTk
class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=cd82295c6f5e46a5a3d6a2b7f6a1e3fc').json()
        print("Welcome To 2minNEWS")
        print("By MOHAMMAD KASHIF SIDDIQUI")
        self.load_gui()
        self.load_news_items(0)
        


        # initial GUI Load
    def load_gui(self):
        self.root = Tk()
        self.root.title("News App by Kashif")
        self.root.geometry("350x600")
        self.root.resizable(False, False)
        self.root.config(bg="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
        # load the list of news items
    def load_news_items(self, index):
        #clear the screen for the news items
        self.clear()

        # image loading

        img_url=self.data["articles"][index]["urlToImage"]
        raw_data = urlopen(img_url).read()
        im=Image.open(BytesIO(raw_data))
        im=im.resize((300,250))
        photo=ImageTk.PhotoImage(im)





        heading =Label(self.root, text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=("verdana",15))

        label=Label(self.root, image=photo)
        label.pack()

        details =Label(self.root, text=self.data["articles"][index]["description"],bg="black",fg="white",wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=("verdana",10))

        frame=Frame(self.root,bg="Black")
        frame.pack(expand= True, fill=BOTH)

        prev=Button(frame,text="Previous",width=16,height=3,bg="red",fg="white",command=lambda:self.load_news_items(index-1))
        # prev.config(font=("Arial", 8, "bold"))
        prev.pack(side=LEFT)
        

        read=Button(frame,text="Read More",width=16,height=3,bg="red",fg="white",command= lambda: webbrowser.open(self.data["articles"][index]["url"]))
        read.pack(side=LEFT)

        next=Button(frame,text="Next",width=16,height=3,bg="red",fg="white",command=lambda:self.load_news_items(index+1))
        next.pack(side=RIGHT)

        if index<=0:
            prev.configure(state=DISABLED)
        if index>=15:
            next.configure(state=DISABLED)


        self.root.mainloop()
    

obj=NewsApp()
