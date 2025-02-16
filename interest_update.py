# modules needed
import math
from pprint import pprint
import csv

# Dictionary containing Users account number and account balance.
users_account_balances = {}

# open account balance file
with open("account_balances.txt", "r") as account_balance_file:
    for line in account_balance_file:
      key, value = line.strip().split('|')
      users_account_balances[key] = float(value)
pprint(users_account_balances)
print("\n")

for key, value in users_account_balances.items():
   if value >= 1000:
      #print(value)
      balance = (value * 2.5) / (12 * 100)
      value += balance
      users_account_balances[key] = value
      
   elif value < 1000:
      balance = (value * 1) / (12 * 100)
      value += balance
      users_account_balances[key] = value

   elif value >= 5000:
      balance = (value * 5) / (12 * 100)
      value += balance
      users_account_balances[key] = value

   elif value == 0:
      value = value
      users_account_balances[key] = value

   else:
      balance = (value * 10) / (12 * 100)
      value += balance
      users_account_balances[key] = value
pprint(users_account_balances)

account_balance_file.close()

