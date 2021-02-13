from tkinter import *
from math import *
import random
import numpy as np
from Results import*

def start():
    root = Tk()
    root.geometry("525x695")
    root.title('Criss-cross')
    cross_count = 0

    def new_game():
        for row in range(3):
            for col in range(3):
                field[row][col]['text'] = ' '
                field[row][col]['background'] = 'white'
        global game_run
        game_run = True
        global cross_count
        cross_count = 0

    def click(row, col):
        if game_run and field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'X'
            global cross_count
            cross_count += 1
            check_win('X')
            if game_run and cross_count < 5:
                computer_move()
                check_win('O')

    def can_win(a1,a2,a3,smb):
        res = False
        if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
            a3['text'] = 'O'
            res = True
        if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
            a2['text'] = 'O'
            res = True
        if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
            a1['text'] = 'O'
            res = True
        return res

    def computer_move():
        for n in range(3):
            if can_win(field[n][0], field[n][1], field[n][2], 'O'):
                return
            if can_win(field[0][n], field[1][n], field[2][n], 'O'):
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'O'):
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'O'):
            return
        for n in range(3):
            if can_win(field[n][0], field[n][1], field[n][2], 'X'):
                return
            if can_win(field[0][n], field[1][n], field[2][n], 'X'):
                return
        if can_win(field[0][0], field[1][1], field[2][2], 'X'):
            return
        if can_win(field[2][0], field[1][1], field[0][2], 'X'):
            return
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if field[row][col]['text'] == ' ':
                field[row][col]['text'] = 'O'
                break

    for row in range(3):
        line = []
        for col in range(3):
            button = Button(root, text=' ', width=10, height=6, font=('Arial', 20), background='white', command=lambda row=row, col=col: click(row,col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_button = Button(root, text='Новая игра', command=new_game)
    new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
    root.mainloop()

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == 'O':
            winres = 'Вы проиграли!'
            res2 = 'Проигрыш'
        elif a1['text'] == 'X' and a2['text'] == 'X' and a3['text'] == 'X':
            winres = 'Вы выиграли!'
            res2 = 'Выигрыш'
        global game_run
        game_run = False
        if game_run == False:
            results_add(res2)
            victory=Tk()
            victory.title("Результат игры")
            victory.geometry("1440x800")
            results=Label(victory,text=winres, font="Arial 27" ,height=3)
            results.pack()
            victory.mainloop()

def ex():
    global win
    win.quit()

def rule():
    rules_win=Tk()
    rules_win.geometry("1280x800")
    ft=Label(rules_win, text="Правила игры Крестики-Нолики!\nПравила игры очень просты, вы играете против компьютера,\n вашей задачей является по очереди ставить на свободные клетки поля\n 3х3 знаки (один всегда крестики, другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры по вертикали,\n горизонтали или диагонали, выигрывает.\nПервый ход делает игрок, ставящий крестики.", font="Arial 27", height=7)
    ft.pack()
    rules_win.mainloop()

def results_check():
    res_win=Tk()
    res_win.mainloop()
    results_file=open("CrissCross/results.txt"), read()
    print(results_file)
    R = Text(res_win, height=15, width=60)
    R.pack()
    R.insert(END,results_file)
    res_win.mainloop()

field = []
game_run = True
cross_count = 0
wind=Tk()
wind.title("Крестики-Нолики")
wind.geometry("1440x800")
btn=Button(wind, command=start, text="Начать игру",fg="white", bg="grey", font="Arial 40", width=10)
rules=Button(wind, command=rule, text="Правила", fg="white", bg="grey", font="Arial 40", width=10)
lbl=Label(wind,text="Добро пожаловать в Крестики-Нолики!", font="Arial 27" ,height=3)
exit=Button(wind, command=ex, text="Выход", fg="white", bg="grey", font="Arial 40", width=10)
resu = Button(wind, command=results_check, text="Результаты", fg="white", bg="grey", font="Arial 40", width=10)
resu.grid(row=5, column=2)
exit.grid(row=1, column=2)
lbl.grid(row=0, column=1)
btn.grid(row=1, column=0)
rules.grid(row=1, column=1)
wind.mainloop()