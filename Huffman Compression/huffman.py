#
# huffman.py
#
# Name: Anna Krutsinger
# Pair programmed: Louis S

class HuffmanTree(object):
    def __init__(self, symbol=None, left=None, right=None, freq=None): 
        """__init__ is the classes constructor, so it takes in data members
        of an object, and constructs a HuffmanTree object with data members
        symbol, left, right and freq"""
        self.left = left
        self.symbol = symbol
        self.right = right
        self.freq = freq

    def read_dict(self, d):
        """read_dict takes a dictionary whose keys are binary codes and 
        whose values are symbols, and populates the HuffmanTree object so that 
        every symbol is represented by its code."""
        leftDict = {} 
        rightDict = {}
        if d == {}:
            return ()
       
        for key in d: 
            if key[0] == "0" and key != "0": # checks unique key    
                leftDict[key[1:]] = d[key]
            elif key[0] == "1" and key != "1": # checks if unique key
                rightDict[key[1:]] = d[key]
        
        if "0" in d:
            self.left  = HuffmanTree(symbol = d['0']) # be sure that it is a leaf
        else:
            self.left = HuffmanTree() # builds the left subtree
            self.left.read_dict(leftDict) # recurses on left again
        
        if "1" in d:
            self.right = HuffmanTree(symbol = d['1']) # be sure that it is a left
        else:
            self.right = HuffmanTree() # builds right subtree
            self.right.read_dict(rightDict)


    def __repr__(self):
        """overrides repr method such that the “official” string representation 
        of an object in the form of a tuple is printed when print() is called"""
        if self.symbol == None: 
            return "(" + self.left.__repr__() + ", " + self.right.__repr__() + ")"
        else: 
            return self.symbol

    def find_char(self, code):
        """find_char takes a binary string and finds the code that corresponds to the 
        character that is represented by a prefix of the string, returning a tuple
        with the matching symbol and the number of bits read from the binary code to 
        find the matching symbol"""
        if self.symbol != None:
            return (self.symbol, 0)
        else:
            if code[0] == '0' :
                left = (self.left.find_char(code[1:])[0], 1+ self.left.find_char(code[1:])[1])  
                return left
            else:
                right = (self.right.find_char(code[1:])[0], 1+ self.right.find_char(code[1:])[1])
                return right
            
    
    def __add__(self, other): 
        """__add___ takes another instance of a HuffmanTree called 'other' and returns a new tree whose 
        left child is the current tree and whose right child is other"""
        tree = HuffmanTree(left = self, right = other, freq = self.freq + other.freq)
        return tree
    
    def __lt__(self, other):
        """overloaded _lt_ method should take another instance of a HuffmanTree 
        called other and compare them based on their frequencies"""
        return self.freq < other.freq

    
    def get_codes(self, prefix = ""):
        """get_codes returns a list of tuple with a symbol and the binary code corresponding 
        to that symbol"""
        if self.symbol != None:
            return [(self.symbol, "")]
        else:
            left = list(map(lambda x: (x[0], "0" + x[1]), self.left.get_codes()))
            right = list(map(lambda x: (x[0], "1" + x[1]), self.right.get_codes()))
            return left + right


