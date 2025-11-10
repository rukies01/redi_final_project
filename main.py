
#Project features
# welcome message
#What will you like to wear
#options Coporate, casual, sport, dinner
#favorites, to include clothes mark as favorites
#ask if cloth is accepted or not
#ck laundry
#add clothes to list

import random

Wardrope = {'Coporate': ['Navy blue trouser suit','Black skirt suit', 'Navyblue Skirt suit', 'Navyblue Skirt Suit', 'Cream Skirt Suit', 'Cream Trouser Suit'],
            'Casual':['Blue jeans and White top', 'Blue jean and Cream Top', 'Blue jeans and Black top','Black jeans and yellow top','Black jeans and Brown top'],
             'Sport':['Black sport wear', 'Navy Blue sport wear', 'Track suit'],
             'Native':['Ankara Jumpsuit', 'Ankara Baggy Pant and Top','Brocade Bubu Gown' ],

            }

def selection():
    print('Welcome to your Wardrope')
    print('Available selections are :')
    for key in Wardrope:
     print (key)
    select = input('What kind of outfit would you like today : ')

def selection2(select):
   if select == 'Coporate':
        print(random.choice(Wardrope['Coporate']))
   elif select == 'Casual':
        print(random.choice(Wardrope['Casual']))
   elif select == 'Sport':
        print(random.choice(Wardrope['Sport']))
   elif select == 'Native':
        print(random.choice(Wardrope['Native']))
   else:
       try:
            if select not in ['Coporate','Casual','Sport','Native']:
                raise ValueError ('That is not a valid Entry')
       except ValueError as error:
           print(error)


selection()
selection2('Coporate')
                   