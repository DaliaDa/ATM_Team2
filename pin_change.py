import Operations as ops
# remove while boop
def pinchange():
        operation = 0
        newpin = input("Please enter your new pin using only 4 numeric values: ")
        try:
            newpin = int(newpin)
            l = str(newpin)
            l = len(l)
            if l==4:
                newpin1= input("Please re-enter the new pin: ")
                try:
                    newpin1 = int(newpin1)
                    if newpin == newpin1:
                        ops.pincode = newpin
                        print("Your pin has been successfully changed.")
                        return
                    else:
                        operation = input("The pin entered does not match the previously entered value. You'll have to perform the entire process again. If you would like to do so please enter 1, if not, enter whatever.")
                        try:
                            operation = int(operation)
                            if operation == 1:
                                pinchange()
                            else:
                                return
                        except ValueError:
                            return
                except:
                    raise ValueError("Invalid value")
            else:
                raise ValueError("Invalid value")
        except ValueError:
            operation = input("The entered value does not meet the criteria. If you would like to try again, press 1, if not enter anything else.")
            try:
                operation = int(operation)
                if operation == 1:
                    pinchange()
                else:
                    return
            except ValueError:
                return


