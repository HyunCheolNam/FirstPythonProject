import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀 이름 설정
root.geometry("640x480") # 가로 * 세로

#progressbar = ttk.Progressbar(root, maximum=100, mode ="indeterminate")
#progressbar.start(10) # 10ms마다 움직임
#progressbar.pack()


#def btncmd():
 #   progressbar.stop()

#btn = Button(root,text="선택", command=btncmd)
#btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length= 150,variable =p_var2 )
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)

        p_var2.set(i) #progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root,text="시작", command=btncmd2)
btn.pack()



root.mainloop()