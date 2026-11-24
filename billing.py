'''
    Authors     : Jesse & Diego & Warren Nixon
    Date        : Oct. 31, 2026
    Course      : CSCI-1220-A01-Python: Python
    Module      : budget.py
    Description : Runs the Bills, Income and Subscriptions lists and the Remaining Amount page (saved in the browser)
'''

import json
from pyscript import document, window

PAGE = document.body.getAttribute("data-list") # Which page it is: bills, income, subs or remainder
STORAGE_KEY = f"budget-{PAGE}" # Each list is saved in the browser under its own name so it is still there on the next page

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


def money(value): # Shows a number as dollars
    if value < 0:
        return f"-${abs(value):,.2f}"
    return f"${value:,.2f}"


def load_list(key): # Gets a saved list of (name, price)
    saved = window.localStorage.getItem(key)

    if not saved: # Nothing saved yet
        return []
    try:
        return [(name, float(price)) for name, price in json.loads(saved)]
    except (ValueError, TypeError):
        return []

def save_list(): # Saves the list so the other pages can use it
    window.localStorage.setItem(STORAGE_KEY, json.dumps(items))

def get_balance(): # Gets the saved bank balance
    saved = window.localStorage.getItem("bank-balance")

    if not saved:
        return None
    try:
        return float(saved)
    except ValueError:
        return None

items = load_list(STORAGE_KEY) # Stores all the items the user wants (name, price)

def show_items(): # This shows everything in the listed numbered from what they entered first with the name and the price next to it
    for i, (name, price) in enumerate(items, start=1):
        print(f"{i}. {name}: {money(price)}")

def view_list():
    if items: # This shows everything in the listed numbered from what they entered first if they have stuff in it
        print("\nYour list:")
        show_items()
        total = sum(price for name, price in items) # Totals up all the money everything cost
        print(f"Total: {money(total)}") # Prints the total to the users

    else: # Only runs if they have nothing in the list
        print("List is empty")

def list_total(name): # Adds up one of the lists (bills, income or subs)
    if name == PAGE:
        return sum(price for item_name, price in items)
    return sum(price for item_name, price in load_list(f"budget-{name}"))

def update_balance():
    left = document.getElementById("balance-left")

    if left is None: # Only the Bills page has this
        return

    balance = get_balance() # Uses the balance that was saved with the button

    if balance is None: # Never set
        left.textContent = "Enter your bank balance to see it with this list"

    else:
        income = list_total("income")
        total = balance + income # The bank balance with the income added
        bills = list_total("bills")
        subs = list_total("subs")
        result = total - bills - subs # What is left after the bills and the subscriptions

        left.textContent = f"Bank Balance {money(balance)} | Added Income {money(income)} | Total {money(total)} | Bills {money(bills)} | Subscriptions {money(subs)} | After Bills and Subscriptions {money(result)}"

def set_balance(event=None): # Runs when the Set Balance button is pressed
    box = document.getElementById("bank-balance")
    text = box.value.replace("$", "").replace(",", "").strip() # Gets rid of anything special and keeps the numbers

    if text.replace(".", "", 1).removeprefix("-").isdecimal(): # runs if they only have numbers and lets 1 decimal point and 1 negative sign through
        balance = float(text)
        window.localStorage.setItem("bank-balance", str(balance)) # Saved so the Remaining Amount page can use it
        box.value = ""
        update_balance()

    else: # They typed something that is not a number (or nothing)
        document.getElementById("balance-left").textContent = "Please enter a number for your bank balance"

def setup_balance():
    update_balance() # The box stays empty, the saved balance shows under it

def show_remainder():
    document.getElementById("output").textContent = ""
    balance = get_balance()
    note = ""

    if balance is None: # They never typed a bank balance on the Bills page
        balance = 0.0
        note = "  (not set - enter it on the Bills page)"

    income = sum(price for name, price in load_list("budget-income"))
    bills = sum(price for name, price in load_list("budget-bills"))
    subs = sum(price for name, price in load_list("budget-subs"))
    remaining = balance + income - bills - subs

    print(f"Bank balance:     {money(balance)}{note}")
    print(f"+ Income:         {money(income)}")
    print(f"- Bills:          {money(bills)}")
    print(f"- Subscriptions:  {money(subs)}")
    print("------------------------------")
    print(f"Remaining:        {money(remaining)}")


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
                    item_price = input(f"Enter the price of {item}: $").replace("$", "").replace(",", "").strip() # Gets rid of anything special and keeps the numbers

                    if item_price.replace(".", "", 1).removeprefix("-").isdecimal(): # runs if they only have numbers and lets 1 decimal point and 1 negative sign through
                        price = float(item_price) # let's the price be a mixed number with the filters applied to what the user typed
                        items.append((item, price)) # Adds the item with the price
                        save_list()
                        print(f"Added {item}: {money(price)}")
                        clear_boxes()

                    else:
                        print("Please enter a number that it costs") # if they put any letters or anything special that does not go with numbers

                else:
                    print("You didn't Enter anything") # If they just hit enter with nothing it it says You didn't Enter anything

            case 2: # The user removes what they want to remove in the list
                if not items: # this part runs if there is nothing in the list
                    print("There is nothing to remove.")

                else: # This lets the user choose what number they want to remove
                    num = input("Enter the number from the list to remove: ").strip() # Let's the user choose what to remove (based on the number)

                    if not num.isdecimal(): # If they put sothing that isn't a number
                        print("Please enter a number")

                    else:
                        num = int(num) # This is for it not being a string so it runs fine
                        if 1 <= num <= len(items): # This removes the item for the list (The 1 is because the list they see starts at 1 not zero)
                            removed_name, removed_price = items.pop(num - 1)
                            save_list()
                            print(f"Removed {removed_name} {money(removed_price)} from the list")
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
    update_balance()

if PAGE == "remainder":
    show_remainder()
else:
    view_list()
    setup_balance()
