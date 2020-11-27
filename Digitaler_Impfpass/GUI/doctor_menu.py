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
    root.title('Doctor Menu')
    root.attributes('-fullscreen', True)

    # Background settings

    image = tk.PhotoImage(file = ImageDIR + r'\Asklepios.png')

    canvas = Canvas(
        root,
        width = 1920,
        height = 1080,
        bg = '#9AC0CD'

    )

    canvas.pack()

    canvas.create_image(
        950,
        0,
        anchor = N,
        image = image
    )

    Impfungen = tk.Button(
        root,
        text = 'new vaccination',
        command = lambda:[impfungen()],
        width = 40,
        bg = '#9AC0CD'
    )

    Impfungen.place(
        x = 150,
        y = 400
    )

    query = tk.Button(
        root,
        text = 'Call up vaccinations',
        command = lambda:[Query()],
        width = 40,
        bg = '#9AC0CD'
    )

    query.place(
        x = 150,
        y = 430
    )

    Logout = tk.Button(
        root,
        text = 'Logout',
        command = lambda:[logout()],
        width = 40,
        bg = '#9AC0CD'
        )

    Logout.place(
        x = 150,
        y = 460
    )

    Exit = tk.Button(
        root,
        text = 'Exit application',
        command = lambda:[root.destroy()],
        width = 40,
        bg = '#9AC0CD'
        )
        
    Exit.place(
        x = 150,
        y = 490
    )

    root.mainloop()



def impfungen():

    root.destroy()

    inster_vaccination = CurrentDIR + r'\vaccination.py'

    os.system('python {}'.format(inster_vaccination))

def Query():

    root.destroy()

    call_vaccinations = CurrentDIR + r'\doctor_query.py'

    os.system('python {}'.format(call_vaccinations))

def logout():

    root.destroy()

    new_login = CurrentDIR + r'\Login.py'

    os.system('python {}'.format(new_login))

if __name__ == '__main__':
    main()