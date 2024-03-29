# Create a function named 'account_balance'
# This function is used to print the account balance.
def account_balance(acc_balance):   
    print("Your current balance: $%.2f" %acc_balance)

# Create a function named 'deposit_amount'
# This function is used to calcuate the deposit
# amount and display the final balance.
def deposit_amount(acc_balance):
    deposit_amount = float(input("How much would you like to deposit? "))
    balance = acc_balance + deposit_amount
    print("Deposit amount was $%.2f, current balance is $%.2f" % (deposit_amount, balance))   

# Create a function named 'withdrawal_amount'
# This function is used to withdrawal amount from the
# main balance and displays the final balance.
def withdrawal_amount(acc_balance):
    withdraw_amount = float(input("How much would you like to withdraw today? "))
    if withdraw_amount > acc_balance:
        print("$%.2f is greater that your account balance of $%.2f" % (withdraw_amount, acc_balance))
    else:
        balance = acc_balance - withdraw_amount
        print("Withdrawal amount was $%.2f, your current balance is $%.2f" % (withdraw_amount, balance))

# Opening balance
acc_balance = float(500.25)
userchoice = input ("What would you like to do?\n")

# Create an 'if' statement to check the user input.
if (userchoice == 'D'):
    deposit_amount(acc_balance)
elif (userchoice == 'W'):
    withdrawal_amount(acc_balance)
elif (userchoice == 'B'):
    account_balance(acc_balance)
elif (userchoice == 'Q'):
  print('thank you for banking with us.')

else:
    print('Invalid Input!')