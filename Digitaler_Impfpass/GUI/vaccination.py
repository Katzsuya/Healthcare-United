import mysql.connector, os, time, datetime
import tkinter as tk
from tkinter import *
from datetime import date


# ----------------------- Global Variables ----------------------- #

CurrentDIR = os.path.dirname(__file__)
ImageDIR = CurrentDIR + r"\Images"


# ----------------------- Functions ----------------------- #


def main():

    conn()

    global root

    root = tk.Tk()
    root.title('Insert new vaccination')
    root.geometry('250x130')

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
        width = 100
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

    # --------- Dropdown menu for vaccine --------- #


    # Initiate empty list
    diseases = []

    # Fetch Column names from vaccine table without Vaccine_ID
    column_names = ("""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "vaccine" 
                    EXCEPT SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME = 'Vaccine_ID'""")

    cursor.execute(column_names)
    result = cursor.fetchall()

    # Append results into list
    for x in result:
        diseases.append(x)

    # Set default input value
    global disease_name

    disease_name = StringVar(root)
    disease_name.set(' ')

    disease = OptionMenu(
        root,
        disease_name,
        *diseases
    )

    disease.config(bg = 'WHITE')

    # Place dropdown menu
    disease.place(
        x = 100,
        y = 50,
        width = 100
    )

    # -- Disease label
    disease_label = tk.Label(
        root,
        text = 'Disease:',
    )

    disease_label.place(
        x = 13,
        y = 55
    )

    # --------- Save button --------- #
    # Inserts data into database

    Save = tk.Button(
        root,
        text = 'Save to database',
        command = lambda:[sqlinsert(vaccine_ID.get(), disease_name.get())]
    )

    Save.place(
        x = 100,
        y = 85
    )

    # --------- Exit to menu button --------- #

    Exit = tk.Button(
        root,
        text = 'Exit to menu',
        command = lambda:[quit()]
        )

    Exit.place(
        x = 12,
        y = 85
    )

    root.mainloop()

def conn():
    
    global db

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="vaccination",
    )

def sqlinsert(VaccineID, DiseaseName):

    today = date.today().strftime('%d.%m.%Y')

    VaccineID = VaccineID.translate({ord(i): None for i in "[(,)']"})
    DiseaseName = DiseaseName.translate({ord(i): None for i in "[(,)]'"})

    # timestamp = datetime.datetime.strptime(today, "%d/%m/%Y").timestamp()

    sql = """UPDATE vaccine
        SET {} = '{}'
        WHERE Vaccine_ID = {};""".format(DiseaseName, today, VaccineID)

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

def quit():

    root.destroy()

    menu = CurrentDIR + r'\doctor_menu.py'

    os.system('python {}'.format(menu))

if __name__ == '__main__':
    main()