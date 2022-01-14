import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ctypes import windll
import keypress_sound
import threading

# high quality font
windll.shcore.SetProcessDpiAwareness(1)


def makeIndent(indent_length=4):
    text = text_editor.get("1.0", tk.END)
    lines = text.split("\n")
    new_data = ""
    for index in range(len(lines)):
        lines[index] = " " * indent_length + lines[index] + "\n"
        new_data += lines[index]

    change_text_of_text_editor(new_data)

# delete -> new data


def change_text_of_text_editor(text):
    text_editor.delete('1.0', tk.END)
    text_editor.insert(tk.END, text)


def open_text():
    typ = [('Text Files', '*.txt')]
    filepath = askopenfilename(filetypes=typ)
    if not filepath:
        return
    text_editor.delete('1.0', tk.END)
    with open(filepath, "r", encoding="utf-8") as open_file:
        text = open_file.read()
        text_editor.insert(tk.END, text)
    root.title(f'Text Files - {filepath}')


def file_save():
    typ = [("Text Files", "*.txt")]
    filepath = asksaveasfilename(defaultextension="txt", filetypes=typ)
    if not filepath:
        return
    with open(filepath, "w") as save_file:
        text = text_editor.get("1.0", tk.END)
        save_file.write(text)
    root.title(f"Text Editor - {filepath}")


def delete_text_specified_word(bad_words):
    with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)


def leave_specified_text(good_words):
    with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
        for line in oldfile:
            if any(good_word in line for good_word in good_words):
                newfile.write(line)


def start_key_press_sound():
    thread = threading.Thread(target=keypress_sound.start)
    thread.start()


#root
root = tk.Tk()
root.title('Text Editor')
root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=500, weight=1)
root.attributes("-alpha", 0.5)

# text editor
text_editor = tk.Text(root, foreground="#00FFFF",background="#000000", font=("Courier", 15))
text_editor.grid(row=0, column=1, sticky="nsew")

# menu
menubar = tk.Menu(root, foreground="#00FFFF",
                  background="#000000", activebackground="#000000",)
function_list = tk.Menu(
    menubar, tearoff=0, foreground="#00FFFF", background="#000000")
menubar.add_cascade(label="Function", menu=function_list)
root.config(menu=menubar)


function_list.add_command(label="Open", command=open_text)
function_list.add_command(label="Save", command=file_save)
function_list.add_command(label="MakeIndent", command=makeIndent)

start_key_press_sound()
root.mainloop()
