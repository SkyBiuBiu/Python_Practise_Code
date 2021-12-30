import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建一个label
l = tk.Label(window,text='',bg='yellow')
l.pack()

# 创建一个事件
counter = 0
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1

# 创建一个menubar
menubar = tk.Menu(window)
# 创建一个Filemenu，并为它添加控件
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
# 分割线
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)
# 子菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)


# 创建一个Editmenu，并为它添加控件
editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

# 将menubar放进window
window.config(menu=menubar)

window.mainloop()