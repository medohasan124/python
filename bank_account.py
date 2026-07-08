
#banking programing

# show balanc
# deposit
#with drow

def show_balance():
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    
    amount = float(input("Enter Your Amount: "))

    if amount < 0:
         print("*********************")
         print("this amount  not Avilable")
         print("*********************")
         return 0
    else:
        return amount


def with_drow():
    
     amount = float(input("Enter Your withdow: "))

     if amount > balance:
         print("*********************")
         print("sorry you don't have that mony")
         print("*********************")
         return 0
     elif amount < 0:
         print("*********************")
         print("must be grater than 0")
         print("*********************")
         return 0
     else:
         return amount

balance = 0 
is_running = True

while is_running:
    print("*********************")
    print("Banking programing")
    print("*********************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdrow")
    print("4.Exit")
    print("*********************")

    choice = input("Enter your choice (1-4): ")

    
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= with_drow()
    elif choice == "4":
        is_running = False
    else:
        print("*********************")
        print("Your choice not Avilable")
        print("*********************")

print("*********************")
print("Thanks have a nice day !")
print("*********************")