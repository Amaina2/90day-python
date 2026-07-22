name = ["Austin Maina", "Toji Fushiguro", "Maki Zenin"]
acct_bal = [100000000, 305003274, 504333324]
acct_pin = [2005, 3845, 5568]

def get_balance(target_name, target_pin, names_list, pin_list, balance_list):
    if target_name in names_list:
        index = names_list.index(target_name)
        if pin_list[index] == target_pin:
            return index
        else:
            return "Wrong PIN"
    return "Name not found"

target_name = input("What is your name ")
target_pin = int(input("What is your PIN "))

result = get_balance(target_name, target_pin, name, acct_pin, acct_bal)

if result == "Wrong PIN" or result == "Name not found":
    print (result)
else:
    index = result
    ask_action = input("Do you want to Withdraw, Deposit or Check Balance (W/D/CB) ").upper()
    if ask_action == "W":
        try:
            amount = int(input("How much do you want to withdraw? "))
        except ValueError:
            print(f"Invalid Amount")
        else:
            if amount <= acct_bal[index]:
                balance = acct_bal[index] - amount
                print(f"{amount}USD is successfully Withdrawn. Your new account balance is {balance}USD")
            else:
                print(f"Insuffiecient Balance, Your current balance is {acct_bal[index]}")

    elif ask_action == "D":
        try:
            amount = int(input("How much do you want to deposit? "))
        except ValueError:
            print(f"Invalid Amount")
        else:
            balance = acct_bal[index] + amount
            print(f"Your new balance is {balance} USD")

    elif ask_action == "CB":
        print(f"Your current account balance is {acct_bal[index]} USD")

    else:
        print("Invalid Choice")