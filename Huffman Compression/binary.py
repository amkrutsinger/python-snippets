
def EightBitNumToBinary(num):
    """takes an 8 bit number and converts it into binary"""
    output = ""
    while num > 0:
        output = str(num % 2) + output
        num = num // 2
    padding = 8 - len(output)
    return padding * "0" + output

def BinaryToNum(string):
    """takes an binary number and converts it into number"""
    answer = 0
    for x in string:
        answer = answer * 2 + int(x)
    return answer
