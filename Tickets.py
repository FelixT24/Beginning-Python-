SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100  

# create a calculate_price function. It takes number of tickets and return 
# num_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    # Create a new constant for the 2 dollar service charge
    # Add service charge
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like {}?".format(name))
    
    # Expect a ValueError to happen and handle it appropriately...remember to test it out
    try:
        num_tickets = int(num_tickets)
        # Raise a value error if request is for more tickets if for more tickets than available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:
        total = calculate_price(num_tickets)
        print("Your total will be ${}".format(total))
        should_proceed = input('Do you want to proceed Y/N?')

        if should_proceed.lower() == 'y':
            print("SOLD!")
            # TODO: Gather credit card informtation and process it
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}.".format(name))
        
print('Sorry the tickets are all sold out!')