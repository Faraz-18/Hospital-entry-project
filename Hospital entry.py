def Patient_entry(P_name, P_age, P_gender, P_condition, P_city, P_phone):
    return P_name, P_age, P_gender, P_condition, P_city, P_phone

for i in range(100):
    Person_name = input("Enter patient's name: ")
    Person_age = input("Enter patient's age: ")
    Person_gender = input("Enter patient's gender: ")
    Person_condition = input("Enter patient's condition: ")
    Person_city = input("Enter patient's city: ")
    Person_phone = input("Enter patient's phone number: ")
    
    result_name, result_age, result_gender, result_condition, result_city, result_phone = Patient_entry(
        P_name=Person_name, P_age=Person_age, P_gender=Person_gender,
        P_condition=Person_condition, P_city=Person_city, P_phone=Person_phone)
    
    if result_name.isalpha():
        if result_age.isdigit():
            if result_gender.isalpha():
                if result_condition.isalpha():
                    if result_city.isalpha():
                        if result_phone.isdigit():
                            print("Patient Information:")
                            print("Name =", result_name)
                            print("Age =", result_age)
                            print("Gender =", result_gender)
                            print("Condition =", result_condition)
                            print("City =", result_city)
                            print("Phone =", result_phone)
                            print("=" * 40)
                        else:
                            print("Invalid phone number.")
                    else:
                        print("City not recognized")
                else:
                    print("Condition not recognized")
            else:
                print("Gender not recognized")
        else:
            print("Age not recognized")
    else:
        print("Name not recognized")