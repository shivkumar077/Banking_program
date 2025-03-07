#banking program

def show_balance(balance):
    print('*****************************')
    print(f"Your account Balance is: Rs {balance:.2f}")
    print('*****************************')

def deposit(balance):
    print('*****************************')
    amount = float(input("Enter the Amount You wanna deposit: Rs  "))
    print('*****************************')

    if amount<=0:
        print('*****************************')
        print("The amount must be greater then 0")
        print('*****************************')
        return 0
    else:
        return amount

def withdraw(balance):
    print('*****************************')
    amount = float(input("Enter the Amount You wanna Withdraw: "))
    print('*****************************')

    if amount > balance:
        print('*****************************')
        print("Insuffincent balance")
        print('*****************************')
        return 0
    elif amount <= 0:
        print('*****************************')
        print("The Amount Must be greater then 0")
        print('*****************************')
        return 0
    else:
        return amount

def main():
    balance = 0

    is_running = True

    while is_running:
        print('*****************************')
        print("------SHIV'S BANKING PROGRAM------")
        print('*****************************')
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print('*****************************')

        choice = input("Enter Your Choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print('*****************************')
            print("That Choice was not valid TRY AGAIN")
            print('*****************************')
    print('*****************************')
    print("Thank you for using our service hope to see you again soon")
    print('*****************************')


if __name__ == '__main__':
    main()