alien_color = ['green', 'yellow', 'red']

for colors in alien_color:
    if colors == 'green':
        points = 5
    elif colors == 'red':
        points = 15
    else:
        points = 10

    print('Player you earned ' + str(points) + ' points.')