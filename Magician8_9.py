magicians = ['davinci', 'picasso', 'shana']


def show_magicians(magicians):
    for names in magicians:
        print(names.title())


def make_great(magicians):
    for names in magicians:
        print(names.title() + " The Great")


make_great(magicians[:])
show_magicians(magicians)
