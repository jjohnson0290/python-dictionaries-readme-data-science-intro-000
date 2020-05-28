""" 
-Dictionaries are used to set attributes(key) and a values to a variable
-create a dictionary with the braces, also called curly braces
-dictionary is a group of key and value pairs, with the key to the left and the corresponding value to the right
-values of a dictionary can be any data type -- strings, numbers, and others
-Objective:
    -create a dictionary(ies)
    -retrieve a value from dictionary
    -add key/value pairs to dictionary
    -create list in dictionary
        -set attributes to a variable in list 
"""


#creates a dictionary of Friends TV show information
#prints list
friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
#prints a value from attribute
print(friends['no_of_seasons'])

#adds new key and value to dictionary
friends['no_of_episodes'] = 236
print(friends)

#keys can be integers
#creates a integer tpye key and deletes it
friends[14] = "some value"
print(friends)
del friends[14]
print(friends)

#creates a list then inserts a list in dictionary
#creators = ["David Crane", "Martha Kauffman"]
friends['creators'] = ["David Crane", "Martha Kauffman"]
print(friends)
print(friends["creators"])

#selects a value in list at an index and stores as variable
david = friends["creators"][0]

'''-----------------------------------------------------'''

#creates a dictionary using Seifeld TV show information
seinfeld = {"name": "Seinfeld", "creators": ["Larry David", "Jerry Seinfeld"], "genre": "sitcom", "no_of_seasons": 10, "no_of_episodes": 180}

#creates a list of TV shows
tv_shows = [friends, seinfeld]
print(tv_shows)
    #prints a nested data structure
    #In describing the data structure, we look to the braces and brackets at the beginning. 
        #[{ means we are starting a list with a dictionary as the first element.}]

#steps to select second creator of Seinfeld and set equal to variable jerry
#prints TV show one information
print(tv_shows[1])
#selects and prints list of TV show one creators
print(tv_shows[1]["creators"])
#selects and prints TV show 1 creator at given index
print(tv_shows[1]['creators'][1])
#sets jerry equal to TV show one creator 
#selects second creator of Seinfeld and set equal to variable jerry
jerry = tv_shows[1]["creators"][1]
print(jerry) 
"""

'''------------------------------------------'''
""" '''
my dictionary
Objective:
    -[x]create a dictionary(ies)
    -[x]retrieve a value from dictionary
    -[x]add key/value pairs to dictionary
    -[x]create list in dictionary
        -[]set attributes to a variable in list
''' 
#[x]create a dictionary(ies)
msLife = {"name": "J-Mac", "age": "18", "time": "18years"}
caLife = {"name": "BlackmanJohnson", "age": "24","time": "4years"}
#places dictionaries in a list
lifeTime = [msLife, caLife]
msLife = lifeTime[0]
caLife = lifeTime[1]
#print(lifeTime)

#[x]retrieve a value from dictionary
print(msLife["name"])
print(caLife["name"])
print(lifeTime[0]["time"])

#[x]add key/value pairs to dictionary
msLife["friend"] = "Tevin R"
caLife["friend"] = "Guillermo R"
print(lifeTime)
print(msLife)

#[x]create list in dictionary and insert into dictionary
msLife["creators"] =  ["Justin Johnson", "MomandDad"]
caLife["creators"] =  ["Justin Johnson", "Marine Corps"]
print(msLife)
print(caLife)

#[x]set value in list and sets equal to a variable
print(lifeTime[1]["creators"][1])
marines = (lifeTime[1]["creators"][1])
print(marines)
