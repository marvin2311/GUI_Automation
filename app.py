import tkinter as tk
from tkinter import filedialog, Text
import subprocess
import os

root = tk.Tk()
root.title("Automation for starting programs")

apps = []

label = tk.Label(root, text="Selected Files", bg="white", font=(None, 20))
label.pack(side = "top", pady = 15)

if os.path.isfile("saveapps.txt"):
    with open("saveapps.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select Files",
    filetypes=(("applications", "*.app"), ("all files", "*.*")))

    if filename:
        apps.append(filename)

    for app in apps:
        name = app.split("/")[-1]
        label = tk.Label(frame, text=name, bg="#F0FFF0")
        label.pack()


def closeApps():
    for widget in frame.winfo_children():
        widget.destroy()
    apps.clear()
    if os.path.isfile("saveapps.txt"):
        os.remove("saveapps.txt")


def runApps():
    for app in apps:
        subprocess.call(["open", app])


canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

frame = tk.Frame(root, bg="#F0FFF0")
frame.place(rely=0.1, relx=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,fg="black", command=addApp)
openFile.pack(side="left", padx=30, pady=10)
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,fg="black", command=runApps)
runApps.pack(side="left", padx=10, pady=10)
closeFiles = tk.Button(root, text="Close Files", padx=10, pady=5,fg="black", command=closeApps)
closeFiles.pack(side="right", padx=30, pady=10)

for app in apps:
    name = app.split("/")[-1]
    label = tk.Label(frame, text=name, bg="#F0FFF0")
    label.pack()


root.mainloop()

if apps:
    with open("saveapps.txt", "w") as f:
        for app in apps:
            f.write(app+",")
