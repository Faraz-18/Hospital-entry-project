import sqlite3

connection = sqlite3.connect("Patients.db")
cursor = connection.cursor()
# cursor.execute("CREATE TABLE Patient (name TEXT, age INTEGER, gender TEXT, condition TEXT, city TEXT)")
# print(cursor.execute("select * from patient").fetchall())
# connection.commit()


while True:
    print("1. To Insert Data")
    print("2. To View Data")
    choice = input("Enter Your Choice: ")
    if choice == "1":
      person_name = input("Enter patient's name: ")
      person_age =int(input("Enter patient's age: "))
      person_gender = input("Enter patient's gender: ")        
      person_condition = input("Enter patient's condition: ")
      person_city = input("Enter patient's city: ")
      cursor.execute(f"insert into patient values ('{person_name}', '{person_age}', '{person_gender}', '{person_condition}', '{person_city}')")
      connection.commit()
    if choice == "2":
          print("                 DATA PRINTING......")
          print("=========================================================")
          rows = cursor.execute("select * from Patient").fetchall()
          for i in rows:
              print(*i, sep='\t')
