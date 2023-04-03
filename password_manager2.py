passwords = {}
user_set_password = ("password2.txt")

def enter():  
    pass_enter = input("Please enter your password to access your passwords:") 
    if pass_enter == password_true:
        main() 
    else:
        print("Password is INCORRECT! Please try again")
        enter()
       
def userpass(username, password):
    with open("PMResults2.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def view_password():
    print("")
    with open("PMResults2.txt", "r") as file:
        contents = file.read()
        print(contents)
    print("_________________________________")

def clear():
    with open("PMResults2.txt", "w") as file:
        file.write("")
    print("")
    print("----------CLEARED!----------")
    print("")

def clear2():
    with open("password2.txt", "w") as file:
        file.write("!placeholder_password!")
    print("----------CLEARED!----------")

def main():

    while True:
        print("1. Add Password:")
        print("2. View Passwords:")
        print("3. Clear your Stored Passwords")
        print("4. Exit:")
        print("5. Clear Entry Password")
        print("")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("")
            username = input("Enter username: ")
            password = input("Enter password: ")
            userpass(username, password)
            print("_________________")
            print("Saved Succesfully")
            print("_________________")
            print("")
        elif choice == "2":
           print("")
           view_password()
        elif choice == "3":
            clear()
        elif choice == "4":
            break
        elif choice == "5":
            clear2()
            print("Please Run App again to enter your new password.")
            print("")
            break
        else:
            print("Invalid choice")  
            print("")

file = open("password2.txt")
line1 = file.readlines()
password_true = line1[0]

if password_true == "!placeholder_password!":
    print("")
    print("---------------------------------------------")
    user_set_password = input("Hello new user, please add a password: ")
    print("")
    with open("password2.txt", "w") as file:
        file.write(user_set_password)
    main()
else:
    enter()





