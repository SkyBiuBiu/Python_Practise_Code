import tkinter as tk

window = tk.Tk()
menubar = tk.Menu(window)

file_menu = tk.Menu(menubar,tearoff=False) # tearoff=False，表示菜单不可以被拖拽出来
file_menu.add_command(label='枸杞')
file_menu.add_command(label='梧桐')
file_menu.add_separator()   # 一个下拉菜单分割线
file_menu.add_command(label='酸枣')

# 添加标签到主窗口
menubar.add_cascade(label='木部',menu=file_menu)
#menubar.add_cascade(label='木部2',menu=file_menu)

window.config(menu=menubar)

window.mainloop()

