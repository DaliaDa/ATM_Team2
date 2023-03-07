import Operations as ops
def Withdraw_function():
    Option = input("If you want to WITHDRAW money, press w: ")
    if Option == "w":
        Withdraw = input("Enter the amount you would like to withdraw: ")
        try:
            if int(ops.get_balance()) < int(Withdraw):
                print("Error1")
                quit()
        except:
            print("Not enough money")
            quit()
        print(Withdraw, "Eur have been withdrawn from your account")
    Exit = input("Would you like to exit? y/n: ")
    if Exit == "y":
        print("Thank you for Using ATM. Please take your card.")
    else:
        print("Choose another operation")




Withdraw_function()