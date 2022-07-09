menu = [['Egg Sandwich', 'Bagel','Coffee'],
        ['Soup', 'PB&J', 'Turkey Sandwich'],
        ['Salad','Spaghetti','Taco'] ]

print(menu[0][1])

menus = {'Breakfast': ['Egg Sandwich', 'Bagel','Coffee'],
        'Lunch': ['Soup', 'PB&J', 'Turkey Sandwich'],
        'Dinner': ['Salad','Spaghetti','Taco'] }

print(menus['Breakfast'])

for x,y in menus.items():
        print(x, ":", y)

person = {'name':'Shravan',
          'sex': 'M',
           'age':'25'}
print('My name is '+ person.get('name')+' age is '+person.get('age'))
