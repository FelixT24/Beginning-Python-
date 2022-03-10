# Create a new empty list named shopping_list
shopping_list = []

# Create function named add_to_list that declares a parameter named item
    # add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    # Notify the user that the item was added and state the number of items in the list currently
    print("Added! List has {} items.".format(len(shopping_list)))

# Define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

def show_help():
    print("What should we pick up at the store?")
    # Multi-line print 
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this to help.
    Enter 'SHOW' to display entire list.
    """)

show_help()
while True: 
    new_item = input("> ")

    if new_item == 'DONE':
        # 'break' will break out of the loop
        break
    elif new_item == 'HELP':
        show_help()
        # 'continue' will jump back to beginning of while loop
        continue

    # Enable the show command to show the list. DON'T forget to update the help documentation
    # HINT: Make sure to run it.
    elif new_item == 'SHOW': 
        show_list()
        continue

    # Call add_to_list with new item as an argument
    add_to_list(new_item)

show_list()
    