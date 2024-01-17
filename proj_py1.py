import tkinter as tk
from tkinter import simpledialog
from tkinter import *
import os, shutil
from glob import glob
import pathlib as Path
ly = "https://www.laptopmag.com/articles/show-full-folder-path-file-explorer)\n"
src_dir = input("Enter your base directory location \n""(How to get the location:"+ly)
root = tk.Tk()
root.withdraw()
y = "Enter the names of the folders you want to create separated by commas"
user_input = simpledialog.askstring(title = "Well",
                                    prompt = y)
list = user_input.split(",")
for i in list:
    path = os.path.join(src_dir, i)
    os.mkdir(path)
ls = glob(os.path.join(src_dir, '**'), recursive = True)
us = glob(os.path.join (user_input, '**'), recursive = True)
'''if not os.path.isdir(user_input):
    print("Not exists")'''
user_n2 = simpledialog.askstring(title = "Now",
                                    prompt = "File keyword")
dict = user_n2.split(",")
uk = glob(os.path.join (user_n2, '**'), recursive = True)

for file in ls:
        if user_n2 in file:
            for f in us:
                if user_n2 in f:
                    shutil.move(file, f)
            else:
                print("k")
print(src_dir)
print(ls)
print(user_input)


