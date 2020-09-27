#- This function will print the lyrics of the song "Old MacDonald" for five different animals
#- The user can input an animal from the selection of Cow, Dog, Cat, Sheep, and Pig

animalNum= eval(input("Insert the number that corresponds to an animal (You have the options of 0.cow, 1.dog, 2.cat, 3.sheep, and 4.pig: "))
animal= ["cow", "dog", "cat", "sheep", "pig"]
animalNoise = ["moo", "woof", "meow", "baa", "oink"]

def songPart2(animal):
    #- This is the second line of the song
    a= "And on the farm he had a "
    c=", Ee-igh, Ee-igh, Oh!"
    return(a + animal + c )

def songPart34(animalNoise):
# This is the third and fourth line of the song
# You don't have to replace. Just use the variable in the output.
    a2= "With a moo, moo here  a moo, moo there."
    b2="Here a moo, there a moo, everywhere a moo, moo."
    a2=(a2.replace("moo", animalNoise))
    b2=(b2.replace("moo", animalNoise))
    return(a2 + b2)

def oldMacSong():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print(songPart2(animal[animalNum]))
    print(songPart34(animalNoise[animalNum]))
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


oldMacSong()

