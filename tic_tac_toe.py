from tkinter import *
import random
import tkinter.messagebox
from functools import partial

#global variables
window = Tk()
player1 = 'X'
computer = 'O'
button1 = ' '
button2 = ' '
button3 = ' '
button4 = ' '
button5 = ' '
button6 = ' '
button7 = ' '
button8 = ' '
button9 = ' '
F = ' '
buttonPlayerWin = ' '
x = True

#declaring window size and background
window.minsize(600, 600)
window.maxsize(600, 600)
window.configure(background='black')

#creates individual buttons for the board/
#title and frame the game is in
def Main():
    
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global F
    
    box = Label(window, text="TIC-TAC-TOE", font=('Arial', '20', '''bold'''),\
                bg='black', fg='darkturquoise')
    box.pack()

    F = Frame(window)
    F.pack()
    
#top left
    button1 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button1'))
    button1.grid(row=1, column=0, sticky=S+N+E+W)
#top center
    button2 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button2'))
    button2.grid(row=1, column=1, sticky=S+N+E+W)
#top right
    button3 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button3'))
    button3.grid(row=1, column=2, sticky=S+N+E+W)
#mid left
    button4 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button4'))
    button4.grid(row=2, column=0, sticky=S+N+E+W)
#center
    button5 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button5'))
    button5.grid(row=2, column=1, sticky=S+N+E+W)
#mid right
    button6 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button6'))
    button6.grid(row=2, column=2, sticky=S+N+E+W)
#bottom left
    button7 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button7'))
    button7.grid(row=3, column=0, sticky=S+N+E+W)
#bottom middle
    button8 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button8'))
    button8.grid(row=3, column=1, sticky=S+N+E+W)
#bottom right
    button9 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button9'))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

#--------------------------------------------------------------------------------------------------
#declares winner and displays button to play again
def winner(name):
    global buttonPlayerWin
    global F
    F.destroy() #destroy window(frame)
    F = Frame(window) #create new window
    F.pack()
    buttonPlayerWin = Button(F, text=name\
    + '\n [click here to\n play again]', \
    font=('Arial 45 bold'), height=500, width=500, \
    command = partial(reset_board), bg='black', fg='darkorchid')
    buttonPlayerWin.pack()

#---------------------------------------------------------------------------------------------------
#declares possible outcomes for different wins (both x and o)
def buttons():
    global F
    global x

#outcome for player    
    if(button1['text'] == 'X' and button2['text'] == 'X' and\
       button3['text'] == 'X') or \
    \
         (button1['text'] == 'X' and button5['text'] == 'X' and\
          button9['text'] == 'X') or \
    \
         (button1['text'] == 'X' and button4['text'] == 'X' and\
          button7['text'] == 'X') or \
    \
         (button4['text'] == 'X' and button5['text'] == 'X' and\
          button6['text'] == 'X') or \
    \
         (button7['text'] == 'X' and button8['text'] == 'X' and\
          button9['text'] == 'X') or \
    \
         (button3['text'] == 'X' and button5['text'] == 'X' and\
          button7['text'] == 'X') or \
    \
         (button2['text'] == 'X' and button5['text'] == 'X' and\
          button8['text'] == 'X') or \
    \
         (button3['text'] == 'X' and button6['text'] == 'X' and\
          button9['text'] == 'X' ):
        x = False #indicates that the game is over
        window.after(400, winner,'YOU WON!')

#outcome for computer       
    elif(button1['text'] == 'O' and button2['text'] == 'O' and\
         button3['text'] == 'O') or \
    \
         (button1['text'] == 'O' and button5['text'] == 'O' and\
          button9['text'] == 'O') or \
    \
         (button1['text'] == 'O' and button4['text'] == 'O' and\
          button7['text'] == 'O') or \
    \
         (button4['text'] == 'O' and button5['text'] == 'O' and\
          button6['text'] == 'O') or \
    \
         (button7['text'] == 'O' and button8['text'] == 'O' and\
          button9['text'] == 'O') or \
    \
         (button3['text'] == 'O' and button5['text'] == 'O' and\
          button7['text'] == 'O') or \
    \
         (button2['text'] == 'O' and button5['text'] == 'O' and\
          button8['text'] == 'O') or \
    \
         (button3['text'] == 'O' and button6['text'] == 'O' and\
          button9['text'] == 'O' ):
             x = False #indicates that the game is over
             window.after(400, winner,'COMPUTER WON!')
             
#outcome for no winner     
    elif(button1['text'] != ' ' and \
        button2['text'] != ' ' and \
        button3['text'] != ' ' and \
        button4['text'] != ' ' and \
        button5['text'] != ' ' and \
        button6['text'] != ' ' and \
        button7['text'] != ' ' and \
        button8['text'] != ' ' and \
        button9['text'] != ' '):
        x = False #indicates that the game is over
        window.after(400, winner,'NO ONE WON!')

#-------------------------------------------------------------------------------------------------- 
def place_move(button):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global x

    if button == 'button1':
        button1.configure(text='X', fg='darkturquoise', command=' ') 

    elif button == 'button2':
         button2.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button3':
         button3.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button4':
        button4.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button5':
        button5.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button6':
        button6.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button7':
        button7.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button8':
        button8.configure(text='X', fg='darkturquoise', command=' ')

    elif button == 'button9':
        button9.configure(text='X', fg='darkturquoise', command=' ')

#checking for end of game          
    buttons()
    if (x): #checking if game hasn't ended
        computer_move() #computer moves if game is still going

#----------------------------------------------------------------------------------------------------
#function to allow computer to move
def computer_move():
    board = [button1, button2, button3, button4,\
             button5, button6, button7, button8, button9]
    tempButton = random.choice(board)
    
#lets computer take its turn anywhere
#except where a move hasn't been played
    while tempButton['text'] != ' ':
        tempButton = random.choice(board)

    tempButton.configure(text='O', fg='darkorchid', command=' ')
    buttons() #checking for end of game

#---------------------------------------------------------------------------------------------------
#function that 'redraws' the board
def reset_board():
    #define global variables
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global buttonPlayerWin
    global x

    #'delete' winning display to redraw the board
    buttonPlayerWin.destroy()
    
    #to redeclare
    x = True

#top left 
    button1 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button1'))
    button1.grid(row=1, column=0, sticky=S+N+E+W)
#top middle
    button2 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button2'))
    button2.grid(row=1, column=1, sticky=S+N+E+W)
#top right
    button3 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button3'))
    button3.grid(row=1, column=2, sticky=S+N+E+W)
#mid left
    button4 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button4'))
    button4.grid(row=2, column=0, sticky=S+N+E+W)
#center
    button5 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button5'))
    button5.grid(row=2, column=1, sticky=S+N+E+W)
#mid right
    button6 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button6'))
    button6.grid(row=2, column=2, sticky=S+N+E+W)
#bottom left
    button7 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button7'))
    button7.grid(row=3, column=0, sticky=S+N+E+W)
#bottom middle
    button8 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button8'))
    button8.grid(row=3, column=1, sticky=S+N+E+W)
#bottom right
    button9 = Button(F, text=' ', font=('Arial 30 bold'),\
    height=3, width=6, command = partial(place_move, 'button9'))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

#---------------------------------------------------------------------------------------------------
#call Main function
Main()
























