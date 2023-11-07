#PYTHON 2
name = "ada lovelace"
print(name.title())
first_name = "ada"
last_name = "lovelace"
full_name = first_name +" " +last_name
print(full_name)
print("Hello, " + full_name.title() +"!")
message = "Hello, " +full_name.title() + "!"
print(message)
print("Languages:\n\tPython\n\tc\n\tJavaScript")
print("Languages:\nPython\nC\nJavaScript")
print(5 + 3)
print(16 - 8)
print(4 * 2)
print (16/2)

favorite_number = "7"
print(favorite_number)
# empty quatation marks creates space between words and variables.
message = "I blinked" + " " + favorite_number + " "+ "times" + "!"
print(message)
#(PYTHON 3)
my_list = [1,2,99999999,4,5]
print(len(my_list))
my_list.insert(1,"tangerines")
print(my_list)
my_list.remove(2)
print(my_list)

#Learning to play with Lists!
friends = ["lisa", "tracey","cameryn","jade","erica"]
print(friends)
print(friends[0].title())
print(friends[1])
print(friends[2].title())
print(friends[3])
print(friends[4].title())
message = "My best friend is" +" "+ friends[1].title()+" " + "she is cool" + "."
print(message)
message = friends[0].title() +" "+ "is very mean" + "."
print(message)
message = "I like going to" +" "+ friends[2].title()+" "+ "when I need help"+"."
print(message)
message = friends[4].title() +" "+ "is my newest friend," +" "+ "I just met her a month ago" +"."
print(message)
message = friends[0].title() +" "+ "and" +" "+ friends[4].title() +" "+ "known each other the longest" + "."
print(message) 

#changing items in a list 
motorcycles= ["hond", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] ="ducati"
print(motorcycles)
#just re-write the item by picking the specific associated like above
motorcycles= ["hond", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)
#using ".append" will add new list items to the end of a list
# use ".insert()" to add an list item in a specific place
motorcycles= ["hond", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)
#use del statement to remove items in a list (CANT BE USED AGAIN)
motorcycles= ["hond", "yamaha", "suzuki"]
del motorcycles[0]
print(motorcycles)
motorcycles= ["hond", "yamaha", "suzuki"]
del motorcycles[1]
print(motorcycles)
# ".pop()" is use to remove items that CAN be used again
motorcycles= ["hond", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#We start by defining and printing the list motorcycles at u. At v we pop
#a value from the list and store that value in the variable popped_motorcycle.
#We print the list at w to show that a value has been removed from the list.
#Then we print the popped value at x to prove that we still have access to
#the value that was removed.
#The output shows that the value 'suzuki' was removed from the end of
#the list and is now stored in the variable popped_motorcycle:
motorcycles = ["hond", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a" + " " + last_owned.title() + ".")
second_owned = motorcycles.pop()
print("The second motorcycle I owned was a" + " "+ second_owned.title()+ ".")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive  = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA" +" "+ too_expensive +" " +"is too expensive for me" + ".")

guest_list = ["corey", "ciera", "marie"]
print(guest_list)
print(guest_list [0].title())
print(guest_list [1].title())
print(guest_list [2].title())
message = "I'd like to invite" +" "+ guest_list[0].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite" +" "+ guest_list[1].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite" +" "+ guest_list[2].title() +" "+ "to dinner next week" +"."
print(message)

guest_list = ["corey", "ciera", "maire"]
print(guest_list)
print(guest_list [0].title())
print(guest_list [1].title())
print(guest_list [2].title())
print(guest_list[0].title()+" "+"can't make it" +"" +".")

guest_list = ["corey", "ciera", "maire"]
guest_list[0]= "Kayla"
print(guest_list)
#i just changed my first guest name from corey to kayla since corey couldnt make it.
print(guest_list [0].title())
print(guest_list [1].title())
print(guest_list [2].title())
message = "I'd like to invite" +" "+ guest_list[0].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite" +" "+ guest_list[1].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite" +" "+ guest_list[2].title() +" "+ "to dinner next week" +"."
print(message)
print("I found a bigger table!")
guest_list = ["kayla", "ciera", "maire"]
guest_list.insert(0, "vivian") 
guest_list.insert(3,"camryn")
guest_list.insert(5,"jill")
print(guest_list)
#boom! i just added more guest in a specific order!
message = "I'd like to invite you " +" "+ guest_list[0].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite you" +" "+ guest_list[1].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite you" +" "+ guest_list[2].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite you" +" "+ guest_list[3].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite you" +" "+ guest_list[4].title() +" "+ "to dinner next week" +"."
print(message)
message = "I'd like to invite you" +" "+ guest_list[5].title() +" "+ "to dinner next week" +"."
print(message)
print(guest_list)
print("I only have space for only two guest now!")
print("Sorry I couldn't let you come" +" "+ guest_list[5] +".")
print("Sorry I couldn't let you come" +" "+ guest_list[4] +".")
print("Sorry I couldn't let you come" +" "+ guest_list[3] +".")
print("Sorry I couldn't let you come" +" "+ guest_list[2] +".")
guest_list.pop(4)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop()
print(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
#Sorting a list permanently
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars) 

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars) 
#sorting a list temporarily
cars = ["bmw", "audi", "toyota", "subaru"] #original list
print(sorted(cars))
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)
#notice the .reverse() doesnt sort backwork alphabetically; it simply reverses the order of the list
#you can quickly find the list by usuing the "len()" function.
cars = ["bmw", "audi", "toyota", "subaru"]
len(cars)
#Python 4)
magicians = ["alice", "davaid", "carolina"]
for magician in magicians:
    print(magician) 
#for every magician in the list of magicians, print the magician's name. The output is a simple printout of each name in the list
magicians = ["alice", "davaid", "carolina"]
for magician in magicians:
    print(magician.title() +" "+"that was a great trick!")
    print("I can't wait to see your next trick," + " " + magician.title() +".\n")

print("Thank you, everyone. That was a great magic show!")
favorite_pizza =["cheese", "pepperoni", "sausage"]
for pizza in favorite_pizza:
    print(pizza.title())
    print("I like" +" "+ pizza.title()+" "+"pizaa")
    print("I love pizza!")
pets= ["turtles", "cats", "dogs"]
print(pets)
for pet in pets:
    print(pet.title() + " "+ "would make a really great pet!")

#usuing the "range() function"
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)  #*
print(squares)
#List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
 #same thing as to whats above
numbers = []
for value in range(1,21):
    print(value)
candy = ["lolli pops", "sweet tarts", "bubble gum", "reeses"]
print(candy)
for piece in candy:
    print(piece.title()[1:])


