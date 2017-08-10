rivers = {'nile': 'egypt', 'mississippi': 'united states', 'fake': 'israel'}

for k, v in rivers.items():
    print("The " + k.title() + " runs through " + v.title())

print()
print("these are the countries: ")
for v in rivers.values():
    print(v.title())
