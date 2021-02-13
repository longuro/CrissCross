from tkinter import *
from math import *
import random
from GameCode import *

def ex():
    global win
    win.quit()

def rule():
    rules_win=Tk()
    rules_win.geometry("1280x800")
    ft=Label(rules_win, text="Правила игры Крестики-Нолики!\nПравила игры очень просты, вы играете против компьютера,\n вашей задачей является по очереди ставить на свободные клетки поля\n 3х3 знаки (один всегда крестики, другой всегда нолики).\nПервый, выстроивший в ряд 3 своих фигуры по вертикали,\n горизонтали или диагонали, выигрывает.\nПервый ход делает игрок, ставящий крестики.", font="Arial 27", height=7)
    ft.pack()
    rules_win.mainloop()

wind=Tk()
wind.title("Крестики-Нолики")
wind.geometry("1440x800")
btn=Button(wind, command=start, text="Начать игру",fg="white", bg="grey", font="Arial 40", width=10)
rules=Button(wind, command=rule, text="Правила", fg="white", bg="grey", font="Arial 40", width=10)
lbl=Label(wind,text="Добро пожаловать в Крестики-Нолики!", font="Arial 27" ,height=3)
exit=Button(wind, command=ex, text="Выход", fg="white", bg="grey", font="Arial 40", width=10)
exit.grid(row=1, column=2)
lbl.grid(row=0, column=1)
btn.grid(row=1, column=0)
rules.grid(row=1, column=1)
wind.mainloop()