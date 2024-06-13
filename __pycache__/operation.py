

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount =  float(int(input('Amount: ')))

    if amount < 0:
            print("Not a valid amount")
            return 0
    else:
         return amount


def withdraw(balance):
    amount = float(int(input('Amount: ')))

    if  amount > balance:
        print("Not enough funds")
        return 0
    elif amount < 0:
        print("amount must be greater thant 0")
        return 0

    else:
        return amount