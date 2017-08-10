#sandwich = {'wheat bread', 'miracle whip', ' american chesse', 'turkey meat'}

def create_sandwich (**ingridiets):
    sandwich = {}
    for key, value in ingridiets.items():
        sandwich[key] = value
    return sandwich

fav_sandwich = create_sandwich(bread='wheat bread', sauce='miracle whip',
                               cheese= ' american cheese',
                               meat ="turkey")

print(fav_sandwich)