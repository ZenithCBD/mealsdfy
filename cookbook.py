Breakfasts = {
    'Pancakes': {
        'Name': 'Pancakes',
        'Ingredients': '1 cup of pancake mix and 1/4 cup of milk',
        'Instructions': 'mix ingredients, then cook your shit on the stove',
    }
}

Postnoons = {
    'Pizza': {
        'Ingredients': 'must hab frozen pizza.',
        'Instructions': 'preheat oven, put pizza in, wait a lil bit, take it out.',
    }
}

def get_meal(x):
    if x == 'Breakfasts':
        print(Breakfasts[str(x)]['Name'])
        print(Breakfasts[str(x)]['Ingredients'])
        print(Breakfasts[str(x)]['Instructions'])
    elif x == 'Postnoons':
        print(Breakfasts[str(x)]['Name'])
        print(Breakfasts[str(x)]['Ingredients'])
        print(Breakfasts[str(x)]['Instructions'])