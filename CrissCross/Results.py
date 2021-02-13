from tkinter import *

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        global game_run
        game_run = False

def winorlose(a1,a2,a3,smb,res):
    if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == 'O':
        res = 'Вы проиграли!'
    elif a1['text'] == 'X' and a2['text'] == 'X' and a3['text'] == 'X':
        res = 'Вы выиграли!'

if game_run == False:
    victory=Tk()
    victory.title("Результат игры")
    victory.geometry("1440x800")
    results=Label(victory,text=res, font="Arial 27" ,height=3)