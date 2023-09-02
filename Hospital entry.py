from datetime import datetime

patient = []

def add_patient():
    print("\n'Indus Hospital'\n")
    Person_name = input("Enter patient's name: ")
    Person_age = input("Enter patient's age: ")
    Person_gender = input("Enter patient's gender: ")
    Person_condition = input("Enter patient's condition: ")
    Person_city = input("Enter patient's city: ")
    Person_phone = input("Enter patient's phone number: ")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    complete = f"Name: {Person_name}\nAge: {Person_age}\nGender: {Person_gender}\nCondition: {Person_condition}\nCity: {Person_city}\nPhone: {Person_phone}\n"

    if Person_name.isalpha() and Person_age.isdigit() and Person_gender.isalpha() and Person_condition.isalpha() and Person_city.isalpha() and Person_phone.isdigit():
        print("Patient Information:")
        print("Name =", Person_name)
        print("Age =", Person_age)
        print("Gender =", Person_gender)
        print("Condition =", Person_condition)
        print("City =", Person_city)
        print("Phone =", Person_phone)
        print("=" * 40)
        patient.append(complete)
    else:
        print("Invalid input. Please enter valid data.")

def view_patient_data():
    if len(patient) == 0:
        print("No patient data available.")
    else:
        print("Patient Data:")
        for i in patient:
            print(i)

while True:
    print("\n'Indus Hospital'\n")
    print("1: To add patient:")
    print("2: View patient's Data:")

    user_choice = input("\nEnter your choice: ")

    if user_choice == "1":
        add_patient()
    elif user_choice == "2":
        view_patient_data()
    else:
        print("Invalid choice. Please enter 1 or 2.")
