# MacDonaldLyric.py
# This program print the lyrics of MacDonald
# Writen by: Ali Arefi

def animalLyric(animal, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, oh!\n\
    And  on that farm he had a {0}, Ee-igh, Ee-igh, oh!\n\
    with a {1}, {1} here and {1}, {1} there.\n\
    Here a {1}, there a {1}, everywhere a {1}, {1}.\n\
    Old MacDonald had a farm, Ee-igh, Ee-igh, oh!\n\n".format(animal, sound))

def main():
    animalLyric("cow", "moo")
    animalLyric("sheep", "baa")
    animalLyric("pig", "oink")
    animalLyric("duck", "quack")

main()
