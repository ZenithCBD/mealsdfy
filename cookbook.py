import random

# need a variable for each ingredient

# I personally purchase eggs in the 18 count.
# In the future, there will be a function calculating if I actually need to purchase eggs, etc.
# HOWEVER, for now I can figure out what percentage of a thing of eggs or milk I need in a recipe
# and then represent that as a decimal. Then I can really see just how much milk or eggs etc I'll need.
# I just now realize that means we need a config file defining the sizes of the items you buy.

# another thing that would be nice is planning portion sizes.

# for now let's just worry about v1.0
breakfasts = {
    "Pancakes": ["eggs,", "pancake mix", "1/4 cup milk"],
    "Scrambled Eggs": ["eggs "],
    "Avacado Toast": ["bread ", "avocados ",],
    "Yogurt Parfait": ["yogurt ", "granola ", "berries ",],
}

dinners = {
    "Pizza": "frozen pizza"
}

lunches = {
    "Frozen Macaroni Bowl": "frozen macaroni meal"

}

snacks = {

}

desserts = {

}

def get_breakfasts(amount):
    breakfast_items = list(breakfasts.keys())
    random.shuffle(breakfast_items)
    for i in range(amount):
        print(breakfast_items[i % len(breakfast_items)])

def get_dinners(amount):
    dinners_items = list(dinners.items())
    for i in range(amount):
        meal, ingredients = dinners_items[i]
        print(f"{i}: {meal}")

def get_lunches(amount):
    lunches_items = list(lunches.items())
    for i in range(amount):
        meal, ingredients = lunches_items[i]
        print(f"{i}: {meal}")
    
def get_snacks(amount):
    snacks_items = list(snacks.items())
    for i in range(amount):
        meal, ingredients = snacks_items[i]
        print(f"{i}: {meal}")
    
def get_desserts(amount):
    desserts_items = list(desserts.items())
    for i in range(amount):
        meal, ingredients = desserts_items[i]
        print(f"{i}: {meal}")