from datetime import datetime

patients = []

def add_patient():
    print("\n'Indus Hospital'\n")
    person_name = input("Enter patient's name: ")
    person_age = input("Enter patient's age: ")
    person_gender = input("Enter patient's gender: ")        
    person_condition = input("Enter patient's condition: ")
    person_city = input("Enter patient's city: ")
    person_phone = input("Enter patient's phone number: ")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if person_name.isalpha() and person_age.isdigit() and person_gender.isalpha() and person_condition.isalpha() and person_city.isalpha() and person_phone.isdigit():
        patient_info = {
            "Name": person_name,
            "Age": person_age,
            "Gender": person_gender,
            "Condition": person_condition,
            "City": person_city,
            "Phone": person_phone,
            "Timestamp": current_time
        }
        print("Patient Information:")
        for key, value in patient_info.items():
            print(f"{key} =", value)
        print("=" * 40)
        patients.append(patient_info)
    else:
        print("Invalid input. Please enter valid data.")

def view_patient_data():
    if len(patients) == 0:
        print("No patient data available.")
    else:
        print("Patient Data:")
        for i, patient_info in enumerate(patients, start=1):
            print(f"Patient {i}:")
            for key, value in patient_info.items():
                print(f"{key} =", value)
            print("=" * 40)

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
