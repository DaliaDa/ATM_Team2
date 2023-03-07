#import Deposit as dep
import Operations as ops
# import Dalia_withdraw
# import receipt


pin1 = ops.get_pin()
balance = ops.get_balance()

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
        print("Welcome!\n")
        pincompare = int(input("Please enter your PIN: ")) # Pin check
        pinbool = pincheck(pincompare, pin1)
        if pinbool == False:
            print("Please contact the bank. \n")
        else:
            print("Choose what action you would like to preform, by pressing the correct letter.")
            print("(D)Deposit\t (W) Withdraw")
            dowhat = input()
            match dowhat:
                case "D":
                    print("Deposit")
                case "W":
                    print("Withdraw")




    case "2":
        print("Sveiki!\n")