import mysql.connector
from datetime import date

# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     database="vaccination",
# # )

# # diseases = []
# # column_names = ('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "vaccine" EXCEPT SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME = "Vaccine_ID"')

# # cursor = db.cursor()
# # cursor.execute(column_names)
# # result = cursor.fetchall()

# # for x in result:
# #     diseases.append(x)

# # print(diseases[0])

# # # for x in result:
# # #     vaccine_ids.append(x)
# # #     print(vaccine_ids)

# today = date.today()

# timestamp = today.strftime('%B %d, %Y')

# print(timestamp)

def conn():

    global db

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="vaccination",
    )

# def query(VACCINE_ID):

#     conn()

#     ID = str(VACCINE_ID)

#     sql = """DROP TABLE IF EXISTS temp_table;
#         CREATE TEMPORARY_TABLE temp_table AS SELECT * FROM vaccine WHERE Vaccine_ID = {};

#         ALTER TABLE temp_table DROP COLUMN Vaccine_ID;""".format(ID)

#     print(sql)

#     cursor = db.cursor()
#     cursor.execute(sql, multi = True)

#     cursor.execute('SELECT * FROM temp_table')

#     global result

#     result = cursor.fetchall()
    
#     print(result)

# query(1)

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
    print(vaccine_ids)