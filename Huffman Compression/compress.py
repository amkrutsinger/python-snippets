import binary
from collections import Counter

from huffman import HuffmanTree

class HuffmanEncoder(object): 
    def encode(self, filename):
        self.filename = filename
        self.read_text(self.filename)
        self.write_to_files()
        self.print_stats()

    def read_text(self, filename):
        """"read_text creates a Counter object with all of the words in a text file
        and then passes that Counter object to another helper function called make_tree"""
        file = open(filename, "r")
        text = file.read()
        file.close()
        self.text = text
        self.count = Counter(text)
        self.make_tree(self.count)      
                
    def make_tree(self, counter): 
        """make_tree builds a HuffmanTree and creates a dictionary whose keys are symbols and whose values are 
        the binary code for each symbol and then saves the tree as self.tree"""
        # sortedList = sorted(list, key = lambda HuffmanTree: HuffmanTree.freq)
        counterkeys = list(counter)
        myTrees = []
        for i in counterkeys:
            myTrees += [HuffmanTree(symbol = i, freq = counter[i])]
        
       

        while(len(myTrees) > 1):
            lowest = self.lowest(myTrees)
            self.tree = lowest
            myTrees.remove(lowest)
            nextLow = self.lowest(myTrees)
            myTrees.remove(nextLow)
            self.tree = HuffmanTree(right = self.tree, left = nextLow, freq = self.tree.freq + nextLow.freq)
            myTrees += [self.tree]
        
        self.dict = dict(self.tree.get_codes())
        dictionary = dict(list(map(lambda x: (x[1], x[0]), self.tree.get_codes())))
        self.tree.read_dict(dictionary)
        return self.tree

    def lowest(self, L):
        """lowest finds the lowest value in list and returns it"""
        lowest = L[0]
        for i in range(len(L)):
            if L[i] < lowest:
                lowest = L[i]
        return lowest

    def write_to_files(self): 
        """write_to_files saves two files such that if the input file that we wish to compress is 
        called filename.txt, the two output files are called filename.txt.HUFFMAN and 
        filename.txt.HUFFMAN.KEY"""
        compressKey = open(self.filename + ".HUFFMAN.KEY", "w")
        # the number of distinct symbols (that is, the size of the key)
        compressKey.write(str(len(self.dict)) + "\n")
        # the total number of symbols in the original file
        compressKey.write(str(sum(self.count.values())) + "\n")
        for i in self.dict:
            compressKey.write(i + " " + self.dict[i] + "\n")
        compressKey.close()

        stringOfBits = ""
        for i in self.text:
            stringOfBits += self.dict[i]
        
        compressed = open(self.filename + ".HUFFMAN", "wb")
        if len(stringOfBits) % 8 != 0:
            stringOfBits += "0" * (8 - len(stringOfBits)%8)
        
        num = []
        for x in range(len(stringOfBits)//8):
            myByte = stringOfBits[x*8:(x+1)*8]
            num += [binary.BinaryToNum(myByte)]

        self.compressedByteLength = bytes(num)
        compressed.write(self.compressedByteLength)
        compressed.close()


    def print_stats(self):
        """print_stats reports the following statistics: the number of different characters in the input file,
        the total number of bytes in the input file, the number of bytes used to store the compressed text, and 
        the "Asymptotic compression ratio"/the ratio of the number of bytes in the Huffman byte file divided 
        by the length of the original file"""
        print("Number of characters in file:", str(sum(self.count.values())))
        file = open(self.filename, "rb")
        readBytes = file.read()
        file.close()
        listOfBytes = list(readBytes)
        print("Number of bytes in the input file:", len(listOfBytes))
        print("Number of bytes in the compressed file:", len(self.compressedByteLength))
        print("Asymptotic compression ratio:", len(self.compressedByteLength)/len(listOfBytes))
        
        
if __name__ == "__main__":
    encoder = HuffmanEncoder()
    encoder.encode("test.txt")
