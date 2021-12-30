import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建Label控件
var = tk.StringVar()
l = tk.Label(window,bg="yellow",width=20,text="empty")
l.pack()

# 定义触发函数，将Label与Radiobutton联系起来
def print_selection():
    l.config(text='you have selected ' + var.get())


# 创建Radiobutton控件
r1 = tk.Radiobutton(window,text='Option A',variable=var,value="A",command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text='Option B',variable=var,value="B",command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text='Option C',variable=var,value="C",command=print_selection)
r3.pack()

window.mainloop()