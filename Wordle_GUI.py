import tkinter as tk
from Wordle import *
import time

count =0
words = get_words()
temp_words=words
wordle_word = get_random_word(words)
print("Answer : "+wordle_word)

box_bg_color="white"
box_fg_color="black"

HEIGHT = 600
WIDTH = 700
CENTER = 'center'

colors=["grey","yellow","green"]

def orginal(type_word,wordle_word):
    if(type_word==wordle_word):
        result_label.configure(text = "You Guessed Correct Word")
def print_recommended_words(words):
    recommended_words=""
    try:
        for i in range(7):
            recommended_words=recommended_words+words[i].upper()+"\n"
    except:
        print()
    recommended_words=recommended_words[0:-1]
    recommend_words_label.configure(text=recommended_words)
    

def Wordle():
    global count
    global words
    global temp_words
    global wordle_word
    print(words.count("niese"))
    if(count==0):
        type_word=first_row_0.get()+first_row_1.get()+first_row_2.get()+first_row_3.get()+first_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            first_row_0.configure(bg=colors[pattern[0]])
            first_row_0.configure(fg='white')
            first_row_1.configure(bg=colors[pattern[1]])
            first_row_1.configure(fg='white')
            first_row_2.configure(bg=colors[pattern[2]])
            first_row_2.configure(fg='white')
            first_row_3.configure(bg=colors[pattern[3]])
            first_row_3.configure(fg='white')
            first_row_4.configure(bg=colors[pattern[4]])
            first_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
            else:
                result_label.config(text = "Enter Your Second Guess")
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")
    elif(count==1):
        type_word=second_row_0.get()+second_row_1.get()+second_row_2.get()+second_row_3.get()+second_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            second_row_0.configure(bg=colors[pattern[0]])
            second_row_0.configure(fg='white')
            second_row_1.configure(bg=colors[pattern[1]])
            second_row_1.configure(fg='white')
            second_row_2.configure(bg=colors[pattern[2]])
            second_row_2.configure(fg='white')
            second_row_3.configure(bg=colors[pattern[3]])
            second_row_3.configure(fg='white')
            second_row_4.configure(bg=colors[pattern[4]])
            second_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
                print_recommended_words(["You completed","game in "+ str(count+1)+" steps"])
            else:
                result_label.config(text = "Enter Your Third Guess")
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")
    elif(count==2):
        type_word=third_row_0.get()+third_row_1.get()+third_row_2.get()+third_row_3.get()+third_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            third_row_0.configure(bg=colors[pattern[0]])
            third_row_0.configure(fg='white')
            third_row_1.configure(bg=colors[pattern[1]])
            third_row_1.configure(fg='white')
            third_row_2.configure(bg=colors[pattern[2]])
            third_row_2.configure(fg='white')
            third_row_3.configure(bg=colors[pattern[3]])
            third_row_3.configure(fg='white')
            third_row_4.configure(bg=colors[pattern[4]])
            third_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
                print_recommended_words(["You completed","game in "+ str(count)+"steps"])
            else:
                result_label.config(text = "Enter Your Fourth Guess")
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")
    elif(count==3):
        type_word=fourth_row_0.get()+fourth_row_1.get()+fourth_row_2.get()+fourth_row_3.get()+fourth_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            fourth_row_0.configure(bg=colors[pattern[0]])
            fourth_row_0.configure(fg='white')
            fourth_row_1.configure(bg=colors[pattern[1]])
            fourth_row_1.configure(fg='white')
            fourth_row_2.configure(bg=colors[pattern[2]])
            fourth_row_2.configure(fg='white')
            fourth_row_3.configure(bg=colors[pattern[3]])
            fourth_row_3.configure(fg='white')
            fourth_row_4.configure(bg=colors[pattern[4]]) 
            fourth_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
                print_recommended_words(["You completed","game in "+ str(count)+"steps"])
            else:
                result_label.config(text = "Enter Your Fifth Guess")
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")
    elif(count==4):
        type_word=fifth_row_0.get()+fifth_row_1.get()+fifth_row_2.get()+fifth_row_3.get()+fifth_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            fifth_row_0.configure(bg=colors[pattern[0]])
            fifth_row_0.configure(fg='white')
            fifth_row_1.configure(bg=colors[pattern[1]])
            fifth_row_1.configure(fg='white')
            fifth_row_2.configure(bg=colors[pattern[2]])
            fifth_row_2.configure(fg='white')
            fifth_row_3.configure(bg=colors[pattern[3]])
            fifth_row_3.configure(fg='white')
            fifth_row_4.configure(bg=colors[pattern[4]])
            fifth_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
                print_recommended_words(["You completed","game in "+ str(count)+"steps"])
            else:
                result_label.config(text = "Enter Your Sixth Guess")
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")
    elif(count==5):
        type_word=sixth_row_0.get()+sixth_row_1.get()+sixth_row_2.get()+sixth_row_3.get()+sixth_row_4.get()
        type_word=type_word.lower()
        if type_word in temp_words:
            pattern = compute_pattern(wordle_word,type_word)
            sixth_row_0.configure(bg=colors[pattern[0]])
            sixth_row_0.configure(fg='white')
            sixth_row_1.configure(bg=colors[pattern[1]])
            sixth_row_1.configure(fg='white')
            sixth_row_2.configure(bg=colors[pattern[2]])
            sixth_row_2.configure(fg='white')
            sixth_row_3.configure(bg=colors[pattern[3]])
            sixth_row_3.configure(fg='white')
            sixth_row_4.configure(bg=colors[pattern[4]])
            sixth_row_4.configure(fg='white')
            if(type_word==wordle_word):
                result_label.configure(text = "You Guessed Correct Word")
                print_recommended_words(["You completed","game in "+ str(count)+"steps"])
            else:
                result_label.config(text = "Sorry, Answer : "+wordle_word)
                hashed_words=compute_hashed_words_with_same_pattern(pattern,type_word,words)
                words=hashed_words
                print_recommended_words(words)
                count=count+1
        else:
            result_label.config(text = "Renter,It is not English word")    
root = tk.Tk()
tk.Tk.title(root, "Welcome ")

canvas_1 = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas_1.pack()

frame = tk.Frame(root, bg='#e6e6e6')
frame.place(relx=0, rely=0, relheight=1, relwidth=2, anchor='n')

label = tk.Label(frame, text="Wordle",bg='#ffccff', font=('Courier Prime', 24, 'bold'), fg='black')
label.place(relx=0.75, rely=0,relheight=0.14, relwidth=0.6, anchor='n')

left_frame = tk.Frame(root, bg='skyblue', bd=10)
left_frame.place(relx=0, rely=0.15, relheight=0.6775, relwidth=1.25, anchor='n')

first_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
first_row_0.focus_force()
first_row_0.place(relx=0.52, rely=0, relheight=0.125, relwidth=0.075, anchor='nw')

first_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
first_row_1.place(relx=0.615, rely=0, relheight=0.125, relwidth=0.075, anchor='nw')

first_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
first_row_2.place(relx=0.71, rely=0, relheight=0.125, relwidth=0.075, anchor='nw')

first_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
first_row_3.place(relx=0.805, rely=0, relheight=0.125, relwidth=0.075, anchor='nw')

first_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
first_row_4.place(relx=0.9, rely=0, relheight=0.125, relwidth=0.075, anchor='nw')

second_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
second_row_0.place(relx=0.52, rely=0.15, relheight=0.125, relwidth=0.075, anchor='nw')

second_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
second_row_1.place(relx=0.615, rely=0.15, relheight=0.125, relwidth=0.075, anchor='nw')

second_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
second_row_2.place(relx=0.71, rely=0.15, relheight=0.125, relwidth=0.075, anchor='nw')

second_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
second_row_3.place(relx=0.805, rely=0.15, relheight=0.125, relwidth=0.075, anchor='nw')

second_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
second_row_4.place(relx=0.9, rely=0.15, relheight=0.125, relwidth=0.075, anchor='nw')

third_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
third_row_0.place(relx=0.52, rely=0.3, relheight=0.125, relwidth=0.075, anchor='nw')

third_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
third_row_1.place(relx=0.615, rely=0.3, relheight=0.125, relwidth=0.075, anchor='nw')

third_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
third_row_2.place(relx=0.71, rely=0.3, relheight=0.125, relwidth=0.075, anchor='nw')

third_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
third_row_3.place(relx=0.805, rely=0.3, relheight=0.125, relwidth=0.075, anchor='nw')

third_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
third_row_4.place(relx=0.9, rely=0.3, relheight=0.125, relwidth=0.075, anchor='nw')

fourth_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fourth_row_0.place(relx=0.52, rely=0.45, relheight=0.125, relwidth=0.075, anchor='nw')

fourth_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fourth_row_1.place(relx=0.615, rely=0.45, relheight=0.125, relwidth=0.075, anchor='nw')

fourth_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fourth_row_2.place(relx=0.71, rely=0.45, relheight=0.125, relwidth=0.075, anchor='nw')

fourth_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fourth_row_3.place(relx=0.805, rely=0.45, relheight=0.125, relwidth=0.075, anchor='nw')

fourth_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fourth_row_4.place(relx=0.9, rely=0.45, relheight=0.125, relwidth=0.075, anchor='nw')

fifth_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fifth_row_0.place(relx=0.52, rely=0.6, relheight=0.125, relwidth=0.075, anchor='nw')

fifth_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fifth_row_1.place(relx=0.615, rely=0.6, relheight=0.125, relwidth=0.075, anchor='nw')

fifth_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fifth_row_2.place(relx=0.71, rely=0.6, relheight=0.125, relwidth=0.075, anchor='nw')

fifth_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fifth_row_3.place(relx=0.805, rely=0.6, relheight=0.125, relwidth=0.075, anchor='nw')

fifth_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
fifth_row_4.place(relx=0.9, rely=0.6, relheight=0.125, relwidth=0.075, anchor='nw')

sixth_row_0 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
sixth_row_0.place(relx=0.52, rely=0.75, relheight=0.125, relwidth=0.075, anchor='nw')

sixth_row_1 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
sixth_row_1.place(relx=0.615, rely=0.75, relheight=0.125, relwidth=0.075, anchor='nw')

sixth_row_2 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
sixth_row_2.place(relx=0.71, rely=0.75, relheight=0.125, relwidth=0.075, anchor='nw')

sixth_row_3 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
sixth_row_3.place(relx=0.805, rely=0.75, relheight=0.125, relwidth=0.075, anchor='nw')

sixth_row_4 = tk.Entry(left_frame, bg=box_bg_color,justify=CENTER, font=('Microsoft Sans Serif', 16 , 'bold'), fg=box_fg_color)
sixth_row_4.place(relx=0.9, rely=0.75, relheight=0.125, relwidth=0.075, anchor='nw')

word_button = tk.Button(left_frame, bg='#A7BCD8', text="Submit", font=('Microsoft Sans Serif', 16 , 'bold'),command=lambda:Wordle())
word_button.place(relx=0.622, rely=0.9, relheight=0.120, relwidth=0.25, anchor='nw')

right_frame = tk.Frame(root, bg='black', bd=10)
right_frame.place(relx=1.005, rely=0.15, relheight=0.6775, relwidth=0.75, anchor='n')

recommend_label = tk.Label(right_frame,text="Recommended\nWords", font=('Microsoft Sans Serif', 16,'bold') , bg = 'black' , fg='orange' )
recommend_label.place(relx=0.0, rely=0, relheight=0.125, relwidth=0.5)

recommend_words_label = tk.Label(right_frame, font=('Microsoft Sans Serif', 13,'bold') , bg = 'black' , fg='white' )
recommend_words_label.place(relx=0.0, rely=0.13, relheight=0.75, relwidth=0.5)

result_label = tk.Label(frame, text="", font=('Courier Prime', 24, 'bold'),bg = "#ffccff", fg='black')
result_label.place(relx=0.75, rely=0.84,relheight=0.16, relwidth=0.6, anchor='n')

result_label.config(text = "Enter Your First Guess")
