import Operations as ops

operation = int(input("Enter 1 to deposit\n"))
if operation ==1: #what will be the operation #?
    amount_deposit = input("Please insert banknotes in the ATM (Eur 5, Eur 10, Eur 20, Eur 50, Eur 100 bills are accepted) and Enter the amount of deposit:\n ")
    deposit = 0
    try:
        deposit = int(amount_deposit)
    except:
        print("Error, please enter numeric value")
        quit()
    try:
        if deposit % 5 == 0 or deposit % 10 == 0 or deposit % 20 == 0 or deposit % 50 == 0 or deposit % 100 == 0:
            print("All Ok")
        else:
            raise ValueError("Invalid value")
    except ValueError:
        print("Error, invalid banknote amount. ATM accepts 5, 10, 20, 50, 100 Eur bills")
        quit()

    ops.deposit(deposit)
    print(
        f"You have deposited EUR {amount_deposit} to your account. Your new balance is EUR"
        f" {ops.get_balance() + deposit}")

print(ops.get_balance()) #Still has problems with this amount as this is inital 100 form ops file....

