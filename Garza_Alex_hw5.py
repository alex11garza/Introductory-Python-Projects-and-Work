recipe_book = {
    "Chicken Soup": ["chicken", "chicken broth", "carrots", "celery", "noodles"],
    "Lasagna": ["lasagna noodles", "pasta sauce", "ricotta"],
    "Grilled Cheese": ["bread", "butter", "cheese"],
    "Garden Salad": ["lettuce", "tomatoes", "carrots", "olives"],
    "Alex's Special": ["chicken", "rice", "broccoli", "soy sauce"]
}
print("Which recipe would you like to make?")
for recipe in recipe_book:
    print("- " + recipe)
selected_recipe1 = input("Enter the name of the recipe: ")
print("\nIngredients for " + selected_recipe1 + ":")
for ingredient in recipe_book[selected_recipe1]:
    print("- " + ingredient)
print("\nWhich recipe would you like to make next?")
for recipe in recipe_book:
    if recipe != selected_recipe1:
        print("- " + recipe)
selected_recipe2 = input("Enter the name of the recipe: ")
print("\nIngredients for " + selected_recipe2 + ":")
for ingredient in recipe_book[selected_recipe2]:
    print("- " + ingredient)
grocery_list = recipe_book[selected_recipe1] + recipe_book[selected_recipe2]
print("\nGrocery List:")
for item in grocery_list:
    print("- " + item)
while True:
    additional_item = input("\nWould you like to add additional items to add to your grocery list (or 'Done' to finish): ")
    if additional_item.lower() == "done":
        break
    else:
        grocery_list.append(additional_item)
print("\nFinal Grocery List:")
for item in grocery_list:
    print("- " + item)
