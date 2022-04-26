from tkinter import*
import random
root=Tk()
root.title("Encapsulation")
root.geometry("600x600")

color_l=Label(root,font=('times bold',30))
color_l.place(relx=0.4,rely=0.4,anchor=CENTER)
score_l=Label(root,text="Score:0",font=('times bold',20))
score_l.place(relx=0.1,rely=0.05,anchor=CENTER)
input_value=Entry(root)

class Game():
    def __init__(self):
        self.score=0
    
    def update_game(self):
            self.color_name=["blue","aqua","green","yellow","red","pink","purple","black"]
            self.random_color=random.randint(0,7)
            
            self.color_text=["Blue","Aqua","Green","Yellow","Red","Pink","Purple","Black"]
            self.random_text=random.randint(0,7)
            
            color_l['text']=self.color_text[self.random_text]
            color_l['fg']=self.color_name[self.random_color]
            
            btn1['text']="Next"
            
    def __update_score(self,input_value):
        if input_value==self.color_name[self.random_color]:
            self.score+=random.randint(1,10)
            score_l['text']="Score: "+self.score
            
    def get_user_value(self,input_value):
        __update_score(self,input_value)
        
obj_game=Game()
def getInput() :
    output=input_value.get()
    obj_game.get_user_value(output)
    obj_game.update_score()
    input_value.delete(0,END)
            
obj_game=Game()

btn1=Button(root,text="Start",command=getInput,relief=FLAT)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()