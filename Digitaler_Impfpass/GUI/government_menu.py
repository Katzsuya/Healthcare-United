import mysql.connector, os
import tkinter as tk
from tkinter import *

# ----------------------- Global Variables ----------------------- #

CurrentDIR = os.path.dirname(__file__)
ImageDIR = CurrentDIR + r"\Images"


# ----------------------- Functions ----------------------- #


def main():

    global root

    root = tk.Tk()
    root.title('Government menu')
    root.attributes('-fullscreen', True)

    # Background settings

    image = tk.PhotoImage(file = ImageDIR + r'\government.png')

    Menu_Image = image.subsample(
        2,
        2
    )

    canvas = Canvas(
        root,
        width = 1920,
        height = 1080

    )

    canvas.pack()

    canvas.create_image(
        0,
        0,
        anchor = NW,
        image = Menu_Image
    )

    # --------- Insert? --------- #  

    insert = tk.Button(
        root,
        text = 'Insert?',
        command = lambda:[sqlinsert()],
        borderwidth = 0,
        activeforeground = '#777788',
        bg = '#444F8D',
        width = 20
    )

    insert.place(
        x = 130,
        y = 300
    )

    # --------- Exit to menu button --------- #

    Logout = tk.Button(
        root,
        text = 'Logout',
        command = lambda:[logout()],
        borderwidth = 0,
        activeforeground = '#777788',
        bg = '#444F8D',
        width = 20        
    )

    Logout.place(
        x = 130,
        y = 330
    )

    # --------- Exit to menu button --------- #

    Exit = tk.Button(
        root,
        text = 'Exit Application',
        command = lambda:[root.destroy()],
        borderwidth = 0,
        activeforeground = '#777788',
        bg = '#444F8D',
        width = 20
    )

    Exit.place(
        x = 130,
        y = 360
    )

    root.mainloop()

def sqlinsert():

    root.destroy()

    menu = CurrentDIR + r'\insert.py'

    os.system('python {}'.format(menu))

def logout():

    root.destroy()

    new_login = CurrentDIR + r'\Login.py'

    os.system('python {}'.format(new_login))


if __name__ == '__main__':
    main()