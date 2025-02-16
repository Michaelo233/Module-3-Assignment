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