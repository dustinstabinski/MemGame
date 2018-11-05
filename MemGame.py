import random
import os
import time
import subprocess as sp

FOOD_NAMES_STR = '''
American Chinese cuisine
Biscuit (and Biscuits and gravy)
Bread
Ammonia cookie
Cuisine of Antebellum America
Apple butter
Apple sauce
Baked potato
Barbecue (see below for specific types)
Bear claw
Beef Manhattan
Blue cheese dressing
Blue-plate special
Bookbinder soup
Breakfast burrito
Brunswick stew
Buffalo burger
Buffalo wing
Bull roast
Burnt ends
Butter cookie
Cajun cuisine
Calf's liver and bacon
Carne pizzaiola[citation needed]
Carolina style
Celery Victor
Cheese dog
Cheese fries
Cheese steak
Chicago-style_pizza
Chicken à la King
Chicken and waffles
Chicken Divan
Chicken fingers
Chicken French
Chicken fried bacon
Chicken fried steak
Chicken nugget
Chicken parmigiana
Chicken sandwich
Chili con carne
Chili dog
Chimichanga
Chips and dip
Dark chocolate
Milk chocolate
White chocolate
Chocolate chip cookies
Choco pie
Chowder
City chicken
Clam cake
Clam chowder
Coleslaw
Cordon bleu
Corn chowder
Corn dog
Corn flakes
Corn relish
Corned beef
Cornish game hen
Cowboy beans
Crab cake
Creamed corn
Creamed eggs on toast
Deviled crab
Deviled egg
Domesticated turkey
Doughnut
Drunken chicken
Eggo
Eggs Benedict
Eggs Neptune
Energy bar
Engastration (e.g., Turducken)
Fajita
Fortune cookie
French dip
Fried chicken
Fried fish
Fry sauce
Frybread
Garden salad
German chocolate cake
Goulash
Greek-American cuisine
Green bean casserole
Grits
Hamburger
Hangtown fry
Haystack
Hog fry
Home fries
Hot chicken
Hot chicken sandwich
Ice cream cake
Italian-American cuisine
Italian beef
Italian dressing
Jell-O
Jerky
Juba
Liver and onions
Lobster Newberg
Lobster roll
London broil
Lorna Doone
Macaroni and cheese
Macaroni salad
Maple bacon donut
Maraca pie
Mashed potato
Mashed pumpkin
Meatcake
Meatloaf
Milk toast
Milkshake
Mission burrito
Mozzarella sticks
Muffuletta
Mulligan stew
Onion ring
Oreo
Oysters Rockefeller
Pancakes
Pasta salad
Pastrami
Patty
Peanut butter
Pemmican
Pepperoni
Philadelphia Cheese steak
Pickled cucumber
Pigs in blankets
Pizza strips
Ploye
Pop-Tarts
Popcorn
Popover
Poppyseed muffin
Pork and beans
Potato salad
Potato skins
Potato wedges
Potatoes O'Brien
Protein bar
Pulled pork
Pumpkin pie
Rabbit pie
Ranch dressing
Reuben sandwich
Ribs
Rolled oyster
Russian dressing
Russian tea cake
Salisbury steak
Sandwich
Sausage gravy
Scampi
Scrapple
Seafood cocktail
Senate bean soup
Slinger
Sloppy joe
Smelt
Sonofabitch stew
Soul food
Sour cream
Squab
Steak
Steak sandwich
Steak sauce
Steamed clams
Stuffed ham
Stuffed peppers
Stuffed zucchini
Succotash
Surf and turf
Swiss steak
Tetrazzini
Cuisine of the Thirteen Colonies
Thousand Island dressing
Toaster Strudel
Tomato compote
Tuna casserole
Turducken
Thanksgiving turkey
Vichyssoise
Waffle
'''
FOOD_NAMES = FOOD_NAMES_STR.split()

HUMAN_NAMES_STR = '''
1	Sophia	Jackson
2	Emma	Aiden
3	Olivia	Lucas
4	Ava	Liam
5	Mia	Noah
6	Isabella	Ethan
7	Riley	Mason
8	Aria	Caden
9	Zoe	Oliver
10	Charlotte	Elijah
11	Lily	Grayson
12	Layla	Jacob
13	Amelia	Michael
14	Emily	Benjamin
15	Madelyn	Carter
16	Aubrey	James
17	Adalyn	Jayden
18	Madison	Logan
19	Chloe	Alexander
20	Harper	Caleb
21	Abigail	Ryan
22	Aaliyah	Luke
23	Avery	Daniel
24	Evelyn	Jack
25	Kaylee	William
26	Ella	Owen
27	Ellie	Gabriel
28	Scarlett	Matthew
29	Arianna	Connor
30	Hailey	Jayce
31	Nora	Isaac
32	Addison	Sebastian
33	Brooklyn	Henry
34	Hannah	Muhammad
35	Mila	Cameron
36	Leah	Wyatt
37	Elizabeth	Dylan
38	Sarah	Nathan
39	Eliana	Nicholas
40	Mackenzie	Julian
41	Peyton	Eli
42	Maria	Levi
43	Grace	Isaiah
44	Adeline	Landon
45	Elena	David
46	Anna	Christian
47	Victoria	Andrew
48	Camilla	Brayden
49	Lillian	John
50	Natalie	Lincoln
51	Isabelle	Samuel
52	Skyler	Joseph
53	Maya	Hunter
54	Lucy	Joshua
55	Lila	Mateo
56	Audrey	Dominic
57	Makayla	Adam
58	Penelope	Leo
59	Claire	Ian
60	Kennedy	Josiah
61	Paisley	Anthony
62	Savannah	Colton
63	Alaina	Max
64	Gabriella	Thomas
65	Violet	Evan
66	Kylie	Nolan
67	Charlie	Aaron
68	Stella	Carson
69	Allison	Christopher
70	Liliana	Hudson
71	Eva	Cooper
72	Callie	Adrian
73	Kinsley	Jonathan
74	Reagan	Jason
75	Sophie	Charlie
76	Alyssa	Miles
77	Alice	Jeremiah
78	Caroline	Gavin
79	Aurora	Asher
80	Eleanor	Austin
81	Juliana	Ezra
82	Annabelle	Chase
83	Emilia	Alex
84	Sadie	Xavier
85	Bella	Jordan
86	Julia	Tristan
87	Keira	Easton
88	Bailey	Zachary
89	Hazel	Parker
90	Jocelyn	Bryson
91	London	Tyler
92	Samantha	Camden
93	Vivian	Damian
94	Gianna	Declan
95	Alexandra	Elliot
96	Cora	Elias
97	Melanie	Cole
98	Everly	Harrison
99	Jordyn	Zane
100	Luna	Kai
'''
counter_name = 1
HUMAN_NAMES = HUMAN_NAMES_STR.split()
for name in HUMAN_NAMES:
    if name == str(counter_name):
        HUMAN_NAMES.remove(name)
        counter_name = counter_name + 1

ANIMAL_NAMES = [
    "Aardvark",
    "Albatross",
    "Alligator",
    "Alpaca",
    "Ant",
    "Anteater",
    "Antelope",
    "Ape",
    "Armadillo",
    "Donkey",
    "Baboon",
    "Badger",
    "Barracuda",
    "Bat",
    "Bear",
    "Beaver",
    "Bee",
    "Bison",
    "Boar",
    "Buffalo",
    "Butterfly",
    "Camel",
    "Capybara",
    "Caribou",
    "Cassowary",
    "Cat",
    "Caterpillar",
    "Cattle",
    "Chamois",
    "Cheetah",
    "Chicken",
    "Chimpanzee",
    "Chinchilla",
    "Chough",
    "Clam",
    "Cobra",
    "Cockroach",
    "Cod",
    "Cormorant",
    "Coyote",
    "Crab",
    "Crane",
    "Crocodile",
    "Crow",
    "Curlew",
    "Deer",
    "Dinosaur",
    "Dog",
    "Dogfish",
    "Dolphin",
    "Dotterel",
    "Dove",
    "Dragonfly",
    "Duck",
    "Dugong",
    "Dunlin",
    "Eagle",
    "Echidna",
    "Eel",
    "Eland",
    "Elephant",
    "Elk",
    "Emu",
    "Falcon",
    "Ferret",
    "Finch",
    "Fish",
    "Flamingo",
    "Fly",
    "Fox",
    "Frog",
    "Gaur",
    "Gazelle",
    "Gerbil",
    "Giraffe",
    "Gnat",
    "Gnu",
    "Goat",
    "Goldfinch",
    "Goldfish",
    "Goose",
    "Gorilla",
    "Goshawk",
    "Grasshopper",
    "Grouse",
    "Guanaco",
    "Gull",
    "Hamster",
    "Hare",
    "Hawk",
    "Hedgehog",
    "Heron",
    "Herring",
    "Hippopotamus",
    "Hornet",
    "Horse",
    "Human",
    "Hummingbird",
    "Hyena",
    "Ibex",
    "Ibis",
    "Jackal",
    "Jaguar",
    "Jay",
    "Jellyfish",
    "Kangaroo",
    "Kingfisher",
    "Koala",
    "Kookabura",
    "Kouprey",
    "Kudu",
    "Lapwing",
    "Lark",
    "Lemur",
    "Leopard",
    "Lion",
    "Llama",
    "Lobster",
    "Locust",
    "Loris",
    "Louse",
    "Lyrebird",
    "Magpie",
    "Mallard",
    "Manatee",
    "Mandrill",
    "Mantis",
    "Marten",
    "Meerkat",
    "Mink",
    "Mole",
    "Mongoose",
    "Monkey",
    "Moose",
    "Mosquito",
    "Mouse",
    "Mule",
    "Narwhal",
    "Newt",
    "Nightingale",
    "Octopus",
    "Okapi",
    "Opossum",
    "Oryx",
    "Ostrich",
    "Otter",
    "Owl",
    "Oyster",
    "Panther",
    "Parrot",
    "Partridge",
    "Peafowl",
    "Pelican",
    "Penguin",
    "Pheasant",
    "Pig",
    "Pigeon",
    "Pony",
    "Porcupine",
    "Porpoise",
    "Quail",
    "Quelea",
    "Quetzal",
    "Rabbit",
    "Raccoon",
    "Rail",
    "Ram",
    "Rat",
    "Raven",
    "Red deer",
    "Red panda",
    "Reindeer",
    "Rhinoceros",
    "Rook",
    "Salamander",
    "Salmon",
    "Sand Dollar",
    "Sandpiper",
    "Sardine",
    "Scorpion",
    "Seahorse",
    "Seal",
    "Shark",
    "Sheep",
    "Shrew",
    "Skunk",
    "Snail",
    "Snake",
    "Sparrow",
    "Spider",
    "Spoonbill",
    "Squid",
    "Squirrel",
    "Starling",
    "Stingray",
    "Stinkbug",
    "Stork",
    "Swallow",
    "Swan",
    "Tapir",
    "Tarsier",
    "Termite",
    "Tiger",
    "Toad",
    "Trout",
    "Turkey",
    "Turtle",
    "Viper",
    "Vulture",
    "Wallaby",
    "Walrus",
    "Wasp",
    "Weasel",
    "Whale",
    "Wildcat",
    "Wolf",
    "Wolverine",
    "Wombat",
    "Woodcock",
    "Woodpecker",
    "Worm",
    "Wren",
    "Yak",
    "Zebra"
]

def close_enough(word_list, response):
    for word in word_list:
        counter = 0
        similar = 0
        if len(word) < len(response):
            index = 0
            for letter in word:
                if letter.lower() in response:
                    similar += 1
                counter += 1
                index += 1
            if similar / len(response) >= .70:
                return [True, word]
        elif len(word) > len(response):
            index = 0
            for letter in response:
                if letter.lower() in word:
                    similar += 1
                counter += 1
                index += 1
            if similar / len(word) >= .70:
                return [True, word]
        else:
            index = 0
            for letter in response:
                if letter.lower() in word:
                    similar += 1
                counter += 1
                index += 1
            if similar / len(word) >= .70:
                return [True, word]
    return [False]

def display_menu():
    print("Welcome to MemGame.\nSelect category by typing in one of the numbers:\n  1)Animals\n  2)Names\n  3)Food\n Enter quit to exit program")

def get_obj_list(level, list):
    counter = 0
    disp_list = []
    while(counter < level):
        disp_list += [list[random.randrange(0,len(list))]]
        counter = counter + 1
    return disp_list
def play_round(level, list):
    round_list = get_obj_list(level, list)
    if len(round_list) == 2:
        print('''
    Welcome to MemGame!
    I will present you with a list of words.
    After the list disappears, type in ONE element from the list.
    If you are correct, then I will respond with another element from the list.
    Then, you must name another element of the original list.
    Do NOT repeat me or yourself. Can you beat me?
    ''')
    print('''
    Study the list and press <enter> when you are ready
    ''')
    print(round_list)
    input()
    print('\033c', end=None)
    num = 0
    counter = 0
    round_length = len(round_list)
    for animal in round_list:
        round_list[num] = round_list[num].lower()
        num = num + 1
    while counter <= round_length:
        answer = input("Enter guess: ")
        if len(round_list) > 1 and close_enough(round_list, answer)[0]:
            answer = close_enough(round_list, answer)[1]
            round_list.remove(answer.lower())
            response = round_list[random.randrange(0,len(round_list))]
            print(response.title())
            round_list.remove(response)
            if len(round_list) == 0:
                print("Level " + str(level) + " complete!")
                num = 0
                counter = 0
                to_next_level(level, list)
            counter = counter + 1
        elif answer.lower() not in round_list:
            print("Incorrect. I win!! Game Over. Returning to home screen...")
            time.sleep(3)
            os.system("clear")
            beginning()
        else:
            print("Level " + str(level) + " complete!")
            num = 0
            counter = 0
            to_next_level(level, list)
def to_next_level(level, list):
    play_round(level + 1, list)

def beginning():
    person_response = " "
    while(person_response != "quit"):
        display_menu()
        person_response = input()
        if person_response == '1':
            print('\033c', end=None)
            play_round(2, ANIMAL_NAMES)
        elif person_response == '2':
            print('\033c', end=None)
            play_round(2, HUMAN_NAMES)
        elif person_response == '3':
            print('\033c', end=None)
            play_round(2, FOOD_NAMES)
        elif person_response == "quit":
            print('\033c', end=None)
            os._exit(0)
#_________________________________________________________________________________________________________________________________________________________

#TEST
#
#_________________________________________________________________________________________________________________________________________________________
# TO BEGIN GAME
beginning()
