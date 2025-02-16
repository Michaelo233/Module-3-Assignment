# required python modules for this program.
import random
import time
import os

# variablr declaration of pixell river atm menu.
option_menu = ["D", "W", "Q"]
random_balance = random.randint(-1000, 10000)
account_balance = random_balance
space = " "
filler = "*"
fill_char = "*"
filler = filler.center(40, fill_char)

option_menu[2] = False

# this checks if the selection is Q, if yes, option_menu[2] = True.
while not option_menu[2]:
    print(f"{filler} \n {space:>8} PIXELL RIVER FINANCIAL \n {space:>13}"
        f"ATM Simulator \n\n {space:>2}Your current balance is: "
        f"${account_balance:,.2f} \n\n {space:>14} Deposit: D \n "
        f"{space:>13} Withdraw: W \n {space:>15} Quit: Q \n{filler}")
    
    # User selection input option.
    selection = input("Enter your selection: ").capitalize()

    # check if selection is D, and add the deposit to the bank balance.
    if selection in option_menu and selection == option_menu[0]:
        transaction_amount = float(
            input("Enter the transaction amount: "))
        account_balance += transaction_amount
    
        print(f"\n{filler}\n Your current balance is: "
              f"${account_balance:,.2f}\n{filler}\n")

    # check is selection is W, and withdraws users input from the bank.
    # it also confirms if user has sufficient funds to withdraw. 
    elif selection in option_menu and selection == option_menu[1]:
        transaction_amount = float(
            input("Enter the transaction amount: "))
        if account_balance - transaction_amount <= 0:
            print(f"\n{filler}\n {space:>10w} INSUFFICIENT FUNDS\n"
                  f"{filler}\n")
        
        else:
            account_balance -= transaction_amount
            print(f"\n{filler}\n Your current balance is: "
                  f"${account_balance:,.2f}\n{filler}\n")
    
    # check if users selection is valid.
    else:
        print(f"\n{filler}\n{space:>11} INVALID SELECTION\n{filler}")
        # Pause the script for the specified number of seconds
        time.sleep(3)

         # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        