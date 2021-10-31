class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene:
            # print('original : ',bin(self.bit_string))
            self.bit_string <<= 2  # shift left two bits
            # print('<<=2 ',bin(self.bit_string))
            if nucleotide == 'A':
                self.bit_string |= 0b0000000
            elif nucleotide == 'B':
                self.bit_string |= 0b0000001
            elif nucleotide == 'C':
                self.bit_string |= 0b0000010
            elif nucleotide == 'D':
                self.bit_string |= 0b0000011

            elif nucleotide == 'E':
                self.bit_string |= 0b0000100
            elif nucleotide == 'F':
                self.bit_string |= 0b0000101
            elif nucleotide == 'G':
                self.bit_string |= 0b0000110
            elif nucleotide == 'H':
                self.bit_string |= 0b0000111

            elif nucleotide == 'I':
                self.bit_string |= 0b0001000
            elif nucleotide == 'J':
                self.bit_string |= 0b0001001
            elif nucleotide == 'K':
                self.bit_string |= 0b0001010
            elif nucleotide == 'L':
                self.bit_string |= 0b0001011

            elif nucleotide == 'M':
                self.bit_string |= 0b0001100
            elif nucleotide == 'N':
                self.bit_string |= 0b0001101
            elif nucleotide == 'O':
                self.bit_string |= 0b0001110
            elif nucleotide == 'P':
                self.bit_string |= 0b0001111

            elif nucleotide == 'Q':
                self.bit_string |= 0b0010000
            elif nucleotide == 'R':
                self.bit_string |= 0b0010001
            elif nucleotide == 'S':
                self.bit_string |= 0b0010010
            elif nucleotide == 'T':
                self.bit_string |= 0b0010011

            elif nucleotide == 'U':
                self.bit_string |= 0b0010100
            elif nucleotide == 'V':
                self.bit_string |= 0b0010101
            elif nucleotide == 'W':
                self.bit_string |= 0b0010110
            elif nucleotide == 'X':
                self.bit_string |= 0b0010111

            elif nucleotide == 'Y':
                self.bit_string |= 0b00110000
            elif nucleotide == 'Z':
                self.bit_string |= 0b00110001
            elif nucleotide == 'a':
                self.bit_string |= 0b00110010

            elif nucleotide == 'b':
                self.bit_string |= 0b00110011
            elif nucleotide == 'c':
                self.bit_string |=0b00110100
            elif nucleotide == 'd':
                self.bit_string |=0b00110101

            elif nucleotide == 'e':
                self.bit_string |= 0b00110110

            elif nucleotide == 'f':
                self.bit_string |= 0b00111001
            elif nucleotide == 'g':
                self.bit_string |= 0b00111010
            elif nucleotide == 'h':
                self.bit_string |= 0b00111011

            elif nucleotide == 'i':
                self.bit_string |= 0b00111100
            elif nucleotide == 'j':
                self.bit_string |= 0b00111101
            elif nucleotide == 'k':
                self.bit_string |= 0b00111110

            elif nucleotide == 'l':
                self.bit_string |= 0b00111111
            elif nucleotide == 'm':
                self.bit_string |= 0b01000000
            elif nucleotide == 'n':
                self.bit_string |= 0b01000001

            elif nucleotide == 'o':
                self.bit_string |= 0b01000010
            elif nucleotide == 'p':
                self.bit_string |= 0b01000011
            elif nucleotide == 'q':
                self.bit_string |= 0b01000100

            elif nucleotide == 'r':
                self.bit_string |=0b01000101
            elif nucleotide == 's':
                self.bit_string |=0b01000110
            elif nucleotide == 't':
                self.bit_string |=0b01000111

            elif nucleotide == 'u':
                self.bit_string |= 0b01000100
            elif nucleotide == 'v':
                self.bit_string |=0b01000101
            elif nucleotide == 'w':
                self.bit_string |=0b01000110

            elif nucleotide == 'x':
                self.bit_string |=0b01000111
            elif nucleotide == 'y':
                self.bit_string |=0b01001000
            elif nucleotide == 'z':
                self.bit_string |=0b01001001

            elif nucleotide == '!':
                self.bit_string |= 0b01001010
            elif nucleotide == '@':
                self.bit_string |= 0b01001011
            elif nucleotide == '#':
                self.bit_string |=0b01001100

            elif nucleotide == '$':
                self.bit_string |=0b01001110
            elif nucleotide == '%':
                self.bit_string |=0b01001111
            elif nucleotide == '^':
                self.bit_string |=0b01010000

            elif nucleotide == '&':
                self.bit_string |=0b01010001
            elif nucleotide == '*':
                self.bit_string |=0b01010010
            elif nucleotide == '(':
                self.bit_string |=0b01010011

            elif nucleotide == ')':
                self.bit_string |=0b01010100
            elif nucleotide == '-':
                self.bit_string |=0b01010101
            elif nucleotide == '_':
                self.bit_string |=0b01010110

            elif nucleotide == '=':
                self.bit_string |=0b01010111
            elif nucleotide == '+':
                self.bit_string |=0b01011000
            elif nucleotide == '`':
                self.bit_string |=0b01011001

            elif nucleotide == '/':
                self.bit_string |=0b01011010
            elif nucleotide == "\\":
                self.bit_string |=0b01011011
            elif nucleotide == '>':
                self.bit_string |=0b01011100

            elif nucleotide == '<':
                self.bit_string |=0b01011101
            elif nucleotide == '?':
                self.bit_string |=0b01011110
            elif nucleotide == ',':
                self.bit_string |=0b01011111

            elif nucleotide == '.':
                self.bit_string |=0b01100000
            elif nucleotide == '{':
                self.bit_string |=0b01100001
            elif nucleotide == '}':
                self.bit_string |=0b01100010

            elif nucleotide == '[':
                self.bit_string |=0b01100011
            elif nucleotide == ']':
                self.bit_string |=0b01100100
            elif nucleotide == '"':
                self.bit_string |=0b01100101

            elif nucleotide == "'":
                self.bit_string |=0b01100110
            elif nucleotide == ':':
                self.bit_string |=0b01100111
            elif nucleotide == ';':
                self.bit_string |=0b01101000

            elif nucleotide == "1":
                self.bit_string |= 0b01101001
            elif nucleotide == '2':
                self.bit_string |= 0b01101010
            elif nucleotide == '3':
                self.bit_string |=0b01101011

            elif nucleotide == "4":
                self.bit_string |=0b01101100
            elif nucleotide == '5':
                self.bit_string |=0b01101101
            elif nucleotide == '6':
                self.bit_string |=0b01101110

            elif nucleotide == "7":
                self.bit_string |=0b01101111
            elif nucleotide == '8':
                self.bit_string |=0b01110000
            elif nucleotide == '9':
                self.bit_string |=0b01110001

            elif nucleotide == "0":
                self.bit_string |=0b01110010
            elif nucleotide == " ":
                self.bit_string |=0b01110010
            else:
               print("none : ",self.bit_string,bin( self.bit_string))
            #print(f'{nucleotide}:{bin(self.bit_string)}')


          #  else:
                #raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # [::-1] reverses string by slicing backward

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof

    original: str = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=/\\?.,'";: 1234567890"""
    print("original :",original)
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("compressed data bin is {} ".format(bin(compressed.bit_string)))
    print("compressed data decimal is {} ".format(compressed.bit_string))
    #print("Your Data :", compressed)
    #print("original and decompressed are the same: {}".format(original == compressed.decompress()))
