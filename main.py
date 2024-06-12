def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount =  float(int(input('Amount: ')))

    if amount < 0:
            print("Not a valid amount")
            return 0
    else:
         return amount


def withdraw():
    amount = float(int(input('Amount: ')))

    if  amount > balance:
        print("Not enough funds")
        return 0
    elif amount < 0:
        print("amount must be greater thant 0")
        return 0

    else:
        return amount


balance = 0
is_running= True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exit')

    choice = input('Enter your choice(1-4): ')

    if choice == "1":
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -=withdraw()
    elif choice == '4':
        is_running = False
    else:
        print('Not valid')

print("Thank you and have a nice day!")
