import tkinter as tk
from tkinter import ttk
import time

def start():
    GB = 100
    download = 0
    bar['value'] = 0
    speed = 1
    while(download < GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        root.update_idletasks()


root = tk.Tk()
root.geometry('350x120')
root.title('Progress Bar Demo')

percent = tk.StringVar()
text = tk.StringVar()

style = ttk.Style()
color = "red"
style.theme_use('default') 
style.configure(f"{color}.Horizontal.TProgressbar",
                foreground=color, background=color)

bar = ttk.Progressbar(root, style=f"{color}.Horizontal.TProgressbar",
                      orient=tk.HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = tk.Label(root, textvariable=percent).pack()
taskLabel = tk.Label(root, textvariable=text).pack()

button = tk.Button(root, text="download", command=start).pack()

root.mainloop()

