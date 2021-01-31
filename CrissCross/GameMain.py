from tkinter import *
import random
from CrissCross import *
game = True
field = []
cross = 0

def click(row, col):
    if game and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        crosst += 1
        win('X')
        if game and cross < 5:
            computer()
            check('O')

def win(symbol):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], symbol)
        check_line(field[0][n], field[1][n], field[2][n], symbol)
    check_line(field[0][0], field[1][1], field[2][2], symbol)
    check_line(field[2][0], field[1][1], field[0][2], symbol)

def chance(a1,a2,a3,symbol):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == symbol:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == symbol:
        a1['text'] = 'O'
        res = True
    return res

def computer():
    for n in range(3):
        if chance(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if chance(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if chance(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if chance(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if chance(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if chance(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if chance(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if chance(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
def line(a1,a2,a3,smb):
    if a1['text'] == symbol and a2['text'] == symbol and a3['text'] == symbol:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game
        game = False

for row in range(3):
    line = []
    for col in range(3):
        button = Button(wind, text=' ', width=4, height=2, font=('Arial', 20), background='white', command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
newgame = Button(wind, text='Новая игра', command=start)
newgame.grid(row=3, column=0, columnspan=3, sticky='nsew')