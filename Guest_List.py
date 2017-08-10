guest = ['Jesus', 'Martin Luther King', 'Michelle Obama', 'Garfield']
print(guest)
guest.remove('Garfield')
print(guest)
for i in guest:
    print('You are invited ' + i)
    print

print("there's a bigger table")

guest.insert(1, 'Taylor')
guest.insert(3, 'Barack Obama')
guest.append('Adele')
guest.append('Check')

for i in guest:
    print('Heres the new list and You are invited ' + i)
    print

print()
print("The reservation cancelled, I can only invite two people")
print()
print(guest)

count = len(guest)

if count != 2:
    for i in guest:
        uninvited = guest.pop()
        print("Sorry you are uninvited " + uninvited)

    for i in guest:
        print('Heres the new list and You are invited ' + i)
        print
