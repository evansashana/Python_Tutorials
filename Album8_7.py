def make_album(artist_name, album_title):
    # Build album dictionary

    album = {'artist': artist_name, 'title': album_title.title()}
    return album


while True:
    print("\nPlease tell your favorite albums:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("artist: ")
    if artist_name == 'q':
        break
    album_title = input('Album title: ')
    if album_title == 'q':
        break
    album = make_album(artist_name, album_title)
    print("\nFavorite Album is by " + album['artist'] + " " + album['title'] +
          "!")


    # first = make_album('J. Cole', '4 your eyez only')
    # second = make_album('Jay-Z', '4:44')
    # third = make_album('21 Savage', 'issa album')
    # fourth = make_album('Cardi B', 'Bodak Yellow', '2')


    # print(first)
    # print(second)
    # print(third)
    # print(fourth)
