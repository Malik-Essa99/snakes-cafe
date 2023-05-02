menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak Meat", "Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Beverages": ["Coffee", "Tea", "Unicorn Tears"],
}

order = {}


def welcome():
    print(
        """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""
    )


def displayMenu(menu):
    for category in menu:
        print("")
        print(category)
        print("----------" + "\n")
        for item in menu[category]:
            print(item)
            print("")

    print(
        """
***********************************
** What would you like to order? **
***********************************
"""
    )


def user_insertion():
    user_input = input(">")
    words = user_input.split(" ")
    for i in range(len(words)):
        words[i] = words[i].title()
    user_input = " ".join(words)
    return user_input


def main():
    customer_order = user_insertion()
    while customer_order != "Quit":
        if any(customer_order in values for values in menu.values()):
            if customer_order in order:
                order[customer_order] += 1
            else:
                order[customer_order] = 1
            print(
                f"** {order[customer_order]} order of {customer_order} has been added to your meal **"
            )
        else:
            print("sorry we dont have this item !")

        customer_order = user_insertion()

    end_application()


def end_application():
    print("thanks for using snakes cafe application !")


# invoke the function
# if __name__=="__main__":
welcome()
displayMenu(menu)
main()
