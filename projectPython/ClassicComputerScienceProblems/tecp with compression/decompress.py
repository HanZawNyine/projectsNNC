def decompress(self) -> str:
    gene: str = ""
    for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1 to exclude         sentinel
        bits: int = self.bit_string >> i & 0b11  # get just 2 relevant bits
        if bits == 0b0000000:  # A
            gene += "A"
        elif bits ==0b0000001:
            gene += "B"
        elif bits ==0b0000010:
            gene += "C"
        elif bits ==0b0000011:
            gene += "D"

        elif bits ==0b0000100:
            gene += "E"
        elif bits ==0b0000101:
            gene += "F"
        elif bits ==0b0000110:
            gene += "G"

        elif bits ==0b0000111:
            gene += "H"
        elif bits ==0b0001000:
            gene += "I"
        elif bits ==0b0001001:
            gene += "J"

        elif bits ==0b0001010:
            gene += "K"
        elif bits ==0b0001011:
            gene += "L"
        elif bits ==0b0001100:
            gene += "M"

        elif bits == 0b0001101:
            gene += 'N'

        elif bits ==0b0001110:
            gene += "O"
        elif bits ==0b0001111:
            gene += "P"
        elif bits ==0b0010000:
            gene += "Q"

        elif bits ==0b0010001:
            gene += "R"
        elif bits ==0b0010010:
            gene += "S"
        elif bits ==0b0010011:
            gene += "T"

        elif bits ==0b0010100:
            gene += "U"
        elif bits ==0b0010101:
            gene += "V"
        elif bits ==0b0010110:
            gene += "W"

        elif bits ==0b0010111:
            gene += "X"
        elif bits ==0b00110000:
            gene += "Y"
        elif bits ==0b00110001:
            gene += "Z"

        elif bits ==0b00110010:
            gene += "a"
        elif bits ==0b00110011:
            gene += "b"
        elif bits ==0b00110100:
            gene += "c"

        elif bits ==0b00110101:
            gene += "d"
        elif bits ==0b00110110:
            gene += "e"
        elif bits ==0b00111001:
            gene += "f"

        elif bits ==0b00111010:
            gene += "g"
        elif bits ==0b00111011:
            gene += "h"
        elif bits ==0b00111100:
            gene += "i"

        elif bits ==0b00111101:
            gene += "j"
        elif bits ==0b00111110:
            gene += "k"
        elif bits ==0b00111111:
            gene += "l"

        elif bits ==0b01000000:
            gene += "m"
        elif bits ==0b01000001:
            gene += "n"
        elif bits ==0b01000010:
            gene += "o"

        elif bits ==0b01000011:
            gene += "p"
        elif bits ==0b01000100:
            gene += "q"
        elif bits ==0b01000101:
            gene += "r"

        elif bits ==0b01000110:
            gene += "s"
        elif bits ==0b01000111:
            gene += "t"
        elif bits ==0b01000100:
            gene += "u"

        elif bits ==0b01000101:
            gene += "v"
        elif bits ==0b01000110:
            gene += "w"
        elif bits ==0b01000111:
            gene += "x"

        elif bits ==0b01001000:
            gene += "y"
        elif bits ==0b01001001:
            gene += "z"
        elif bits ==0b01001010:
            gene += "!"

        elif bits ==0b01001011:
            gene += "@"
        elif bits ==:
            gene += "#"
        elif bits ==:
            gene += "$"

        elif bits ==:
            gene += "%"
        elif bits ==:
            gene += "^"
        elif bits ==:
            gene += "&"

        elif bits ==:
            gene += "*"
        elif bits ==:
            gene += "("
        elif bits ==:
            gene += ")"

        elif bits ==:
            gene += "-"
        elif bits ==:
            gene += "_"
        elif bits ==:
            gene += "="

        elif bits ==:
            gene += '`'
        elif bits ==:
            gene += '/'
        elif bits ==:
            gene += "\\"

        elif bits ==:
            gene += '>'
        elif bits ==:
            gene += '<'
        elif bits ==:
            gene += '?'
        elif  bits ==:
            gene += ','

        elif bits == :
            gene += '.'
        elif bits == :
            gene +=  '{'
        elif bits == :
            gene += '}'
        elif bits == :
            gene +='['

        elif bits ==:
            gene +=']'
        elif bits ==:
            gene +='"'
        elif bits ==:
            gene +="'"
        elif bits ==:
            gene +=':'

        elif bits ==:
            gene +=';'
        elif bits ==:
            gene +="1"
        elif bits ==:
            gene +='2'
        elif bits ==:
            gene +='3'

        elif bits ==:
            gene +='4'
        elif bits ==:
            gene +='5'
        elif bits ==:
            gene +='6'
        elif bits ==:
            gene +='7'

        elif bits ==:
            gene +='8'
        elif bits ==:
            gene +='9'
        elif bits ==:
            gene +='0'
        elif bits ==:
            gene +=' '


        else:
            print(" decompress None : ", self.bit_string, bin(self.bit_string))