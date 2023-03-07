import Operations as ops

operation = int(input("Enter 1 to deposit\n"))
if operation ==1: #what will be the operation #?
    amount_deposit = input("Please insert banknotes in the ATM (Eur 5, Eur 10, Eur 20, Eur 50, Eur 100 bills are accepted) and Enter the amount of deposit:\n ")
    try:
        deposit = int(amount_deposit)
    except:
        print("Error, please enter numeric value")
        quit()

    ops.deposit(deposit)
    print(f"You have deposited EUR {amount_deposit} to your account. Your new balance is EUR {ops.get_balance() + deposit}")


#Still need to figure this one out - has asked Edgars how to add second try statement...
#try:
#    if amount_deposit%5==0 and amount_deposit%10==0 and amount_deposit%20==0 and amount_deposit%50==0 and amount_deposit%100==0:
#        except:
#    print("Error, invalid banknote amount. ATM accepts 5, 10, 20, 50, 100 Eur bills")
#    quit()