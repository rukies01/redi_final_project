# Wardrobe Organizer – Python Project

A simple, wardrobe management app with menu which helps users to pick outfits, organize clothing into categories, save clothes to favorites, and manage laundry.  
This project was built to practice Python fundamentals, problem-solving, and file handling while creating something fun and useful.

---

## Features

###  1. Random Outfit Selection
- Choose a clothing category from (Corporate, Casual, Sport, or Native)
- The app returns a random outfit from the category chosen
- Selected items are saved to Laundry.

### 2. Laundry System
- Selected outfits are automatically saved to the Laundry list
- Laundry can be viewed or emptied
- When emptied, all outfits in Laundry are deleted

###  3. Favorites (Saved to File)
- Users can save selected outfits as Favorites
- Favorites are stored in `favorites.txt`
- File helps item to remain saved even after the program closes

### 4. Add New Clothes to the Wardrobe
- Users can add new items or new categories to the wardrobe

### 5. Clean Menu Interface
- Easy-to-use looped menu
- Handles invalid input
- Uses `.strip()` and `.lower()` for clean formatting

### 6. Exit option and error handling
- To exit the programme
- To raise an error when the user input an unknown input.

---

## Technologies Used
- Python environment
- Random module
- File handling (`open()`, read/write)
- Lists & dictionaries
- Loops, conditionals, Switch case, functions
  

---

##  File Structure
WardrobeOrganizer/
│
├── main.py
├── favorites.txt
├── laundry.txt 
└── README.md

## How It Works

1. Run the program  
2. Choose an option from the menu (1-6) 
3. The program responds instantly:
   - selecting a random clothe from the category choosen  
   - ask user if they want to save favorites  
   - adding items to Laundry 
       
The program continue to  run until the user selects the Exit option.

This is a link to the Wardrobe organizer diagram
![Diagram of code](https://github.com/rukies01/redi_final_project/blob/main/Redi%20project%20Diagramm.1.png)


# PURPOSE & IMPACT SECTION 

This Wardrobe Organizer was created to solve a common everyday problem of:
**“What should I wear today?”**

This project:
- reduces decision fatigue that comes with deciding which outfit to select 
- encourages a better outfit rotation  
- saves users' favorites  
- mimics a real life laundry behaviour  
 

From a learning perspective, the project strengthens:
- file handling 
- menu-driven programs  
- data manipulation using lists and dictionaries  
- randomization logic  
- input validation  
- clean program structure  

## Setup & Usage

1. Clone the repo  
   ```bash
   git clone https://github.com/rukies01/WardrobeOrganizer.git
2. Run the script
   python main.py

## Future Improvements

Add a weather API to suggest weather appropriate clothes
Export wardrobe to CSV or JSON
Add timestamps to track last worn dates
Add a GUI 


Author:
Rukayyat Adelekan
Python Developer/Data Analyst
LinkedIn: www.linkedin.com/in/adelekanrukayyat


