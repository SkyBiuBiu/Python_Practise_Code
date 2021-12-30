import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x250')

# 定义事件
def showinfo_box():
    tkinter.messagebox.showinfo(title='showinfo', message='showinfo')

# 放置按钮
tk.Button(window,text='showinfo_box',command=showinfo_box).pack()
#tk.Button(window,text='showwarning_box',command=None).pack()
#tk.Button(window,text='showerror_box',command=None).pack()
#tk.Button(window,text='askquestion_box',command=None).pack()
#tk.Button(window,text='askretrycancel_box',command=None).pack()
#tk.Button(window,text='askyesno_box',command=None).pack()
#tk.Button(window,text='askyesnocancel_box',command=None).pack()


window.mainloop()


