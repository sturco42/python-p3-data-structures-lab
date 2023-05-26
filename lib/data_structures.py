spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    print([i["name"] for i in spicy_foods])
    return [i["name"] for i in spicy_foods]
get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    print([i for i in spicy_foods if i["heat_level"] > 5])
    return [i for i in spicy_foods if i["heat_level"] > 5]
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        x = f"{i['name']} ({i['cuisine']}) | Heat Level: {i['heat_level'] * '🌶'}"
        print(x)
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, x):
    for i in spicy_foods:
        if x == i['cuisine']:
            return i
get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    x = get_spiciest_foods(spicy_foods)
    print_spicy_foods(x)

def get_average_heat_level(spicy_foods):
    print(sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods))
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
# create_spicy_food(spicy_foods)