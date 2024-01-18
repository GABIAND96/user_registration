import csv


def register():
    """register data input"""
    username = input("enter user: ")
    password = input("enter password: ")
    name = input("enter name: ")
    email = input("enter e-mail adress: ")

    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, name, email])
    print("the user has been registered")
    return writer


def login():
    """return if our input data is correct"""
    username = input("enter username: ")
    password = input("enter password: ")

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("succesfull authentication!")
                return True
        print("Wrong. check the username or the password.")
        return False


def show_details():
    """return details, name and e-mail adress"""
    username = input("enter username: ")

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print(f"Nume: {row[2]}")
                print(f"Email: {row[3]}")

            return row



def start():
    """start menu"""
    while True:
        print("\nMeniu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("enter option: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                while True:
                    print("\nMeniu after authentication:")
                    print("1. Show Details")
                    print("2. Logout")
                    inner_choice = input("enter option: ")
                    if inner_choice == '1':
                        show_details()
                    elif inner_choice == '2':
                        break
                    else:
                        print("invalid option. try again.")
        elif choice == '3':
            print("App closed.")
            break
        else:
            print("invalid option. try again.")


if __name__ == "__main__":
    start()


