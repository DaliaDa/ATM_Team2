import Operations as ops
yes_or_not = input("Do you want a receipt? (Y/N): ")
if yes_or_not == "N":
   print("Go back.");
else:
   def options(number):
      for x in number:
         print(x)

   variants=["1.Show a receipt on the screen" , "2.Print a receipt on paper" , "3.Receive SMS with a receipt" , "4.Receive an email with receipt"]

   options(variants)

   lang = input("Please, choose an option. Enter a number: ")

   match lang:
      case"1":
         print(f"Your  balance is EUR {ops.get_balance()}")

      case"2":
         print("Take your receipt.")

      case"3":
         while True:
            phoneNumber = input("Please, enter your phone number: ")
            answer = input("Are you sure that your phone number is correct? (Y/N): ")

            if answer == "N":
               print("Please, enter your phone number again." )
            elif answer == "Y":
               print("SMS has been successfully sent.")
               break

      case"4":
         while True:
            email = input("Please, enter your email address: ")
            answer2 = input("Are you sure that your email address is correct? (Y/N): ")

            if answer2 == "N":
               print("Please, enter your email address again." )
            elif answer2 == "Y":
               print("An email has been successfully sent.")
               break
