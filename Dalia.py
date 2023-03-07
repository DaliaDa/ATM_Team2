UserChoice = input("If you want to WITHDRAW money, press w: ")
if UserChoice == "w":
    UserWithdraw = input("Enter the amount you would like to withdraw: ")
    print(UserWithdraw, "Eur have been withdrawn from your account")
UserExit = input("Would you like to exit? y/n: ")
if UserExit == "y":
    print("Thank you for Using ATM. Please take your card.")
else:
    print("Choose another operation")