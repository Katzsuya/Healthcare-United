import mysql.connector, os, time, datetime
import tkinter as tk
from tkinter import *
from datetime import date

# ----------------------- Global Variables ----------------------- #

CurrentDIR = os.path.dirname(__file__)
ImageDIR = CurrentDIR + r"\Images"


# ----------------------- Functions ----------------------- #

def main():

    global root

    root = tk.Tk()
    root.title('Insert')
    root.geometry('350x230')

    # --------- Tax ID initial entry field --------- #

    global tax_id

    tax_id = Entry(
        root,
        width = 40
    )

    # --------- Lastname initial entry field --------- #

    global Lastname

    Lastname = Entry(
        root,
        width = 40
    )

    # --------- Firstname initial entry field --------- #

    global Firstname

    Firstname = Entry(
        root,
        width = 40
        )

    # --------- Birthday initial entry field --------- #

    global birthday_day, birthday_month, birthday_year

    # -- Days dropdown menu

    days = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17',
        '18',
        '19',
        '20',
        '21',
        '22',
        '23',
        '24',
        '25',
        '26',
        '27',
        '28',
        '29',
        '30',
        '31',
    ]

    birthday_day = StringVar(root)
    birthday_day.set('')

    days_dropdown = OptionMenu(
        root,
        birthday_day,
        *days
    )

    days_dropdown.place(
        x = 80,
        y = 95,
        width = 60
    )

    # -- Months dropdown menu

    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'Octtober',
        'November',
        'December'
    ]

    birthday_month = StringVar(root)
    birthday_month.set('')

    months_dropdown = OptionMenu(
        root,
        birthday_month,
        *months
    )

    months_dropdown.place(
        x = 140,
        y = 95,
        width = 100
    )

    # -- Years dropdown menu

    current_year = date.today().strftime('%Y')

    years = [*range(1970, int(current_year) + 1, 1)]

    birthday_year = StringVar(root)
    birthday_year.set('')

    years_dropdown = OptionMenu(
        root,
        birthday_year,
        *years
    )

    years_dropdown.place(
        x = 240,
        y = 95,
        width = 80
    )

    # --------- Postcode initial entry field --------- #

    global Postcode

    Postcode = Entry(
        root,
        width = 40
        )

    # --------- Tax ID Label --------- #

    tax_label = tk.Label(
        root,
        text = 'Tax_ID: ',
    )

    tax_label.place(
        x = 10,
        y = 10
    )

    # --------- Lastname Label --------- #

    Lastname_label = tk.Label(
        root,
        text = 'Lastname:'
    )

    Lastname_label.place(
        x = 10,
        y = 40
    )

    # --------- Firstname Label --------- #

    Firstname_label = tk.Label(
        root,
        text = 'Firstname:'
    )

    Firstname_label.place(
        x = 10,
        y = 70
    )

    # --------- Birthday Label --------- #

    Birthday_label = tk.Label(
        root,
        text = 'Birthday:'
    )

    Birthday_label.place(
        x = 10,
        y = 100
    )

    # --------- Postcode Label --------- #

    postcode_label = tk.Label(
        root,
        text = 'Postcode:'
    )

    postcode_label.place(
        x = 10,
        y = 130
    )

    # --------- Button to save to database --------- #

    save = tk.Button(
        root,
        text = 'Save to database',
        command = lambda:[sqlinsert(tax_id.get(),  Lastname.get(), Firstname.get(), birthday_day.get(), birthday_month.get(), birthday_year.get(), Postcode.get())],
        width = 34
        )

    save.place(
        x = 78,
        y = 152
    )

    # --------- Exit to menu button --------- #

    Quit = tk.Button(
        root,
        text = 'Exit to menu',
        command = lambda:[quit()]
    )

    Quit.place(
        x = 10,
        y = 200
    )

    # -- Integrate User Input fields into the root window

    tax_id.place(
        x = 80,
        y = 10
    )

    Lastname.place(
        x = 80,
        y = 40
    )

    Firstname.place(
        x = 80,
        y = 70
    )

    Postcode.place(
        x = 80,
        y = 130
    )

    root.mainloop()

# Function to Establish Connection to the Database

def conn():

    global db

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="vaccination",
    )

def sqlinsert(TAX_ID, FIRSTNAME, LASTNAME, BIRTHDAY_DAY, BIRTHDAY_MONTH, BIRTHDAY_YEAR, POSTCODE):

    conn()
    
    bday = ('{}. {} {}').format(BIRTHDAY_DAY, BIRTHDAY_MONTH, BIRTHDAY_YEAR)

    # print(TAX_ID, LASTNAME, FIRSTNAME, bday, POSTCODE, VACCINE_ID)
    
    cursor = db.cursor(buffered = True)

    new_vaccine_ID = """INSERT INTO vaccine(
        Cholera,
        FSME,
        Dengue,
        HPV,
        Masern,
        Covid
    )

    VALUES (
        DEFAULT,
        DEFAULT,
        DEFAULT,
        DEFAULT,
        DEFAULT,
        DEFAULT
    );
    """

    cursor.execute(new_vaccine_ID)

    get_vaccine_id = 'SELECT Vaccine_ID FROM vaccine ORDER BY Vaccine_ID DESC;'

    cursor.execute(get_vaccine_id)
    vaccine_id_result = str(cursor.fetchone())
    
    sql = str("""INSERT INTO person(
        Tax_ID,
        Lastname,
        Firstname,
        Birthday,
        Postcode,
        Vaccine_ID
    )

    VALUES (
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}'
    )""").format(
        TAX_ID,
        FIRSTNAME,
        LASTNAME,
        bday,
        POSTCODE,
        vaccine_id_result.translate({ord(i): None for i in '(,)'})
    )

    cursor.execute(sql)

    # -- Commits the insert to the database. Important!

    db.commit()

def quit():

    root.destroy()

    menu = CurrentDIR + r'\government_menu.py'

    os.system('python {}'.format(menu))

if __name__ == '__main__':
    main()