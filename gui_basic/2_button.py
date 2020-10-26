from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정

btn1 = Button(root, text="버튼1")
btn1.pack() #pack()을 호출 해줘야만 윈도우에 포함이됨.

btn2 = Button(root, padx=5, pady=10, text="버튼2222222")# padx, pady 는 버튼의 크기 설정
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼44444444444") # width, height 로 버튼 크기를 설정하면 불변
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btnnmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btnnmd)
btn7.pack()

root.mainloop()