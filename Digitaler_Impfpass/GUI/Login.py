import mysql.connector, os
import tkinter as tk
from tkinter import *

# ----------------------- Global Variables ----------------------- #

CurrentDIR = os.path.dirname(__file__)
ImageDIR = CurrentDIR + r"\Images"


# ----------------------- Functions ----------------------- #


def main():

    try:
        conn()
        print("Database connection can be established")
    except:
        print("Could not connect to the database!")
        sys.exit()

    global root

    root = tk.Tk()
    root.title("Welcome")
    root.geometry('1920x1080')
    root.attributes('-fullscreen', True) 

    canvas = Canvas(
        root, 
        width = 1920, 
        height = 1080
        )

    canvas.pack()

    global Status

    Status = ''

    # User Inputs

    global username

    username = Entry(
        root,
        width = 40
    )

    global password

    password = Entry(
        root,
        width = 40,
        show = '*'
    )

    image = tk.PhotoImage(file = ImageDIR + r'\Login.png')

    background_image = canvas.create_image(
        960,
        550,
        image = image
    )

    canvas.tag_lower(background_image)

    username_label = tk.Label(
        root,
        text = 'Username:',
        borderwidth = 0,
        bg = 'BLACK',
        fg = 'WHITE',
        font = ('Helvetica', 16)
    )

    username_label.place(
        x = 100,
        y = 700,
    )


    password_label = tk.Label(
        root,
        text = 'Password:',
        borderwidth = 0,
        bg = 'BLACK',
        fg = 'WHITE',
        font = ('Helvetica', 16)
    )

    password_label.place(
        x = 100,
        y = 730
    )

    login_button = tk.Button(
        root,
        command = lambda:[login(username.get(), password.get())],
        text = 'Login',
        font = ('Helvetica', 16),
        anchor = 'center',
        bg = 'BLACK',
        fg = 'WHITE',
        borderwidth = 1,
        width = 19
    )

    login_button.place(
        x = 220,
        y = 760
    )

    Status = tk.Label(
        root,
        text = Status,
        bg = 'BLACK',
        fg = 'WHITE',
        font = ('Helvetica', 12),
        anchor = 'w'
    )

    Status.place(
        x = 250,
        y = 810
    )

    username.place(
        x = 220,
        y = 705
    )

    password.place(
        x = 220,
        y = 735
    )

    root.mainloop()

# Function to Establish Connection to the Database

def conn():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="vaccination",
    )

def login(username, password):
    
    # -- Login Credentials
    
    # -- Doctor
    if username == 'doctor' and password == 'doctor':
        Status.config(fg = 'GREEN', text = 'Welcome, Doctor {}'.format(username))
        try:
            conn()
            
            doctor_menu = str(r'python {}\doctor_menu.py').format(CurrentDIR)

            root.destroy()

            os.system(doctor_menu)

        except:
            Status.config(fg = 'RED', text = 'Database connection failed!')

    # -- Government
    elif username == 'staat' and password == 'staat':
        try:
            conn()

            government_menu = str(r'python {}\government_menu.py').format(CurrentDIR)

            root.destroy()

            os.system(government_menu)
        except:
            Status.config(fg = 'RED', text = 'Database connection failed!')

    # -- User 1

    if username == 'user1' and password = 'user1':
        
        try:
            conn()

            user_menu = str(r'python {}\user_menu').format(CurrentDIR)

            root.destroy()

            os.system(user_menu)

    else:
        Status.config(fg = 'RED', text = 'Invalid login credentials!')

if __name__ == '__main__':
    main()