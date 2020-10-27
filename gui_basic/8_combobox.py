import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로

values= [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root,height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록의 제목 설정

readonly_combobox = ttk.Combobox(root,height=5, values=values, state ="readonly")
readonly_combobox.current(0) #0번째 인덱스값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())

btn = Button(root,text="선택", command=btncmd)
btn.pack()

root.mainloop()