from tkinter import *

def results_add(rs):
    results_file=open("CrissCross/results.txt",'w')
    results_file.write(rs + '\n')
    results_file.close()