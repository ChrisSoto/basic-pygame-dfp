# Mad lib intro
print("Welcome to my Mad Lib!")

print()

name = input("Enter a name: ")
adjective1 = input("Write an adjective: ")
adjective2 = input("One more, please: ")
noun0 = input("A plural noun: ")
verb = input("Input a verb: ")
noun1 = input("Another noun: ")
noun2 = input("And one more noun, please: ")

print()

print("This is where the story can get really silly!")

print()

print("Input one of each of the following, please")

print()
animal = input("An animal: ")
emotion = input("An emotion: ")
superhero = input("A superhero: ")
friend_name = input("A friend's name: ")
country = input("A country: ")
dessert = input("A dessert: ")
year = input("A year: ")
age = input("Your age: ")
favorite_number = input("Your favorite number: ")
age = int(age)
favorite_number = int(favorite_number)
new_number = age + favorite_number
new_number = str(new_number)

print()

madlib = "This morning " + name + " woke up feeling " + adjective1 + ". It is going to be a " + adjective2 + " day! Outside, a bunch of " + noun0 + " were protesting to keep " + verb + " in stores. They began to " + noun1 + " to the rhythm of the " + noun2 + " which made all the " + animal + \
    "s very " + emotion + ". Concerned, " + superhero + " texted " + country + ", who flew " + friend_name + " to " + country + " and dropped " + \
    dessert + " off. " + name + " woke up in the year " + year + " in a world where " + \
    animal + "s ruled the world for the next " + new_number + " years!"

print(madlib)
