# Laura Bejder Jensen
# October 28th, 2022 / October 29th, 2022
# Homework 1

# Here I am using input to ask the user what year they were born
birthyear = int(input("What is your year of birth?"))

# 1. Creating an output showing how old the user is
year = 2022
age = year - birthyear

print(f'You are {age} years old')

# 2. Calculating how many times the user's heart has beaten in that time
# A normal human heart beats aproximately 80 times per minute. There are 525,600 minutes per year
humanheart = 80 * 525600 * age

print(f"Your heart has beated approximately {humanheart:,} times in the {age} years you have been alive")

# 3. Calculating how many times a bluewhale's heart has beaten in that time
# A normal bluewhale heart beats aproximately 33 times per minute. There are 525,600 minutes per year

bluewhale = 33 * 525600 * age

print(f"A bluewhale's heart has beated approximately {bluewhale:,} times in the {age} years you have been alive")

# 4. Calculating how many times a rabbit's heart has beaten in that time
# A rabbit's heart beats aproximately 160 times per minute.

rabbit = 160 * 525600 * age
print(f"A rabbit's heart has beated approximately {round(rabbit/1000000000, 2)} billion times in the {age} years you have been alive")

# 5. Redoing the rabbit question above but I am using commas instead of f string

print("A rabbit's heart has beated approximately", round(rabbit/1000000000, 2), "billion times in the", age, "years you have been alive")

# I find it easier to use the f-string method because there is less a danger of missing a comma or "" and then messing the whole //
# code up. Especially if you are printing a long sentence. On the other hand, the f-sting method seems very sensitive. I accidently //
# put a space between the f and the "" and it didn't work.

# 6. Figuring out whether the user is older or younger than I am (25 years-old)
if age == 25:
    print("Congratulations! You are the same age as Laura :-)")
elif age < 25:
    print("Too bad, you are younger than Laura...") 
else:
    print("Unfortunately, you are older than Laura...")

#And then we are calculating the age difference
if age < 25:
    print(f"You are {age-25} years younger than Laura!") 
elif age > 25:
    print(f"You are {age-25} years older than Laura!") 

# Now we try to figure out whether the user was born in an even or an odd year
if (birthyear % 2) == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

# 7. How many times there has been a president from the Democratic Party in office since they were born
# Since 1980 the US has had the following presidents: Jimmy Carter (D), 1977-1981, Ronald Reagan (R), 1981-1989, //
# George H. W. Bush (R), 1989-1993, Bill Clinton (D), 1993-2001, George W. Bush (R), 2001-2009, Barack Obama (D), 2009-2017, //
# Donald Trump (R), 2017-2021, Joe Biden (D), 2021-2022

if birthyear >= 2018:
    print("There has been 1 president from the Democratic Party in office since you were born.")
elif birthyear >= 2002:
    print("There has been 2 presidents from the Democratic Party in office since you were born.")
elif birthyear >= 1982:
    print("There has been 3 presidents from the Democratic Party in office since you were born.")
elif birthyear == 1981 or birthyear==1980:
    print("There has been 4 presidents from the Democratic Party in office since you were born.")

# 8. Which US President was in office when they were born (1980 onward)
if birthyear == 1980:
    print(f"Jimmy Carter (D) was president in {birthyear} - the year you were born!")
elif birthyear == 1981:
    print(f"Jimmy Carter (D) and Ronald Reagan (R) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 1981 and birthyear < 1988:
    print(f"Ronald Reagan (R) was president in {birthyear} - the year you were born!")
elif birthyear == 1989:
    print(f"Ronald Reagan (R) and George H. W. Bush (R) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 1989 and birthyear < 1993:
    print(f"George H. W. Bush (R) was president in {birthyear} - the year you were born!")
elif birthyear == 1993:
    print(f"George H. W. Bush (R) and Bill Clinton (D) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 1993 and birthyear < 2001:
    print(f"Bill Clinton (D) was president in {birthyear} - the year you were born!")
elif birthyear == 2001:
    print(f"Bill Clinton (D) and George W. Bush (R) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 2001 and birthyear < 2009:
    print(f"George W. Bush (R) was president in {birthyear} - the year you were born!")
elif birthyear == 2009:
    print(f"George W. Bush (R) and Barack Obama (D) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 2009 and birthyear < 2017:
    print(f"Barack Obama (D) was president in {birthyear} - the year you were born!")
elif birthyear == 2017:
    print(f"Barack Obama (D) and Donald Trump (R) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 2017 and birthyear < 2021:
    print(f"Donald Trump (R) was president in {birthyear} - the year you were born!")
elif birthyear == 2021:
    print(f"Donald Trump (R) and Joe Biden (D) were presidents some time in {birthyear} - the year you were born!")
elif birthyear > 2021:
    print(f"Joe Biden (D) was president in {birthyear} - the year you were born!")
else:
    print("You are too old. No one cares who the president was when you were born!")


# 9. Another approach to #7 and #8 - and which of them is the better. 

    #7 I tried using a dictionary including the democratic presidents' names and the year they left office, and then //
    # created a loop to print out the right message based on a calculation of the birth year and the year they left office. This //
    # definately works better than the method above. Much less writing, much more effective!
democrats = {
    "Jimmy Carter" : 1981,
    "Bill Clinton" : 2001,
    "Barack Obama" : 2017,
    "Joe Biden" : 2022
}
num = 0 
for year in democrats.values():
    if birthyear - year <= 0:
        num = num + 1
print("In your lifetime, there has been", num, "democratic president(s).")

    #8 This one was harder to redo with the same method as above. Overall it works well but I haven't found a way to include both //
    # the retirering president and the president elect in the years where the inauguration takes place. So I lose some of the nuace //
    # in the answer but again this method is much more time effective. I tried making a list within the dictionary and use that as //
    # as a foundation for the calculation but I couldn't make it work.

presidents_1980 = {
    "Jimmy Carter": 1980,
    "Ronald Reagan" : 1988,
    "George H. W. Bush" : 1992,
    "Bill Clinton" : 2000,
    "George W. Bush" : 2008,
    "Barack Obama" : 2016,
    "Donald Trump" : 2020,
    "Joe Biden" : 2022
}

for key, value in presidents_1980.items():
    if birthyear - value <= 0:
        print(f"In {birthyear}, {key} was the president of the United States.")
        break 

# 10. In case someone says they were born in the future, we ask them a second time as it is highly unlikely that their first //
# answer was correct (although it would also be impressive if someone born in 2022 was responding...):

if birthyear > 2022:
    int(input("Are you sure? What year were you born?"))


