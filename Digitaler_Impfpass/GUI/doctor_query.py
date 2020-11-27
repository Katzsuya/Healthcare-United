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
    root.title('Vaccinations')
    root.geometry('460x250')

    conn()

    # --------- Dropdown menu for Vaccine IDs --------- #

    # Innitiate empty list
    vaccine_ids = []

    # Get current Vaccine IDs from database
    cursor = db.cursor()
    cursor.execute('SELECT VACCINE_ID FROM vaccine')

    result = cursor.fetchall()

    # Append the results to the list
    for x in result:
        vaccine_ids.append(x)

    # Set default input value

    global vaccine_ID

    vaccine_ID = StringVar(root)
    vaccine_ID.set(' ')

    vaccineID = OptionMenu(
        root,
        vaccine_ID,
        *vaccine_ids
    )

    vaccineID.config(bg = 'WHITE')

    vaccineID.place(
        x = 100,
        y = 20,
        width = 325
    )

    # -- Vaccine ID label

    vaccineID_label = tk.Label(
        root,
        text = 'Vaccine ID:',
    )

    vaccineID_label.place(
        x = 13,
        y = 25
    )


    # --------- Label and text for Query result --------- #

    SQLresultlabel = tk.Label(
        root,
        text = 'Vaccinations: '
    )

    SQLresultlabel.place(
        x = 13,
        y = 65
    )

    cholera = tk.Label(
        root,
        text =  'Cholera:'
    )

    cholera.place(
        x = 100,
        y = 66
    )

    global cholera_result

    cholera_result = tk.Label(
        root,
        text = 'test'
    )

    cholera_result.place(
        x = 160,
        y = 66
    )

    fsme = tk.Label(
        root,
        text = 'FSME:'
    )

    fsme.place(
        x = 100,
        y = 96
    )

    global fsme_result

    fsme_result = tk.Label(
        root,
        text = 'test'
    )

    fsme_result.place(
        x = 160,
        y = 96
    )

    dengue = tk.Label(
        root,
        text = 'Dengue:'
    )

    dengue.place(
        x = 100,
        y = 126
    )

    global dengue_result

    dengue_result = tk.Label(
        root,
        text = 'test'
    )

    dengue_result.place(
        x = 160,
        y = 126
    )

    hpv = tk.Label(
        root,
        text = 'HPV:'
    )

    hpv.place(
        x = 300,
        y = 66
    )

    global hpv_result

    hpv_result = tk.Label(
        root,
        text = 'test'
    )

    hpv_result.place(
        x = 350,
        y = 66
    )

    masern = tk.Label(
        root,
        text = 'Masern:'
    )

    masern.place(
        x = 300,
        y = 96
    )

    global masern_result

    masern_result = tk.Label(
        root,
        text = 'test'
    )

    masern_result.place(
        x = 350,
        y = 96
    )

    covid = tk.Label(
        root,
        text = 'COVID:'
    )   

    covid.place(
        x = 300,
        y = 126
    )

    global covid_result

    covid_result = tk.Label(
        root,
        text = 'test'
    )

    covid_result.place(
        x = 350,
        y = 126
    )

    # --------- Button to fire query into database --------- #

    fire = tk.Button(
        root,
        text = 'Go!',
        command = lambda:[query(vaccine_ID.get())],
        width = 45
        )

    fire.place(
        x = 101,
        y = 222
    )

    # --------- Exit to menu button --------- #

    Exit = tk.Button(
        root,
        text = 'Exit to Menu',
        command = lambda:[quit()],
        width = 13
        )

    Exit.place(
        x = 0,
        y = 222
    )

    root.mainloop()

def conn():

    global db

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="vaccination",
    )

def query(VACCINE_ID):

    conn()

    cholerasql = 'SELECT Cholera FROM vaccine WHERE Vaccine_ID = {};'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor = db.cursor()
    cursor.execute(cholerasql)

    choleraresult = cursor.fetchall()

    
    fsmesql = 'SELECT FSME FROM vaccine WHERE Vaccine_ID = {}'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor.execute(fsmesql)

    fsmeresult = cursor.fetchall()

    
    denguesql = 'SELECT Dengue FROM vaccine WHERE Vaccine_ID = {}'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor.execute(denguesql)

    dengueresult = cursor.fetchall()


    hpvsql = 'SELECT HPV FROM vaccine WHERE Vaccine_ID = {}'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor.execute(hpvsql)

    hpvresult = cursor.fetchall()


    masernsql = 'SELECT Masern FROM vaccine WHERE Vaccine_ID = {}'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor.execute(masernsql)

    masernresult = cursor.fetchall()


    covidsql = 'SELECT Covid FROM vaccine WHERE Vaccine_ID = {}'.format(VACCINE_ID.translate({ord(i): None for i in '(,)'}))

    cursor.execute(covidsql)

    covidresult = cursor.fetchall()


    cholera_result.config(text = choleraresult)
    fsme_result.config(text = fsmeresult)
    dengue_result.config(text = dengueresult)
    hpv_result.config(text = hpvresult)
    masern_result.config(text = masernresult)
    covid_result.config(text = covidresult)

def quit():

    root.destroy()

    menu = CurrentDIR + r'\doctor_menu.py'

    os.system('python {}'.format(menu))

if __name__ == '__main__':
    main()