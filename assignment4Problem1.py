#- This function will print the lyrics of the song "Old MacDonald" for five different animals
#- The user can input an animal from the selection of Cow, Dog, Cat, Sheep, and Pig

animalNum= eval(input("Insert the number that corresponds to an animal (You have the options of 1.cow, 2.dog, 3.cat, 4.sheep, and 5.pig: "))
animal= ["cow", "dog", "cat", "sheep", "pig"]
animalNoise = ["moo", "woof", "meow", "baa", "oink"]

def songPart2(animal):
    #- This is the second line of the song
    a= "And on the farm he had a "
    c=", Ee-igh, Ee-igh, Oh!"
    print (a + animal + c )

def songPart34(animalNoise):
# This is the third and fourth line of the song
    a2= "With a moo, moo here  a moo, moo there."
    b2="Here a moo, there a moo, everywhere a moo, moo."
    print(a2.replace("moo", animalNoise))
    print(b2.replace("moo", animalNoise))

def oldMacSong():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print(songPart2(animal[animalNum]))
    print(songPart34(animalNoise[animalNum]))
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


oldMacSong()

