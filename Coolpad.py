from tkinter import *
import customtkinter
from CTkMenuBar import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
from CTkColorPicker import *


root = customtkinter.CTk()
root.geometry("800x600")
root.title("Coolpad")


global open_status_name
open_status_name = False

global selected
selected = False


customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#New File
def new_file():
    #Delete previous text
    entry.delete("1.0", END)
    #Update status
    root.title('New File - CoolPad')

#Open File
def open_file():
    #Delete previous text
    entry.delete("1.0", END)
    #Get filename
    text_file = filedialog.askopenfilename(initialdir="C:/downloads/", title="Open File", filetypes=(("Text FIles", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    if text_file:
        global open_status_name
        open_status_name = text_file

    name = text_file
    name = name.replace("C:/downloads/", "")
    root.title(f'{name} - CoolPad')

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    entry.insert(END, stuff)
    text_file.close()

#Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/downloads/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        name = name.replace("C:/downloads/", "")
        root.title(f'{name} - CoolPad')
        #Save the file
        text_file = open(text_file, "w")
        text_file.write(entry.get(1.0, END))
        text_file.close

def cut_text():
    global selected
    if entry.selection_get():
        selected = entry.selection_get()
        entry.delete("sel.first", "sel.last")

def copy_text():
    global selected
    if entry.selection_get():
        selected = entry.selection_get()


def paste_text():
    if selected:
        position = entry.index(INSERT)
        entry.insert(position, selected)

def change_theme_to_light():
    customtkinter.set_appearance_mode("Light")
    print("Theme set to light")

def change_theme_to_dark():
    customtkinter.set_appearance_mode("Dark")
    print("Theme set to dark")

def system_theme():
    customtkinter.set_appearance_mode("System")
    print("Theme set to system")

menu = CTkMenuBar(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")
button_3 = menu.add_cascade("Settings")


dropdown1 = CustomDropdownMenu(widget=button_1, corner_radius=0)
dropdown1.add_option(option="Open", command=open_file, corner_radius=0)
dropdown1.add_option(option="New File", command=new_file, corner_radius=0)
dropdown1.add_separator()
dropdown1.add_option(option="Save As", command=save_as_file, corner_radius=0)

dropdown1.add_separator()

dropdown2 = CustomDropdownMenu(widget=button_2, corner_radius=0)
dropdown2.add_option(option="Cut", command=cut_text)
dropdown2.add_option(option="Copy", command=copy_text)
dropdown2.add_option(option="Paste", command=paste_text)
dropdown2.add_separator()
dropdown2.add_option(option="Undo")
dropdown2.add_option(option="Redo", command="redo_text")

dropdown3 = CustomDropdownMenu(widget=button_3, corner_radius=0)
sub_menu2 = dropdown3.add_submenu("Theme")
sub_menu2.add_option(option="Light Mode", command=change_theme_to_light)
sub_menu2.add_option(option="Dark Mode", command=change_theme_to_dark)
sub_menu2.add_option(option="System", command=system_theme)

entry = customtkinter.CTkTextbox(root, width=10000, height=10000, corner_radius=0, font=('Arial', 18), activate_scrollbars=True)
entry.pack()

scrollbar = customtkinter.CTkScrollbar(root, command=entry.yview, hover=True, width=5)
scrollbar.pack()

root.mainloop()