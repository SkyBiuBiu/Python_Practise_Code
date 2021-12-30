import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

# # 1.pack 方法
# tk.Label(window,text='1').pack(side='top')
# tk.Label(window,text='1').pack(side='bottom')
# tk.Label(window,text='1').pack(side='left')
# tk.Label(window,text='1').pack(side='right')

# 2.grid 方法
canvas = tk.Canvas(window,height=150,width=500)
canvas.grid(row=1,column=1)
image_file = tk.PhotoImage(file='img.png')
image = canvas.create_image(0,0,anchor='nw',image=image_file)


# # 3.place 方法（以数字1的中心为锚点，放置在x=100,y=100的地方，即中心）
# tk.Label(window,text='1').place(x=100,y=100,anchor='center')

window.mainloop()
