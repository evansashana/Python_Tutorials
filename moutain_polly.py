responses = {}

# Set a flag to indicate that polling is active
polling_active = True
"""Display a simple greeting."""
while polling_active:
    # Prompt user for name and response
    name = input("\n Whats your name? ")
    response = input("\n Which mountain would you like to climb someday ")

    # Store the response in dictionary
    responses[name] = response

    # Find out if anyone else wants to take the poll
    repeat = input("Would you like someone else to take the poll y/n ")
    if repeat == 'n':
        polling_active = False

# Polling is done, print out responses
print("\n ---------Polling Results--------- ")
for name, response in responses.items():
    print(name + " wants to climb " + response)

print(responses)