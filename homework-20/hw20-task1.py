import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_stores(recipe_name, recipes, stores):
    # Find the recipe by name
    recipe = next((r for r in recipes if r['name'] == recipe_name), None)
    if not recipe:
        return f"რეცეპტი {recipe_name} ვერ მოიძებნა."

    required_ingredients = set(recipe['ingredients'])
    store_matches = {store['name']: set(store['products']) & required_ingredients for store in stores}

    # Initialize lists
    min_stores = []
    visited_stores = set()

    while required_ingredients:
        best_store = max(
            (store for store in store_matches if store not in visited_stores),
            key=lambda store: len(store_matches[store]),
            default=None
        )

        if not best_store:
            return "ამ კერძს ამ ქალაქში ვერ მოამზადებთ."

        min_stores.append(best_store)
        visited_stores.add(best_store)
        required_ingredients -= store_matches[best_store]

    return min_stores

def main():
    recipes = load_data('recipes.json')
    stores = load_data('stores.json')

    recipe_name = input("რომელ კერძს მოამზადებთ? ")
    stores_needed = find_stores(recipe_name, recipes, stores)

    if isinstance(stores_needed, list):
        print(f"შეგიძლიათ ეს პროდუქტები შემდეგ მაღაზიებში შეაგროვოთ: {', '.join(stores_needed)}")
    else:
        print(stores_needed)

if __name__ == '__main__':
    main()
