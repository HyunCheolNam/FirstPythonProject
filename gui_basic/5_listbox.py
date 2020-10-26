from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
#selectmode 는 extended는 여러개 선택 single은 하나 
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()


def btncmd():
    #listbox.delete(END)) #맨 뒤에 항목을 삭제, 0으로 설정하면 맨 앞에 항목 삭제
    
    #갯수 확인
    #print("리스트에는",listbox.size(), "개가 있어요")

    #항목 확인 get(시작인덱스,끝인덱스)
    #print("1번째부터 3번재까지의 항목 : ", listbox.get(0,2))

    #선택된 항목 확인(위치로 반환 (ex) 1,2,3)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root,text="클릭", command=btncmd)
btn.pack()

root.mainloop()