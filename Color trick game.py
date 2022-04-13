from tkinter import*
import random
root=Tk()
root.title("Encapsulation")
root.geometry("600x600")

color_l=Label(root,font=('times bold',30))
color_l.place(relx=0.4,rely=0.4,anchor=CENTER)

class Game():
    def __init__(self):
        self.score=0
    
    def update_game(self):
            self.color_name=["blue","aqua","green","yellow","red","pink","purple","black"]
            self.random_color=random.randint(0,7)
            
            self.color_text=["Blue","Aqua","Green","Yellow","Red","Pink","Purple","Black"]
            self.random_text=random.randint(0,7)
            
            color_l['text']=self.color_text[self.random_text]
            color_l['fg']=self.color_text[self.random_color]
            
            btn1['text']="Next"
            
obj_game=Game()

btn1=Button(root,text="Start",command=obj_game.update_game)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()