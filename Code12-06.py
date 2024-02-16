from tkinter import *

window = Tk()
window.geometry("600x600")

photo = PhotoImage(file = 'pet01.gif')
photo_ary = []
h = photo.height()
w = photo.width()
for i in range(h):
    for k in range(w):
        r, g, b = photo.get(i,k)
        value = (r+g+b)//3
        photo_ary.append(value)

if photo_ary[i] <= 127:
    photo_ary[i] = 0
else :
    photo_ary[i] = 255

for i in range(len(h)):
    for k in range(w)
        r = g = b = photo_ary[pos]
        pos = pos + 1
        photo_guy

paper = Label(window, image=photo)
paper.pack(expand=1, anchor = CENTER)
window.mainloop()

