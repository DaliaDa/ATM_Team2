# import Deposit
# import Operations
# import Dalia_withdraw
# import receipt


pin1=int(1234)
balance = 378

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
            print("Choose what action you would like to preform, by pressing the correct number.")
            print("(1)Deposit\t (2) Withdraw")
            dowhat = input()
            match dowhat:
                case "1":
                case "2":




    case "2":
        print("Sveiki!\n")