def io():
    """ This function demonstrates reading and writing text files and
    binary files. """
    
    # First, let's read a small text file
    f1 = open("small.txt", "r")  # Open text file for reading
    text = f1.read()  # Read the entire contents of the file into a string
    f1.close() # Always close files after opening them!
    print("I just read in ", text)

    f2 = open("output1.txt", "w")  # Open text file for writing
    spam = ["s", "p", "a", "m"]
    for char in spam:
        f2.write(char + "\n")  # write each character followed by a newline
    f2.close()

    # mystery is a list of numbers between 0 and 255, each corresponding
    # to one byte of data.  That is, each one is the decimal representation
    # of an 8-bit number
    myListOfBytes = [98, 101, 97, 118, 101, 114]
    # The "wb" below means open this file for writing binary data
    f3 = open("mystery.txt", "wb") 
    f3.write(bytes(myListOfBytes)) # Convert numbers to bytes and write out!
    f3.close()

    # The "rb" below means open this file for reading binary data
    f4 = open("mystery.txt", "rb")
    readBytes = f4.read()
    f4.close()
    listOfBytes = list(readBytes) # convert bytes to list of numbers
    print(listOfBytes)  # print the actual list of bytes
    print(readBytes)    # print the bytes as characters

