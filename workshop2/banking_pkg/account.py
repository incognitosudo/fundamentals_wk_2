#     <-----  Task 4  ---->

#when called, function displays user balance -when logged in.
def show_balance(balance):
    print("Current Balance: $"+ str(balance))

# function adds balance and deposit amount
def deposit(balance):
    amount = float(input("Enter amount to deposit: ")) 
    return balance + amount

# funciton is similar to deposit
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    return balance - amount

def logout(name):
    print("Goodbye " + name + "!")


#continue to app.py