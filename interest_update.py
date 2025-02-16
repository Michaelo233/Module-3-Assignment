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

   # 5% interest added.
   if value >= 5000:
      interest = (value * 5) / (12 * 100)
      value += interest
      users_account_balances[key] = value

   # 2.5% interest added.
   elif value >= 1000:
      interest = (value * 2.5) / (12 * 100)
      value += interest
      users_account_balances[key] = value

   # 1% interest added.     
   elif value > 0:
      interest = (value * 1) / (12 * 100)
      value += interest
      users_account_balances[key] = value

   # 10% interest charged.
   elif value < 0:
      interest= (value * 10) / (12 * 100)
      value += interest
      users_account_balances[key] = value

   # 0% interest charged or added.  
   else :
      value = value
      users_account_balances[key] = value

pprint(users_account_balances)

account_balance_file.close()

field_names = ['Account', 'Balance']

with open("updated_balance_MO.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Account", "Balance"])

    # Write the data
    for key, value in users_account_balances.items():
        writer.writerow([key, value])