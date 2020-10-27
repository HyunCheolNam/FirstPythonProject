from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = StringVar() # int형으로 값을 저장
btn_burger1 = Radiobutton(root,text="햄버거", value="햄버거", variable=burger_var)
btn_burger2 = Radiobutton(root,text="치즈버거", value="치즈버거", variable=burger_var)
btn_burger3 = Radiobutton(root,text="치킨버거", value="치킨버거", variable=burger_var)


btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root,text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root,text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())


btn = Button(root,text="주문", command=btncmd)
btn.pack()

root.mainloop()