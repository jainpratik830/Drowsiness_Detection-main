from tkinter import *
import tkinter.font as font
import random
from time import sleep
num1 = []
num2 = []

for i in range(101):
    num1.append(str(i))
    num2.append(str(i))

# print(num1)
timer = 30
score = 0
displayed_num1 = ''
displayed_num2 = ''

def game():
  
  #This fuction will be called when start button is clicked

    def startGame():
        global displayed_num1
        global displayed_num2
        if(timer == 30):
            color_entry['state']='normal'
            startCountDown()
            displayed_num1 = random.choice(num1)
            displayed_num2 = random.choice(num2)
            # sum_sign= '+'
            display_words1.config(text=displayed_num1, fg="white")
            display_words2.config(text=displayed_num2, fg="white")
            sum_sign.config(text='+', fg="white")
            color_entry.bind('<Return>', displayNextWord)
            # print("helo")
            # start_button["state"]="disabled"
            
   #This function is to reset the game
    
    def resetGame():
        global timer, score, displayed_num1, displayed_num2
        timer = 30
        score = 0
        displayed_num1 = ''
        displayed_num2 = ''
        color_entry['state']='normal'
        # # print("helo")
        # start_button["state"]="active"
        game_score.config(text = "Your Score : " + str(score))
        display_words1.config(text = '')
        sum_sign.config(text='+', fg="white")
        display_words2.config(text='')
        time_left.config(text="Game Ends in : -")
        color_entry.delete(0, END)
        if(timer == 30):
            color_entry['state']='normal'
            # startCountDown()
            displayed_num1 = random.choice(num1)
            displayed_num2 = random.choice(num2)
            # sum_sign= '+'
            display_words1.config(text=displayed_num1, fg="white")
            display_words2.config(text=displayed_num2, fg="white")
            sum_sign.config(text='+', fg="white")
            color_entry.bind('<Return>', displayNextWord)
        # startGame()


    def startCountDown():
        global timer
        if(timer >= 0):
            time_left.config(text = "Game Ends in : " + str(timer) + "s")
            timer -= 1
            time_left.after(1000,startCountDown)
            if (timer == -1):
                if(score>=6):
                    time_left.config(text="Well done, you can continue with your work!!!", fg="light green")
                else:  
                    color_entry['state']='disable'
                    time_left.config(text="Oops,your score was too low\n Press the reset button and try again!", fg="red")

 #This function to display random words

    def displayNextWord(event):
        global displayed_num1
        global displayed_num2
        global score
        if(timer > 0):
            if(int(displayed_num1) + int(displayed_num2) == int(color_entry.get().lower())):
                score += 1
                game_score.config(text = "Your Score : " + str(score))
            color_entry.delete(0, END)
            displayed_num1 = random.choice(num1)
            displayed_num2 = random.choice(num2)
            display_words1.config(text=displayed_num1, fg="white")
            display_words2.config(text=displayed_num2, fg="white")
            



    

    my_window = Tk()
    my_window.title("Number Quiz")
    my_window.geometry("500x200")
    my_window.config(bg= "#001a33")
    app_font = font.Font(family='Helvetica', size = 16)
    game_desp = "Enter the sum of the following. \nTwo numbers and Press Enter"
    myFont = font.Font(family='Helvetica')
    game_description = Label(my_window, text = game_desp, font = app_font, fg= "light blue", bg="#001a33")
    game_description.pack()
    game_score = Label(my_window, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "light blue", bg="#001a33")
    game_score.pack()
    display_words1 = Label(my_window , font = (font.Font(size=28)), pady = 10, bg="#001a33")
    display_words2 = Label(my_window , font = (font.Font(size=28)), pady = 10, bg="#001a33")
    sum_sign = Label(my_window , font = (font.Font(size=28)), pady = 0, bg="#001a33")
    
    display_words1.pack()
    sum_sign.pack()
    display_words2.pack()
    time_left = Label(my_window, text = "Game Ends in : -", font = (font.Font(size=16)), fg = "light blue" ,bg="#001a33")
    time_left.pack()
    color_entry = Entry(my_window, width = 30,state='disabled')
    color_entry.pack(pady = 5)
    btn_frame = Frame(my_window, width= 80, height = 20, bg= 'red')
    btn_frame.pack(side = BOTTOM)
    start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "light blue", bd = 2,padx = 20, pady = 10 , command = startGame)
    start_button.grid(row=0, column= 0)
    reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 2,padx = 20, pady = 10 , command = resetGame)
    reset_button.grid(row=0, column= 1)
    my_window.geometry('600x450')
    my_window.mainloop()







