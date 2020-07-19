# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 08:33:52 2020

@author: Emmanuel Alejandro Hurtado Alejandre Data 2A
"""
'''TIC-TAC-TOE'''
'''This game is only for 2 Human Players'''

'''Importing tkinter library'''
from tkinter import *
from tkinter import messagebox 
from tkinter import simpledialog

'''Method that blocks the buttons'''
def block():
    for i in range(0,9):
        button_list[i].config(state="disable") # Disables every button

''' Method that starts the game by cliking the "Start Game" button '''       
def start():
    for i in range(0,9):
        button_list[i].config(state="normal")  # Ables every button
        button_list[i].config(bg="lightgray")  # Change its colors
        button_list[i].config(text="")         # Pirnt nothing on they
        t[i] = "N"                             # Asing N value to Check Table

'''Method that change the turn and prints on the buttons the correspondent symbol'''
def change(num):                             # Recibes num
    global turno, P1, P2                     # Using global variables to can work
    if (t[num]=="N" and turno==0):           # If in Check Table posicion[num] is free and is turn of Player X
        button_list[num].config(text="X")    # In button_list posicion[num] print "X"
        button_list[num].config(bg="white")  # Change its color to white
        t[num] = "X"                         # Put in Check Table in posicion [num] an "X"
        turno = 1                            # Change turn 
        turnoPlayer.set("Turn: " + P2)       # Change turn to Player X 
  
    elif (t[num]=="N" and turno==1):             # If in Check Table posicion[num] is free and is turn of Player Y
        button_list[num].config(text="O")        # In button_list posicion[num] print "O"
        button_list[num].config(bg="lightblue")  # Change its color to lightblue
        t[num] = "O"                             # Put in Check Table in posicion [num] an "O"
        turno = 0                                # Change turn
        turnoPlayer.set("Turn: " + P1)           # Change turn to Player O
        
    button_list[num].config(state="disable")  # Disable the button  
    verify()                                  # Verify if someone won

'''Method that verifies when a Player wins the game'''   
def verify():
    global turno, P1, P2                   # Using global variables to can work
    # Player 1 Wins when:
    if (t[0]=="X" and t[1]=="X" and t[2]=="X") or (t[3]=="X" and t[4]=="X" and t[5]=="X") or (t[6]=="X" and t[7]=="X" and t[8]=="X"):
        block() 
        messagebox.showinfo("Winner!", "You won Player X!") # Won by Horizontal 
        turno = 0                                           # In the new game starts Player X
        turnoPlayer.set("Turn: " + P1)                      # Change turn to Player X 
        
    elif (t[0]=="X" and t[3]=="X" and t[6]=="X") or (t[1]=="X" and t[4]=="X" and t[7]=="X") or (t[2]=="X" and t[5]=="X" and t[8]=="X"):
        block()
        messagebox.showinfo("Winner!", "You won Player X!") # Won by Vertical
        turno = 0                                           # In the new game starts Player X 
        turnoPlayer.set("Turn: " + P1)                      # Change turn to Player X
        
    elif (t[0]=="X" and t[4]=="X" and t[8]=="X") or (t[2]=="X" and t[4]=="X" and t[6]=="X"):
        block()
        messagebox.showinfo("Winner!", "You won Player X!") # Won by Middle Cross
        turno = 0                                           # In the new game starts Player X
        turnoPlayer.set("Turn: " + P1)                      # Change turn to Player X
        
    # Player 2 Wins when:
    elif (t[0]=="O" and t[1]=="O" and t[2]=="O") or (t[3]=="O" and t[4]=="O" and t[5]=="O") or (t[6]=="O" and t[7]=="O" and t[8]=="O"):
        block()
        messagebox.showinfo("Winner!", "You won Player O!") # Won by Horizontal
        turno = 1                                           # In the new game starts Player O
        turnoPlayer.set("Turn: " + P2)                      # Change turn to Player O
        
    elif (t[0]=="O" and t[3]=="O" and t[6]=="O") or (t[1]=="O" and t[4]=="O" and t[7]=="O") or (t[2]=="O" and t[5]=="O" and t[8]=="O"):
        block()
        messagebox.showinfo("Winner!", "You won Player O!") # Won by Vertical
        turno = 1                                           # In the new game starts Player O
        turnoPlayer.set("Turn: " + P2)                      # Change turn to Player O
        
    elif (t[0]=="O" and t[4]=="O" and t[8]=="O") or (t[2]=="O" and t[4]=="O" and t[6]=="O"):
        block()
        messagebox.showinfo("Winner!", "You won Player O!") # Won by Middle Cross
        turno = 1                                           # In the new game starts Player O
        turnoPlayer.set("Turn: " + P2)                      # Change turn to Player O
        
window = Tk()                   # Creating window
window.geometry("400x500")      # Defining dimensions of window
window.title("Tic-Tac-Toe")     # Defining title of window
button_list = []                # Creating a list of buttons
t = [] # X O N                  # Creating Check Table
P1 = "Player X"                 # Player X string
P2 = "Player O"                 # Player O string
turnoPlayer = StringVar()       # Turn Player string

# Asking to users which one is going to start the game (Player X or Player O)
chose = simpledialog.askstring("Chose Order", "Press X to start as Player X  or Press O to start as Player O ")
if(chose=="X" or chose=="x"):
    turno = 0                            # Defining first turn for Player X
    turnoPlayer.set("Turn: " + P1)       # Turn to Player X
    
elif(chose=="O" or chose=="o"):
    turno = 1                            # Defining first turn for Player O
    turnoPlayer.set("Turn: " + P2)       # Turn to Player O

# Filling Check Table with "N"s
for i in range(0,9):                     
    t.append("N")

# Creating button0
boton0 = Button(window,width=9,height=3,command=lambda: change(0)) 
button_list.append(boton0)          # Adding buton0 to button_list
boton0.place(x=50, y=130)            # Placing button0 on window 

# Creating button1
boton1 = Button(window,width=9,height=3,command=lambda: change(1))
button_list.append(boton1)          # Adding buton1 to button_list
boton1.place(x=150, y=130)           # Placing button1 on window

# Creating button2
boton2 = Button(window,width=9,height=3,command=lambda: change(2))
button_list.append(boton2)          # Adding buton2 to button_list
boton2.place(x=250, y=130)           # Placing button2 on window

# Creating button3
boton3 = Button(window,width=9,height=3,command=lambda: change(3))
button_list.append(boton3)          # Adding buton3 to button_list
boton3.place(x=50, y=230)           # Placing button3 on window

# Creating button4
boton4 = Button(window,width=9,height=3,command=lambda: change(4))
button_list.append(boton4)          # Adding buton4 to button_list
boton4.place(x=150, y=230)          # Placing button4 on window

# Creating button5
boton5 = Button(window,width=9,height=3,command=lambda: change(5))
button_list.append(boton5)          # Adding buton5 to button_list
boton5.place(x=250, y=230)          # Placing button5 on window

# Creating button6
boton6 = Button(window,width=9,height=3,command=lambda: change(6))
button_list.append(boton6)          # Adding buton6 to button_list
boton6.place(x=50, y=330)           # Placing button6 on window

# Creating button7
boton7 = Button(window,width=9,height=3,command=lambda: change(7))
button_list.append(boton7)          # Adding buton7 to button_list
boton7.place(x=150, y=330)          # Placing button7 on window

# Creating button8
boton8 = Button(window,width=9,height=3,command=lambda: change(8))
button_list.append(boton8)          # Adding buton8 to button_list
boton8.place(x=250, y=330)          # Placing button8 on window

# Note: Lambda in this case allows calling Method "change" only if the button is pressed 

# Showing Title of the game
titleE = Label(window,text="Tic-Tac-Toe", font=("Arial Bold",30)).place(x=80, y= 30)

# Showing Players Turns 
turnE = Label(window,textvariable=turnoPlayer).place(x=150, y =85)

# Creating start button
start_boton = Button(window,bg='#006',fg='white',text='Start Game',width=15,height=3, command= start).place(x=130,y=425)
block()              # Blocks the buttton Until the  Start Game will be pressed 
window.mainloop()    # Loop that allows the window work

'''
References:
   Mokhtar Ebrahim: https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
   SProgramacion: https://www.youtube.com/watch?v=ZvbB2k398kw
'''