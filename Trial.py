name = ["Austin Maina", "Toji Fushiguro", "Maki Zenin"]
acct_bal = [100000000, 305003274, 504333324]
acct_pin = [2005, 3845, 5568]


def get_balance(target_name, target_pin, names_list, pin_list, balance_list):
    if target_name in names_list:
        index = names_list.index(target_name)
        if pin_list[index] == target_pin:
            return index  # PIN correct — hand back the index so we can act on the balance
        else:
            return "Wrong PIN"
    return "Name not found"


target_name = input("What is your name ")
target_pin = int(input("What is your PIN "))

result = get_balance(target_name, target_pin, name, acct_pin, acct_bal)

if result == "Wrong PIN" or result == "Name not found":
    print(result)
else:
    index = result  # PIN was correct, result is the account's index
    action = input("Withdraw, Deposit, or Checkbalance? ")

    if action.lower() == "withdraw":
        amount = int(input("How much would you like to withdraw? "))
        if amount <= acct_bal[index]:
            acct_bal[index] = acct_bal[index] - amount
            print("Withdrawal successful. New balance:", acct_bal[index])
        else:
            print("Insufficient funds. Current balance:", acct_bal[index])

    elif action.lower() == "deposit":
        amount = int(input("How much would you like to deposit? "))
        acct_bal[index] = acct_bal[index] + amount
        print("Deposit successful. New balance:", acct_bal[index])

    elif action.lower() == "checkbalance":
        print("Your balance is:", acct_bal[index])

    else:
        print("Invalid option")