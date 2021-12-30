import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建一个Label
var = tk.StringVar()   # 创建变量
l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

# 创建一个触发函数
def print_selection(v):
    l.config(text='you have selected ' + v)

# 创建一个Scale
s = tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval=2,resolution=0.01,command=print_selection)
s.pack()

window.mainloop()