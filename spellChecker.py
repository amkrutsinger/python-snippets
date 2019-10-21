# CS5 
# Filename: hw3pr1.py
# Name: Anna Krutsinger
# Problem description: SPAM! - a spell checking program

import time
memo = {}

def ED(first, second):
    """Returns the edit distance between the strings first and second"""
    if first == '': 
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = 1 + ED(first[1:], second[1:])
        deletion = 1 + ED(first[1:], second)
        insertion = 1 + ED(first, second[1:])
        return min(substitution, deletion, insertion)


# Function #1
def fastED(first, second, memo):
    """fastED is ED()2.0, as in: it returns the edit distance between the first and second string
       but does it much faster than ED
       Arguments: first, first string
                  second, second string
                  memo, a Python dictionary
       Returns: integer value for the minimum edit distance
       """
    if (first, second) in memo:
        return memo[(first, second)]
    elif first == "":
        return len(second)
    elif second == "":
        return len(first)
    elif first[0] == second[0]: # match found!
        match = fastED(first[1:], second[1:], memo)
        memo[(first, second)] = match
        return match
    else:
        sub = 1 + fastED(first[1:], second[1:], memo) # substitution
        delt = 1 + fastED(first[1:], second, memo) # deletion
        ins = 1 + fastED(first, second[1:], memo) # insertion
        answer = min(sub, delt, ins)
        memo[(first, second)] = answer
        return answer


# Function 2
def topNmatches( word, nummatches, ListOfWords ):
    """topNmatches finds the number of best matches in a ListOfWords to the inputted word using FastED() and outputs
                   them in an alphabetical list 
       Arguments: word, a string which is the word to match using fastED method
                  nummatches, an integer which is 0 or greater
                  ListOfWords, a list of strings against which to match word
       Returns: an alphabetically-sorted list of the total of nummatches words from ListOfWords that have the lowest 
                edit-distance scores with the input word
    """
    scores = list(map(lambda x: (fastED(word, x, memo), x), ListOfWords)) # creates a list of tuples in the form of (score, words)
    scores.sort() # sorts the tuples
    finalanswer = [scores[i][1] for i in range(nummatches)] # a list of the corresponding words to the lowest ED with length of nummatches-1
    finalanswer.sort() # alphabetizes the list
    return finalanswer # returns the list


# Function 3
def spam():
    """spam checks if the user inputted word matches any of the words in a text file dictionary, returning 'Correct' if it does
        and the user inputted word is wrong, spam returns a list of 10 words with the best edit distances and the computation time
        needed to get the list of words"""
    f = open("3esl.txt")
    contents = f.read()
    words = contents.split("\n")
    while(True):
        userInput = input("spell check> ")
        if userInput == "":
            print("")
        elif userInput in words:
            print("Correct")
        else:
            startTime = time.time()
            myLowestWords = topNmatches(userInput, 10, words)
            endTime = time.time()
            print("Suggested possible words: ", *myLowestWords, sep = "\n") 
            print("Calculated time: ", endTime - startTime)
        