def Main():
    # Having brackets is the python 3.X way
    print("test")

    # Loose typing means python figures out the type in run time also means you
    #don't need to define it as you would in C languages.
    numOfLoops = askuser()
    x = 1
    #white space is important in python since there is no brackets! (normally 4 spaces)
    if numOfLoops is None:
        numOfLoops = askuser()
    elif numOfLoops > 9:
        print("Too big of a number try again")
        numOfLoops = askuser()


    while x <= numOfLoops:
        print(x)
        x = x + 1

    lists = ["cat", "dog", "rat", "tuna", "tree"]
    dictionary = {"A": 1, "B": 2, "C": 3, "Z": 99}
    #examples of cool for loops

    for animal in lists:
        print(animal)
    for key, value in dictionary.items():
        print(key, value)

#functions!
def askuser():
    # python 3.x messes with how inputs are taken, this way we force an int type
    #on an input otherwise it will act as a string
    return int(input("how many times should this loop: "))

#If you use a main function make sure to call it at the end!
Main()
