import tkinter as tk

# 初始化一个windows对象。
window = tk.Tk()
# 窗口框架
window.title("My window") # 窗口标题
window.geometry('200x200') # 窗口大小，宽x高

# 创建一个输入框
e = tk.Entry(window,show='*')
e.pack()

# 插入到光标所在的位置
def insert_point():
    var = e.get()
    t.insert('insert',var)

# 插入到文本框的尾段
def insert_end():
    var = e.get()
    t.insert('end',var)

# 创建两个button，并添加事件
b1 = tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end',command=insert_end)
b2.pack()

# 创建一个文本框
t = tk.Text(window,height=2)
t.pack()

window.mainloop()