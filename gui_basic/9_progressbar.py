import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로

progressbar = ttk.Progressbar(root, maximum=100, mode ="indeterminate")
progressbar.start(10) # 10ms마다 움직임
progressbar.pack()


def btncmd():
    pass

btn = Button(root,text="선택", command=btncmd)
btn.pack()

root.mainloop()