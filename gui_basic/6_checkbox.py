from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로

chkvar = IntVar() #chkvar에 인트형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()#자동선택처리
chkbox.deselect()#선택 해제 처리
chkbox.pack()#팩은 필수

def btncmd():
    pass

btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()