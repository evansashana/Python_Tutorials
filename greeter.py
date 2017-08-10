def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title())


greet_user('jesse')


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Infinite Loop
names = []

while True:
    print("\nPlease tell me your name: ")
    print("Enter q if you want to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    format_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + format_name + "!")

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
# formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")