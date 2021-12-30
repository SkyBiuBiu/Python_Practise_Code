import tkinter as tk

# 初始化一个windows对象。
window = tk.Tk()
# 窗口框架
window.title("My window") # 窗口标题
window.geometry('200x100') # 窗口大小，宽x高


# 文字变量储存器对象
text_var = tk.StringVar()
# 创建Label
l = tk.Label(window,textvariable=text_var,bg='orange',font=('Mircosoft YaHei',12),width=15,height=2)
# 安置这个Label对象，除了pack方法还有其它的方法可以安置Label对象，如place方法。
l.pack()


# 定义一个 hit_me()函数
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        text_var.set('you hit me')
    else:
        on_hit = False
        text_var.set('')

# 创建Button
b = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
# 安置Button对象
b.pack()

# 窗口主循环
window.mainloop()