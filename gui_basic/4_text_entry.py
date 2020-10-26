from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

#엔트리는 엔터를 못한다 그래서 로그인창에서 아이디나 비밀번호를 입력받을때 쓰면 좋다
#텍스트는 엔터키 입력가능.
txt = Text(root, width = 30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0,"한줄만 입력가능합니다")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1은 첫번쨰라인을 의미, 0은 0번쨰 컬럼 위치를 의미
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()