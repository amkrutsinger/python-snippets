import binary
from collections import Counter

from huffman import HuffmanTree

class HuffmanDecoder(object):
    def decode(self, filename):
        self.filename = filename
        self.read_key_file()
        self.read_message_file()
        self.write_to_file()
        
    def read_key_file(self): 
        """read_key_file reads in lines from the filename.txt.HUFFMAN.KEY"""
        fp = open(self.filename + ".KEY")
        numOfSymbols = int(fp.readline())
        self.fileLength = int(fp.readline())
        self.dictionary = {}
        for i in range(numOfSymbols): 
            sym = fp.read(1)
            code = fp.readline().strip()
            self.dictionary[code] = sym
        fp.close()

    def read_message_file(self):
        """read_message_file uncompresseses a binary (byte) file and save the resulting text as self.text
        using the HuffmanTree class's find_char method"""
        f = open(self.filename, "rb")
        readBytes = f.read()
        f.close()
        readBytes = list(readBytes)

        stringOfBits = ""
        for i in range(len(readBytes)):
            stringOfBits += binary.EightBitNumToBinary(readBytes[i])

        self.tree = HuffmanTree()
        self.tree.read_dict(self.dictionary)
        
        toPrint = ""
        for i in range(self.fileLength):
            toPrint += self.tree.find_char(stringOfBits)[0]
            stringOfBits = stringOfBits[ self.tree.find_char(stringOfBits)[1]: ]
        self.text = toPrint
        
    def write_to_file(self):
        """write_to_file writes the text from self.text to a new file called self.filename.HUFFMAN.DECODED"""
        f = open(self.filename + ".DECODED", "w")
        f.write(self.text)
        f.close()
     
if __name__ == "__main__": 
    decoder = HuffmanDecoder()
    decoder.decode("test.txt.HUFFMAN")
