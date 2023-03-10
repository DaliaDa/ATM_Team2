import Operations as ops
def deposit_function():
        operation = 1
        amount_deposit = input("Please insert banknotes in the ATM (Eur 5, Eur 10, Eur 20, Eur 50, Eur 100 bills are accepted) and Enter the amount of deposit:\n")
        try:
            deposit = int(amount_deposit)
        except ValueError:
            print("Error, please enter numeric value")
            operation = input("If you would like to try again, type 1. If not, type anything but 1.")
            try:
                operation = int(operation)
                if operation ==1:
                    deposit_function()
                else:
                    return
            except:
                return
        try:
            if deposit % 5 == 0:
                ops.balance += deposit
                ops.deposit(deposit)
                print(f"You have deposited EUR {amount_deposit} to your account. Your new balance is EUR" f" {ops.get_balance()}")
                return
            else:
                raise ValueError("Invalid value")
        except ValueError:
            print("Error, invalid banknote amount. ATM accepts 5, 10, 20, 50, 100 Eur bills")
            operation = input("If you would like to try again, type 1. If not, type anything but 1.")
            try:
                operation = int(operation)
                if operation ==1:
                    deposit_function()
                else:
                    return
            except:
                return











