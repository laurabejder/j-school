# Laura Bejder Jensen
# October 31, 2022
# Homework 2, Part 2

# PART ONE: Lists

# 1. I create a list of seven countries - in this case the G7 countries
countries = ["United States", "France", "Germany", "Japan", "Canada", "Italy", "United Kingdom"]

# 2. Then I use a loop to print each element of the list
for country in countries:
    print(country)

# 3. Then I sort the list permanently

countries.sort()

# 4. And display the first element of the sorted list

print(f"The first country in the list is {countries[0]}.")

# 5. Then I display the second-to-last element
print(f"The second-to-last country in the list is the {countries[-2]}.")

# 6. To remove a country from the list, I use .remove(). I decide to remove the US.
countries.remove("United States")

# 7. To print each country's name in all caps, I use the .upper() function
for country in countries:
    print(country.upper())

# PART TWO: Dictionaries

# 1. Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'.

tree = {
    "name" : "the King Oak",
    "species" : "European Oak",
    "age" : 1500,
    "location_name" : "Jægerspris, Denmark",
    "latitude" : 55.910278,
    "longitude" : 11.989167
}

# 2. Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print(f"The {tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}")

# 3. The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
nyc_latitude = 40.7128

if tree['latitude'] < nyc_latitude:
    print(f"The tree, {tree['name']}, in {tree['location_name']} is south of NYC")
else:
    print(f"The tree, {tree['name']}, in {tree['location_name']} is north of NYC")

# 4. Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

user_age = int(input("How old are you?"))

if user_age > tree['age']:
    print(f"You are {user_age-tree['age']} years older than {tree['name']}")
elif user_age < tree['age']:
    print(f"You are {tree['age']-user_age} years younger than {tree['name']}")
else:
    print(f"You are the same age as {tree['name']}")

# PART TWO: Lists of dictionaries

# 1. Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

cities = [
    {"name": "Moscow", "latitude": 55.758664, "longitude": 37.619292}, 
    {"name": "Tehran", "latitude": 35.668208, "longitude": 51.374414}, 
    {"name": "Falkland Islands", "latitude": -51.796719, "longitude": -58.594932}, 
    {"name": "Seoul", "latitude": 37.566983, "longitude":126.978235},
    {"name": "Santiago", "latitude": -33.451856, "longitude": -70.650466}
]

# 2. Then I create a loop that goes throug each element of the list and prints the name and whether it is below or above equator.

for city in cities:
    print(city["name"])
    if city["latitude"] > 0:
        print("The city is above equator")
    elif city["latitude"] < 0:
        print("The city is below equator")
        if city["name"] == "Falkland Islands":
            print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
        else:
            print()
    else:
        print("The city is on equator")
    
# 3. Then I create a loop to see if each city is north or south of the Oak tree

for city in cities:
    if city["latitude"] > tree["latitude"]:
        print(f"{city['name']} is north of {tree['name']}")
    elif city["latitude"] < tree["latitude"]:
        print(f"{city['name']} is south of {tree['name']}")
    else:
        print(f"{city['name']} is on the same latitude as {tree['name']}")