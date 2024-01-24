# Import required modules.
import math

# Main menu.
def mainmenu():
    # Using a while loop to control error handling until matching input for the menu is entered from the user.
    while (True):
        print("-"*60)
        print ("\ninvestment - to calculate the amount of interest you'll earn on your investment.") 
        print ("bond       - to calculate the amount you'll have to pay on a home loan.")
        print ("\n-1         - to return to the main menu at any stage.")
        print ("\n")
        print("-"*60)

        # User Defined Variable for menu direction.
        # Use .lower() to help handle any errors on the input.

        choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()


        # Call the relevant function for the input.
        if choice == "investment":
            investment_calculator()
        elif choice == "bond":
            bond_calculator()
        elif choice == "-1":
            mainmenu()
        else:
            #loop returns back to the start if incorrect input
            print("\n⚠ Error,invalid input detected, please check your spelling and try again. ⚠\n")


def investment_calculator():
    print()
    print("-"*60)
    print ("Investment Calculator")
    print("-"*60)

    # Define user input variables.
    # Use While loop with if block to handle errors until appropriate input is met.
    while True:
        amount = (input("\nPlease enter the amount you wish to deposit £ "))
        if amount.isalpha():
            print(f"""\n⚠ {amount} is invalid input. Please try again.
                \rOr enter '-1' to return to the main menu ⚠\n""")
            continue
        elif amount == "-1":
            mainmenu()
        elif amount.isnumeric():
            deposit = float(amount)

        # Repeat previous loop for user input variables.
        while True:  
            percentage_rate = (input("\nPlease enter your interest rate here as a solid number. "))
            if percentage_rate.isalpha():
                print(f"""\n⚠ {percentage_rate} is invalid input. Please try again.
                    \rOr enter '-1' to return to the main menu. ⚠\n""")
                continue
            elif percentage_rate == "-1":
                mainmenu()
            elif percentage_rate.isnumeric():
                percentage = float(percentage_rate) / 100 # Dividing knowing the input is percentalie.
        
            # Repeat previous loop for user input variables.
            while True:
                time = (input("\nHow many years do you intend on investing? "))
                if time.isalpha():
                    print(f"""\n⚠ {time} is invalid input. Please try again.
                          \rOr enter '-1' to return to the main menu. ⚠\n""")
                    continue  
                elif time == "-1":
                    mainmenu()
                elif time.isnumeric():
                    years = int(time)

                # Similar loop to work with information gathered.
                # Allow user to choose type of interest.
                # Handle relevant errors that can occur.
                while True:
            
                    interest = input("\nPlease select either 'simple' or 'compound' interest: ").lower()
            
                    # Run down this line if the input matches.
                    if interest == "simple": 
                        print()
                        print("-"*60)
                        print ("Interest Calculator (simple)")
                        print("-"*60)

                        # Create the local variable and perform the calculations.
                        # Overwrite the local variable with the result.
                        simple_interest = deposit * (1 + percentage * years)
                        simple_interest = "{:.2f}".format(simple_interest) 

                        # Display the information back to the user in a readable manner.
                        print()
                        print (f"""After {years} years. 
                            \rThe return on your investment will be 
                            \r£{simple_interest}\n""")
                        print ("-"*60)
                        print()
                        mainmenu()

                    # Programme runs here if input matches.        
                    elif interest == "compound":
                        print()
                        print("_"*60)
                        print("Interest Calculator (compound)")
                        print("-"*60)

                        # Declared local variables, determined by user input.
                        # Perform calculations and store result in original variable.
                        compound_interest = float(deposit * math.pow((1+percentage),years))
                        compound_interest = "{:.2f}".format(compound_interest)

                        # Display Information back to user in a readable manner.
                        print ()
                        print (f"""After {years} years. 
                            \rThe Return on your investment will be 
                            \r£{compound_interest}\n""")
                        print ("-"*60)
                        print()
                        mainmenu()

                    # Exit function.    
                    elif interest == "-1":
                        mainmenu()
                    
                    else:
                    # Run if any other input is detected, restarting loop.
                        print ()
                        print ("""⚠ Error,invalid input detected, please check your spelling and try again.
                            \rOr enter '-1' to return to the main menu. ⚠\n""")


def bond_calculator():      
    # called if choice matches 'bond'.
    print()
    print("-"*60)
    print ("Bond Calculator")
    print("-"*60)

    # Declare local Variables to use within the loop.
    # Defined by user input.
    # Dividing the percentage input for calculations performed later.
    # Use while True blocks in conjunction with Try Except to make sure user input is valid.

    while True:
        property = (input("\nWhat is the value of the property? £ "))
        if property.isalpha():
             print(f"""\n⚠ {property} is invalid input. Please try again.
                   \rOr enter '-1' to return to the main menu. ⚠\n""")
             continue
        elif property == "-1":
            mainmenu()
        elif property.isnumeric():
            value = float(property)

        while True:
            property_rate = (input("\nPlease enter the interest rate as a solid number. "))
            if property_rate.isalpha():
                print(f"""\n⚠ {property_rate} is invalid input. Please try again.
                      \rOr enter '-1' to return to the main menu. ⚠\n""")
                continue
            elif property_rate == "-1":
                mainmenu()
            elif property_rate.isnumeric():
                rate = float(property_rate) / 100 / 12

            while True:
                property_months = (input("\nHow many months are you planning to take to repay the bond? "))
                if property_months.isalpha():
                    print(f"""\n⚠ {property_months} is invalid input. Please try again.
                          \r Or enter '-1' to reurn to the main menu. ⚠\n""")
                    continue
                elif property_months == "-1":
                    mainmenu()
                elif property_months.isnumeric():
                    months = int(property_months)

                # Declared local variables, determined by user input.
                # Perform calculations and store result in original variable.
                repayment = (rate * value)/(1 -(1 + rate)**(-months))
                repayment = "{:.2f}".format(repayment)

                # Display Information back to user in a readable manner.
                print ()
                print ("-"*60)
                print (f"""At current value of £{value}. 
                    \rYour monthly repayments for the next {property_months} months will be
                    \r£{repayment}\n""")
                print ("-"*60)
                print()
                mainmenu()


mainmenu()