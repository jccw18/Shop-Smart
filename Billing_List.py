items = [] # Stores all the items the user wants

# This class lets the user see and change the list as needed
def list_info():
    print("\nList Settings")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View list")
    print("4. Quit")

while True: # Runs until the user is done editing the list
    list_info() # Shows the user the info about the list
    choose = int(input("Choose an option (1-4): ")) # The user chooses what they want to do to the list based on the options (in the class, list_info) they were given (Only problem is that if they put a string it runs into a error)

    match choose:
        case 1: # Adds the item they want and makes what they type in all lowercase
            item = input("Enter an item to add: ").strip()

            if item:
               items.append(item)
               print(f"Added {item}.")
            else:
                print("You didn't Enter anything") # If they just hit enter with nothing it it says You didn't Enter anything

        case 2: # The user removes what they want to remove in the list (Also runs into a error if a string is entered)
            if not items: # this part runs if there is nothing in the list
                print("There is nothing to remove.")
            else: # This shows everything in the list and lets the user choose what number they want to remove
                for i, item in enumerate(items, start=1):
                    print(f"{i}. {item}")
                num = int(input("Enter the number from the list to remove: ")) # This is the part that can give an error

                if 1 <= num <= len(items): # This removes the item for the list (The 1 is because the list they see starts at 1 not zero)
                    removed = items.pop(num - 1)
                    print(f"Removed {removed} from the list")
                else: # If the user enters any number that is not listed to them
                    print("Invalid number.")

        case 3: # This shows the user everything in the list
            if items: # This shows everything in the listed numbered from what they entered first
                print("\nYour list:")

                for i, item in enumerate(items, start=1):
                    print(f"{i}. {item}")
                else: # Only runs if they have nothing in the list
                    print("List is empty")
    
        case 4: # This lets the user exit the list
            print("You ended the list")
            break

        case _: # This is if they eneter anything that is not offered
            print("Please choose 1, 2, 3, or 4")