# Laura Bejder Jensen
# October 31, 2022
# Homework 2

# PART ONE: Lists

#  1. Make a list of the following numbers: 22, 90, 0, -10, 3, 22 and 48

list = [22, 90, 0, -10, 3, 22, 48]

print(f"This list contains the following numbers {list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}, {list[5]}, and {list[-1]}")

# 2. Display the number of elements in the list.

number_of_elements = len(list)
print(f"The number of elements in the list is {number_of_elements}")

# 3. Display the 4th element of this list.
print(f"The 4th element of the list is {list[3]}")

# 4. Display the sum of the 2nd and 4th element of the list.

print(f"The sum of the 2nd and 4th elements of the list is {list[1]+list[3]}")

# 5. Display the 2nd-largest value in the list.

sorted_list = sorted(list)

print (f"The 2nd largest value in the list is {sorted_list[-2]}")

# 6. Display the last element of the original unsorted list

print(f"The last element of the list is {list[-1]}")

# 7. Display the sum of all of the numbers divided by two.

print(f"The sum of all the elements divided by two is {sum(list)/2}")

# 8. Print whether the median or the mean of the numbers is higher

# First I calculate the mean and defines it as a variable
mean = sum(list)/len(list)
print(f"The mean is {mean}")

# With the median, I just find the middle element in the list - here 4 - because there //
# are 7 elements in the list. 
median = sorted_list[3]
print(f"The median is {median}")
    # I am not sure this is the best way to do it. I am wondering how we can calculate//
    # the median without knowing the number of elements in the list ... 

# Then I make python print wether the median or the mean of the list is higher

if mean > median:
    print("The mean of the list is higher than the median")
elif median > mean:
    print("The median of the list is higher than the mean")
else:
    print("The mean and the median of the list are the same")


# PART ONE: Dictionary

# 1. I am creating a dictionary with information about my favorite movie

movie = {
    "title": "Before Sunrise",
    "year": 1995,
    "director": "Richard Linklater"
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# 2. Then I add information about the budget and the revenue to the list

movie["budget"]= 2500000
movie["revenue"]= 22500000

print(f"My favorite movie is {movie['title']} which was released in {movie['year']} and was directed by {movie['director']}. The difference between the budget and the revenue is {(movie['revenue']-movie['budget'])/1000000} million.")

# 3. If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." //
# Otherwise print "That was an okay investment."

if movie["budget"] > movie["revenue"]:
    print("That was a bad investment")
elif movie["revenue"]/5 > movie["budget"]:
    print("That was a great investment.")
else: 
    print("That was an okay investment.")

# 4. One dictionary describing the population of the boroughs of NYC.

nyc_boroughs = {
    "Manhattan": 1600000,
    "Brooklyn": 2600000,
    "Bronx": 1400000,
    "Queens": 2300000,
    "Staten Island": 470000
}

# 5. Display the population of Brooklyn.
print("The population of Brooklyn is", nyc_boroughs["Brooklyn"]/1000000,"millions")

# 6. Display the combined population of all five boroughs
print("The combined population of all five boroughs is", sum(nyc_boroughs.values())/1000000,"millions")

# 7. Display what percent of NYC's population lives in Manhattan.
print(round(nyc_boroughs["Manhattan"]/sum(nyc_boroughs.values())*100,2),"percent of NYC's population lives in Manhattan.")
