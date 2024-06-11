from banking_pkg import account #part of task 4

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#     <-----  Task 2  ---->
print("    === Automated Teller Machine ===    ")

#declare variable <name>, <pin>, and balance using input function for user
name = input("Enter your name to register: ")  
pin = input("Enter PIN: ")   
balance = 0

#echo info
print(name, " has been registered with a starting balance of $" + str(balance))


#     <-----  Task 3  ---->
# User logs in and shows menu an infinite while loop
print("")
print("    === Automated Teller Machine ===    ")
while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials!")

    break

# 2nd inf while loop calling atm_menu func w/ user variable as arg
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    #  <--- Task 4 ---->
    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)   #this is current balance before deposit
        account.show_balance(balance)  #display updated balance


    elif option == "3": #same as option 2 but different function calls
        balance = account.withdraw(balance)   
        account.show_balance(balance)  
    
    elif option == "4": #same as option 2 but different function calls
        account.logout(name)

        break

#     <-----  Task 4  ---->
#View, withdraw, deposit in bank account. account.py code is added. go to account.py

