import Operations as ops
def Withdraw_function():
   Option = input("If you want to WITHDRAW money, press w: ")
   if Option == "w":
      print("Your balance is", ops.get_balance(), "Eur")
      Withdraw = input("Enter the amount you would like to withdraw: ")

      try:
         if int(ops.get_balance()) < int(Withdraw):
            print("Error1")
            quit()
      except:
         print("Not enough money")
         quit()

      print(Withdraw, "Eur have been withdrawn from your account")
      print("Your new balance is", ops.get_balance() - int(Withdraw), "Eur")
   Exit = input("Would you like to EXIT? y/n: ")
   if Exit == "y":
      print("Thank you for Using ATM. Please take your card.")
   else:
      print("Choose another operation")


Withdraw_function()




