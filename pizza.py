def make_pizza(size, *toppings):
    print("\n Making a " + str(size) + "-inch piza with the followig "
                                       "toppings:")
    for topping in toppings:
        print ("- " + topping)
        