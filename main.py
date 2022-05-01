card_details = {"un": ["abc", "xyz", "pqr"], "pin": [1234, 5678, 1357], "balance": [10000, 15000, 20000]}


def display_balance():
    print("Account balance is : {}".format(card_details["balance"][card_details["un"].index(entered_un)]))
    print("----------------------------------------------------------------------------------------------")


def cash_withdraw(amount):
    global card_details

    if amount > card_details["balance"][card_details["un"].index(entered_un)] - 1000:
        print("Your balance is insufficient")
        display_balance()
    elif amount > 100000:
        print("Maximum withdrawal amount is 100000")
        display_balance()
    else:
        card_details["balance"][card_details["un"].index(entered_un)] -= amount
        display_balance()


def cash_deposit(amount):
    global card_details
    card_details["balance"][card_details["un"].index(entered_un)] += amount
    display_balance()


def check():
    global flag
    print("Do you want to do anything more? (y/n)")
    do = input()

    if do == "n":
        print("Have a nice day!")
        flag = False


entered_un = input("Please enter your username:")
if entered_un in card_details["un"]:
    entered_pin = int(input("Please enter your card pin number:"))
    count = 0
    while entered_pin != card_details["pin"][card_details["un"].index(entered_un)]:
        if count == 5:
            print("You have tried the maximum number of times. Enter your card again and try")
            break
        print("Entered pin is incorrect. You have " + str(5 - count) + " more times to try")
        print("**************************************************************************")
        entered_pin = int(input("Check again and enter your correct card pin number:"))
        count = count + 1

    else:
        print("You have accessed to the machine")
        flag = True
        while flag:
            print("Select what you want to do")
            print("Account balance : Press 1")
            print("Cash withdrawal : Press 2")
            print("Cash deposit    : Press 3")

            choice = input()

            if choice == "1":
                display_balance()
                check()

            elif choice == "2":
                print("Enter the amount you need to withdraw")
                value = float(input("Amount: "))
                cash_withdraw(value)
                check()

            elif choice == "3":
                print("Enter the amount you need to deposit")
                value = float(input("Amount: "))
                cash_deposit(value)
                check()

else:
    print("Entered username is incorrect. You have to enter the card again and enter a valid username")