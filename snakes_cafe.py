from pprint import pprint

# menu_types = {
#     'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
#     'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
#     'Desserts': ['Ice Cream', 'Cake', 'Pie'],
#     'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
# }

menu_types = ["Wings", "Cookies", "Spring Rolls","Salmon", "Steak","Meat Toranado", "A Litte Garden", "Ice Cream","Cake" , "Pie", "Coffee", "Tea", "Unicorn Tears" ]

welcoming_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
print(welcoming_message)

menu = """
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

"""
# pprint(menu_types)
print(menu)
def user_input():

    count = {item: 0 for item in menu_types}
    while 1:
        order = input('What would you like to order? \n >')
        if order == 'quit':
            print('Goodbye')
            break
        # elif order in menu_types:
        elif order in menu_types:
            count[order] += 1
            print(f'** {count[order]} order of {order} have been added to your meal **')


user_input()