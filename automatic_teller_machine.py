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
print(f"{filler} \n {space:>8} PIXELL RIVER FINANCIAL \n {space:>13}"
      f"ATM Simulator \n\n {space:>2}Your current balance is: "
      f"${account_balance:,.2f} \n\n {space:>14} Deposit: D \n "
      f"{space:>13} Withdraw: W \n {space:>15} Quit: Q \n{filler}")
