from tkinter import Tk, Text
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
root = Tk(className=' Text Editor')

root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=500, weight=1)

text_editor = Text(root, foreground="#00FFFF", background="#000000")
text_editor.grid(row=0, column=1, sticky="nsew")
root.mainloop()
