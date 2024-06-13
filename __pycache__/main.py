from operation import show_balance,deposit,withdraw

def main():
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
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -=withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('Not valid')

    print("Thank you and have a nice day!")

if __name__ == "__main__":
    main()