# CS5 Black, Homework 8
# Filename: hw8pr3.py
# Name: Anna Krutsinger
# Collaborator(s): Louis S
# Description: 20 Questions


def play(tree):
    """play takes a tree as input and plays the game on the tree, 
    returning a new tree that is the result of playing the game on the input tree
        Argument: tree, a tree in the form (question, (yesAnswer), (noAnswer))
    """
    if tree == ():
        return ()
    elif "?" in tree[0]:
        question = tree[0]
        answer = str.lower(input(question + " ")) # gets first question answer
        if answer == "yes":
            return (tree[0],) + (play(tree[1]),) + (tree[2],)
        elif answer == "no":
            return (tree[0],) + (play(tree[2]),) + (tree[2],)
        else:
            question = tree[0]
            answer = str.lower(input(question + " ")) # gets first question answer
    else:
        question = "Is it " + tree[0] + "?"
        answer = str.lower(input(question + " "))
        if answer == "yes":
            print("I got it!")
        elif answer == "no":
            print("Drat!")
            correctAnswer = str.lower(input("What was it? "))
            nextQuestion = input("What's a question that distinguishes between " + tree[0] + " and " + correctAnswer + "? ")
            answer = str.lower(input("What's the answer for " + correctAnswer + "? "))
            if answer == "yes":
                return (nextQuestion, (correctAnswer, None, None), (tree[0], None, None))
            elif answer == "no":
                return (nextQuestion, (tree[0], None, None), (correctAnswer, None, None))


def savetree(tree, fileName):
    """savetree takes a tree and a string corresponding to the name of a file and saves the tree in that file
       Arguments: tree, the tree created using play(tree)
                  fileName, string containing the file name
       Returns: n/a
    """
    stringTree = lorax(tree)
    fileHandle = open(fileName, "w")
    print(stringTree, file = fileHandle)
    fileHandle.close()


def lorax(tree):
    """lorax (because the lorax speaks for the trees to save them!) converts the tree into a string
    in the form: firstQuestion\n Internal Node\n ...Leaf\n
        Argument: tree, a tree entered in as a tuple
        Returns: a string, answer, that represents the tree"""
    answer = ""
    if tree == ():
        return answer
    else:
        if "?" in tree[0]:
            answer += tree[0]
            answer += "\nInternal Node\n" + lorax(tree[1])+ lorax(tree[2])
        else:
            answer += tree[0] + "\nLeaf\n" 
    return answer 

def main():
    print("Welcome to 20 Questions!")
    #loadFile = input("Would you like to load a tree from a file?")
    #fileName = input("What's the name of the file? ")
    tree = ("Is it bigger than a breadbox?", ("an elephant", None, None), ("a mouse", None, None))
    tree = play(tree)
    replay = input("Would you like to play again? ")
    while replay == "yes":
        tree = play(tree)
        replay = input("Would you like to play again? ")
    save = str.lower(input("Would you like to save this tree? "))
    if save == "yes":
        fileName = input("Please enter a file name: ")
        savetree(tree, fileName)
        print("Thank you!  The file has been saved.")
    print("Bye!")

    