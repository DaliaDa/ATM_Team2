
import Operations as ops
# import Dalia_withdraw
# import receipt


pin1 = ops.get_pin()

def pincheck(checkp, realp): # function that checks pin code
    times = int(0)
    if checkp != realp:
        while checkp != realp:
            times = times + 1
            if times == 3:
                print("Your account has been BLOCKED.\n")
                return False
            else:
                print("Pin is incorrect. You can re-enter it ", 3-times, " time(s).\n")
                checkp = int(input())
        return True
    else:
        return True




print("Please choose a language option you'd like to continue with by pressing the number by the language: \n")
lang = input("(1)English\t (2)Latvian \n")
match lang:
    case "1":
        process = int(1)
        pincompare = int(input("Please enter your PIN: ")) # Pin check
        pinbool = pincheck(pincompare, pin1)
        if pinbool == False:
            print("Please contact the bank. \n")
        else:
            process = 1
            while process == 1:
                print("Choose what action you would like to preform, by pressing the correct letter.")
                print("(D)Deposit\t (W) Withdraw\t (R)Receipt\t (B)Balance\t (P)Change PIN")
                dowhat = input()
                dowhat = dowhat.upper()
                match dowhat:
                    case "D":
                        from Deposit import deposit_function
                        deposit_function()
                        process = input("If you would like to preform another operation, press 1. If not, enter whatever.")
                        try:
                            process = int(process)
                            if process ==1:
                                continue
                            else:
                                quit()
                        except:
                            quit()
                    case "W":
                        from Dalia_withdraw import withdraw_function
                        withdraw_function()
                        process = input("If you would like to preform another operation, press 1. If not, enter whatever.")
                        try:
                            process = int(process)
                            if process ==1:
                                continue
                            else:
                                quit()
                        except:
                            quit()
                    case "R":
                        from receipt import receipt
                        receipt()
                        process = input("If you would like to preform another operation, press 1. If not, enter whatever.")
                        try:
                            process = int(process)
                            if process ==1:
                                continue
                            else:
                                quit()
                        except:
                            quit()
                    case "B":
                        print("Your current balance is ",ops.get_balance(), " EURO.")
                        process = input("If you would like to preform another operation, press 1. If not, enter whatever.")
                        try:
                            process = int(process)
                            if process ==1:
                                continue
                            else:
                                quit()
                        except:
                            quit()
                    case "P":
                        pin1 = ops.get_pin()
                        pincompare = int(input("Please enter your PIN: ")) # Pin check
                        pinbool = pincheck(pincompare, pin1)

    case "2":
        print("Sveiki!\n")