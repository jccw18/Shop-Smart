'''
    Authors     : Jesse & Diego & Warren Nixon
    Date        : Oct. 31, 2026
    Course      : CSCI-1220-A01-Python: Python
    Module      : Billing List.py
    Description : Allows the user to create and modify the list to their need
'''

items = [] # Stores all the items the user wants

# This class lets the user see and change the list as needed
def list_info():
    print("\nList Settings")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View list")
    print("4. Quit")

def show_items():
    for i, (name, price) in enumerate(items, start=1):
        print(f"{i}. {name}: ${price:.2f}")

while True: # Runs until the user is done editing the list
    list_info() # Shows the user the info about the list
    choose = input("Choose an option (1-4): ") # The user chooses what they want to do to the list based on the options (in the class, list_info) they were given

    if not choose.isdigit(): # If it is not a number it will run this instead of a error
        print("Please choose 1, 2, 3, or 4")
    else: # If they choose a valid number
        choose = int(choose) # This is not really needed it is just to make the match case look better (if you do change it put "" for the match case)
        match choose:
            case 1: # Adds the item they want and makes what they type without any white space
                item = input("Enter an item to add: ").strip()

                if item:
                    item_price = input(f"Enter the price of {item}: $").strip().replace("$", "")
                    
                    if item_price.replace(".", "", 1).isdigit():
                        price = float(item_price)
                        items.append((item,price))
                        print(f"Added {item}: ${price:.2f}.")
                    else:
                        print("Please enter a number that it costs")
                else:
                    print("You didn't Enter anything") # If they just hit enter with nothing it it says You didn't Enter anything

            case 2: # The user removes what they want to remove in the list
                if not items: # this part runs if there is nothing in the list
                    print("There is nothing to remove.")
                else: # This shows everything in the list and lets the user choose what number they want to remove
                    show_items()

                    num = input("Enter the number from the list to remove: ") # Let's the user choose what to remove (based on the number)

                    if not num.isdigit(): # If they put sothing that isn't a number
                        print("Please enter a number")
                    else: 
                        num = int(num) # This is for it not being a string so it runs fine
                        if 1 <= num <= len(items): # This removes the item for the list (The 1 is because the list they see starts at 1 not zero)
                            
                            removed_name, removed_price = items.pop(num - 1)
                            print(f"Removed {removed_name} {removed_price:.2f} from the list")

                        else: # If the user enters any number that is not listed to them
                            print("Invalid number (Number was not on list).")

            case 3: # This shows the user everything in the list
                if items: # This shows everything in the listed numbered from what they entered first
                    print("\nYour list:")

                    show_items()

                    total = sum(price for name, price in items)
                    print(f"Total: ${total:.2f}")

                else: # Only runs if they have nothing in the list
                    print("List is empty")
    
            case 4: # This lets the user exit the list
                print("You ended the list")
                break

            case _: # This is if they eneter anything that is not offered (just incase something fails)
                print("Please choose 1, 2, 3, or 4")
