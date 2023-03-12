import Operations as ops
def withdraw_function():
   print("Your balance is", ops.get_balance(), "Eur")
   process = 1
   while process == 1:
      Withdraw = input("Enter the amount you would like to withdraw: ")

      try:
         Withdraw = int(Withdraw)
         if int(ops.get_balance()) < int(Withdraw):
            print("You do not have enough resources to support this withdraw request. \n")
            process = input("Would you like to preform another withdrawal request? If yes, please type 1. Else, type anything else. \n")
            try:
               process = int(process)
               if process == 1:
                  withdraw_function()
               else:
                  return
            except ValueError:
               return
         elif int(ops.get_balance()) >= int(Withdraw):
            if Withdraw % 5 != 0:
               print("Please keep in mind that you can only withdraw even amounts consisting of 5, 10, 20, 50, 100 euro banknotes. \n")
               process = input("Would you like to preform another withdrawal request? If yes, please type 1. Else, type anything else. \n")
               try:
                  process = int(process)
                  if process == 1:
                     withdraw_function()
                  else:
                     return
               except ValueError:
                  return
            elif Withdraw%5==0:
               ops.balance -= Withdraw
               print(Withdraw, " EURO has been withdrawn from your balance. Your current balance is ", ops.balance, " EURO.")
               process = input("Would you like to preform another withdrawal request? If yes, please type 1. Else, type anything else. \n")
               try:
                  process = int(process)
                  if process == 1:
                     withdraw_function()
                  else:
                     return
               except ValueError:
                  return
      except ValueError:
        print("Please enter a numeric value.")
        withdraw_function()









