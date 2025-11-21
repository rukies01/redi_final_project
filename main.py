
#Project features
# welcome message
#What will you like to wear
#options Coporate, casual, sport, dinner
#favorites, to include clothes marked as favorites and saved in a file
#ask if cloth is accepted or not
#ck laundry
#add clothes to list

import random

Wardrope = {'Corporate': ['Navy blue trouser suit','Black skirt suit', 'Navyblue Skirt suit', 'Navyblue Skirt Suit', 'Cream Skirt Suit', 'Cream Trouser Suit'],
            'Casual':['Blue jeans and White top', 'Blue jean and Cream Top', 'Blue jeans and Black top','Black jeans and yellow top','Black jeans and Brown top'],
             'Sport':['Black sport wear', 'Navy Blue sport wear', 'Track suit'],
             'Native':['Ankara Jumpsuit', 'Ankara Baggy Pant and Top','Brocade Bubu Gown' ],

            }
Laundry = []   # make this a text file.
Favorites = []  # make this a text file.



def add_cloth_to_Favorites():
    with open('Favorites.txt','w') as file:
        for item in Favorites:
            file.write(item + "\n")
        
def choice(answer):  # This function ask user if the random provided outfit should be added to the list of Favorites
    my_choice = input('Would you like me to add this to your Favorites ? (yes/no): ').strip().lower()
    if my_choice == 'yes':
          Favorites.append(answer)  # add 'answer' to favorites list
          add_cloth_to_Favorites()
          print('Item added to your Favorites!') #prints Item has been added to list to inform user
    else:
          print('Item not added to Favorites!')  # print this if my_choice is no


def selection2(select):  #This function returns a random selection according to user input
   if select == 'Corporate':
        answer = random.choice(Wardrope['Corporate'])  #returns a random choice from coporate
        return(answer)
   elif select == 'Casual':
        answer = random.choice(Wardrope['Casual']) # #returns a random choice from casual
        return(answer)
   elif select == 'Sport':
        answer = random.choice(Wardrope['Sport']) # #returns a random choice from sport
        return(answer)
   elif select == 'Native':
        answer = random.choice(Wardrope['Native']) # #returns a random choice from native
        return(answer)
   else:
       try:
            if select not in ['Corporate','Casual','Sport','Native']: # This throws an error if user selection is not in List
                raise ValueError ('This is not a valid Entry')  # prints this to notify user of wrong input
       except ValueError as error:
           print(error)  # prints the error
     


def selection():
    
    for key in Wardrope:
     print (key)
    select = input('What kind of outfit would you like today(Corporate, Casual, Sport, Native)? : ').strip().capitalize()  # print available options
    answer = selection2(select)
    add_cloth_to_laundry(answer)
    print(f'{Laundry}')
    choice(answer)


    
def view_favorites():
     with open("Favorites.txt", "r") as file:
       favorites = file.read()
       print(f'Your Favorites : {favorites}')  # this shows a list of clothes added to favorites


def add_cloth_to_laundry(answer): # this function add the randomly selected outfit to laundry and assumming the user wore that cloth
    Laundry.append(answer)  # this add ans to Laundry
    with open('Laundry.txt','w') as file: #opens the file Laundry.txt if not exixting
        for item in Laundry:
            file.write(item + "\n")  # add item to file Laundry.txt


def view_laundry():
    with open("Laundry.txt", "r") as file: # this opens the file Laundry.txt if not exixting
       laundry = file.read()  # this reads the items in file Laundry.txt
    print(f'Your Laundry:{laundry}') #prints item in file
    
        


def empty_laundry():
    Laundry.clear()  # this empty/clear the laundry list
    with open("Laundry.txt", "w") as file:
        file.write("")  # this ovewrites the Laundry file with noting, automatically deleting file contents
    print('Hurray!!!, Laundry emptied successfully!')


def add_to_wardrope(): # this function alows user to add clothes to the Wardrope
   Add_to_Wardrope1 = input('Please choose a category:(Native, Corporate, Casual, Sport) ').strip().capitalize()
   Add_to_Wardrope2 = input('Please provide the cloth type: ').strip().title()
    
   
   A = Wardrope.get(Add_to_Wardrope1)  # converts the value in selected key into a list
   A.append(Add_to_Wardrope2)  # adds the user input into the list
   Wardrope.update({Add_to_Wardrope1:A})  # converts list back to dictionary and append.
   print(f'{Add_to_Wardrope2} has been added to Wardrope')
   print(f'{A}')




def main():
    while True:
        print('Welcome to your Wardrop')
        print('What will you like to do ?')
        print('1. Select a Cloth')
        print('2. view Favorites')
        print('3. View Laundry') 
        print('4. Empty my Laundry')
        print('5. Add cloth to wardrope')
        print('6.Exit')

        user_choice = input('Please select options(1-6):').strip()
        if user_choice == '1':
            selection()
        elif user_choice == '2':
          view_favorites()
          
        elif user_choice == '3':
            view_laundry()
            
        elif user_choice == '4':
            empty_laundry()
            
        elif user_choice == '5':
            add_to_wardrope()   # ck use case
            
        elif user_choice == '6':
            print("Goodbye!")
            break 
        else:
            print("Invalid choice, please enter a number from 1 to 6.")



main()


             





