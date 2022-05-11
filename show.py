import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry("2000x1080")
container = ttk.Frame()
root.title('District Wise Rainfall Analysis Dashboard : ')
canvas = tk.Canvas(container,width=1300, height=700)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

img = Image.open("img1.png")
resized = img.resize((1250, 500), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic)
label.pack(padx=20, pady=20)

img1 = Image.open("img2.png")
resized1 = img1.resize((1250, 500), Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resized1)
canvas.place(anchor='nw')
tk.Label(text="Grid Layout")
label = tk.Label(scrollable_frame, image=new_pic1)
label.pack(padx=20, pady=20)

img2 = Image.open("img3.png")
resized2 = img2.resize((1250, 500), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized2)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic2)
label.pack(padx=20, pady=20)

img3 = Image.open("img4.png")
resized3 = img3.resize((1250, 500), Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic3)
label.pack(padx=20, pady=20)

img4 = Image.open("img5.png")
resized3 = img4.resize((1250, 500), Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic4)
label.pack(padx=20, pady=20)

img5 = Image.open("img6.png")
resized3 = img5.resize((1250, 500), Image.ANTIALIAS)
new_pic5 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic5)
label.pack(padx=20, pady=20)

img6 = Image.open("img7.png")
resized3 = img6.resize((1250, 500), Image.ANTIALIAS)
new_pic6 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic6)
label.pack(padx=20, pady=20)

img7 = Image.open("img8.png")
resized3 = img7.resize((1250, 500), Image.ANTIALIAS)
new_pic7 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic7)
label.pack(padx=20, pady=20)

img8 = Image.open("img9.png")
resized3 = img8.resize((1250, 500), Image.ANTIALIAS)
new_pic8 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic8)
label.pack(padx=20, pady=20)

img9 = Image.open("img10.png")
resized3 = img9.resize((1250, 500), Image.ANTIALIAS)
new_pic9 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic9)
label.pack(padx=20, pady=20)

img10 = Image.open("img11.png")
resized3 = img10.resize((1250, 500), Image.ANTIALIAS)
new_pic10 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic10)
label.pack(padx=20, pady=20)



container.pack(padx=20, pady=20)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
