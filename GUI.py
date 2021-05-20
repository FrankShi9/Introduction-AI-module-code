from tkinter import *


root = Tk()
list1 = [1,2,3]
list2 = [4,5,6]
listB = Listbox(root)
listB1 = Listbox(root)

for item in list1:
    listB.insert(2,item)
for item in list2:
    listB1.insert(2,item)

listB.pack()
listB1.pack()
#enter msg loop
root.mainloop()