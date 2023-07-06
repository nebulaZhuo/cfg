prices = {"TV": 1000, "Phone": 50, "Alarm Clock": 25}
balance = 100

class ThreeFailedAttempts(Exception):
    pass

def purchased(item, balance):
    if balance >= prices.get(item):
        return True
    else:
        return False

def goodbye_greeting(item):
    print(f"Here’s your {item}!\n")
    print("Thanks for coming to The Store. Come again!")
    print("*******************************************")
    exit(0)

def retry_purchase(item, balance, attempts=1):
    if attempts == 3:
        raise ThreeFailedAttempts("Payment failed 3 times. Please exit the store.")
    more_money = input("Sorry your payment failed, do you have any more money? (Y/N)")
    if more_money == "Y":
        try:
            balance += float(input("How much?"))
        except ValueError:
            raise ValueError("Invalid input, exiting store")
    if purchased(item, balance):
        goodbye_greeting(item)
    else:
        attempts += 1
        retry_purchase(item, balance, attempts)


def greeting():
    print("Welcome to The Store!")
    print("We currently have the following items:")
    for item in prices:
        print(f"{item} - £{prices.get(item)}")
    try:
        choice = input("\nWould you like to buy anything?\nEnter 'exit' to exit the shop\n")

        if choice == "exit":
            exit(0)
        elif choice in prices.keys():
            if purchased(choice, balance):
                goodbye_greeting(choice)
            else:
                retry_purchase(choice, balance)
        else:
            raise ValueError("Not a valid answer, please return and try again")
    except (ValueError, ThreeFailedAttempts) as exception:
        print(exception)
    else:
        print("Thank you for your purchase!")
    finally:
        print("Exiting the store.")

greeting()

