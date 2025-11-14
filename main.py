
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
Laundry = []
Favorites = []

def main():
    while True:
        print('Welcome to your Wardrop')
        print('What will you like to do ?')
        print('1. Select a Cloth')
        print('2. Add cloth to favorites')
        print('3. View Favorites') 
        print('4. Empty my Laundry')
        print('5. Add cloth to wardrope')
        print('6.Exit')

        user_choice = input()
        if user_choice == '1':
            item = selection()
            if item:
        
def choice(answer):
    my_choice = input('Would you like me to add this to your Favorites ? (yes/no): ')
    if my_choice == 'yes':
          Favorites.append(answer)  # add 'answer' to favorites list
          print('Item added to your Favorites!')
    else:
          print('Item not added to Favorites!')  # print this if my_choice is no


def selection2(select):
   if select == 'Coporate':
        answer = random.choice(Wardrope['Coporate'])  #returns a random choice from coporate
        print(answer)
   elif select == 'Casual':
        answer = random.choice(Wardrope['Casual']) # #returns a random choice from casual
        print(answer)
   elif select == 'Sport':
        answer = random.choice(Wardrope['Sport']) # #returns a random choice from sport
        print(answer)
   elif select == 'Native':
        answer = random.choice(Wardrope['Native']) # #returns a random choice from native
        print(answer)
   else:
       try:
            if select not in ['Coporate','Casual','Sport','Native']:
                raise ValueError ('That is not a valid Entry')
       except ValueError as error:
           print(error)


def selection():
    
    for key in Wardrope:
     print (key)
    select = input('What kind of outfit would you like today : ')  # print available options
    answer = selection2(select)
    choice(answer)


    
def view_favorites():
     print(f'Your Favorites : {Favorites}')  # this shows a list of clothes added to favorites


def add_cloth_to_laundry(answer):
    while True:
        Laundry.append(answer)
    else:
        break
        


def empty_laundry():
    Laundry.clear()  # this empty/clear the laundry list





selection()

                   