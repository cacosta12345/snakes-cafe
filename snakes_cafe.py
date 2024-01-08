def print_menu():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

menu_items = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]

def take_order():
    
    menu_items_lower = [item.lower() for item in menu_items]
    order_count = {}

    while True:
        order = input("> ").strip().lower()
        if order == 'quit':
            break

        if order in menu_items_lower:
            original_item = menu_items[menu_items_lower.index(order)]
            order_count[original_item] = order_count.get(original_item, 0) + 1
            print(f"\n** {order_count[original_item]} order of {original_item} has been added to your meal **\n")
        else:
            print("\n** Item not on menu **\n")

if __name__ == "__main__":
    print_menu()
    take_order()
