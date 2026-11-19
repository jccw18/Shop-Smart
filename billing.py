'''
    Authors     : Jesse & Diego & Warren Nixon
    Date        : Oct. 31, 2026
    Course      : CSCI-1220-A01-Python: Python
    Module      : Billing List.py
    Description : Allows the user to create and modify the list to their need
'''

from pyscript import document

def print(*args, end="\n"):
    output = document.getElementById("output")
    output.textContent += " ".join(str(a) for a in args) + end

def input(question=""):
    if question.startswith("Enter an item"):
        box = "item-name"
    elif question.startswith("Enter the price"):
        box = "item-price"
    else:
        box = "remove-num"
    return document.getElementById(box).value

def clear_boxes():
    for box in ("item-name", "item-price", "remove-num"):
        document.getElementById(box).value = ""


items = [] # Stores all the items the user wants


def show_items(): # This shows everything in the listed numbered from what they entered first with the name and the price next to it

    for i, (name, price) in enumerate(items, start=1):
        print(f"{i}. {name}: ${price:,.2f}")

def view_list():

    if items: # This shows everything in the listed numbered from what they entered first if they have stuff in it

        print("\nYour list:")
        show_items()

        total = sum(price for name, price in items) # Totals up all the money everything cost
        print(f"Total: ${total:,.2f}") # Prints the total to the users

    else: # Only runs if they have nothing in the list

        print("List is empty")


def option_clicked(event=None):

    document.getElementById("output").textContent = "" 
    choose = event.target.getAttribute("data-choice")

    if not choose.isdigit(): # If it is not a number it will run this instead of a error

        print("Please choose 1, 2, 3, or 4")

    else: # If they choose a valid number

        choose = int(choose) # This is not really needed it is just to make the match case look better (if you do change it put "" for the match case)

        match choose:

            case 1: # Adds the item they want and makes what they type without any white space

                item = input("Enter an item to add: ").strip() # They could put anything

                if item: # runs if they put a item in
                    item_price = input(f"Enter the price of {item}: $").strip().replace("$", "").replace(",", "") # Gets rid of anything special and keeps the numbers

                    if item_price.replace(".", "", 1).replace("-", "", 1).isdigit(): # runs if the only have numbers and lets the 1 negative sign and 1 decmail through

                        price = float(item_price) # let's the price be a mixed number with the filters applied to what the user typed
                        items.append((item,price)) # Adds the item with the price
                        element = document.getElementById("bank-balance")
                        raw_text = element.value.strip().replace("$", "").replace(",", "")

                        try:
                            numeric_value = float(raw_text)
                            updated_value = numeric_value - price  # Or + when refunding
                            element.value = f"{updated_value:.2f}"
                        except ValueError:
                            pass
                        print(f"Added {item}: ${price:,.2f}")
                        clear_boxes()

                    else:

                        print("Please enter a number that it costs") # if they put any letters or anything special that does not go with numbers

                else:

                    print("You didn't Enter anything") # If they just hit enter with nothing it it says You didn't Enter anything

            case 2: # The user removes what they want to remove in the list

                if not items: # this part runs if there is nothing in the list

                    print("There is nothing to remove.")

                else: # This lets the user choose what number they want to remove

                    num = input("Enter the number from the list to remove: ") # Let's the user choose what to remove (based on the number)

                    if not num.isdigit(): # If they put sothing that isn't a number

                        print("Please enter a number")

                    else:

                        num = int(num) # This is for it not being a string so it runs fine
                        if 1 <= num <= len(items): # This removes the item for the list (The 1 is because the list they see starts at 1 not zero)

                            removed_name, removed_price = items.pop(num - 1)
                            element = document.getElementById("bank-balance")
                            raw_text = element.value.strip().replace("$", "").replace(",", "")

                            try:
                                numeric_value = float(raw_text)
                                updated_value = numeric_value + removed_price  # Or + when refunding
                                element.value = f"{updated_value:.2f}"
                            except ValueError:
                                pass 
                            print(f"Removed {removed_name} {removed_price:,.2f} from the list")
                            clear_boxes()

                        else: # If the user enters any number that is not listed to them

                            print("Invalid number (Number was not on list).")

            case 3: # This shows the user everything in the list

                pass

            case 4: # This lets the user exit the list

                print("You ended the list")

            case _: # This is if they eneter anything that is not offered (just incase something fails)

                print("Please choose 1, 2, 3, or 4")

    view_list()


view_list()
