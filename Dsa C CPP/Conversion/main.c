#include <stdio.h>

int BinToDecimal(char bin[]);

void decimalToOctal(int decimal);

void decimalToHexa(int decimal);

void decTobin(int dec);

void hexaToDec(char hexa[]);

int main() {
//    char bin[] = "1111";
//    printf("binary value : %s\n",bin);
//    int decimal = BinToDecimal(bin);
//    decimalToOctal(decimal);
//    decimalToHexa(decimal);
//    decTobin(decimal);
    hexaToDec("9AFe");

    return 0;
}

int BinToDecimal(char bin[]) {
    int i = 0, number = 0, decimal = 0;

    while (bin[i] != '\0') {
        number = bin[i] - 48;
        if (number != 0 && number != 1) {
            return -1;
        }
        decimal = (decimal * 2) + number;

        i++;
    }
    printf("decimal value : %d\n", decimal);
    return decimal;
}

void decimalToOctal(int decimal) {
    int oct[100], x = 0;
    while (decimal != 0) {
        oct[x] = decimal % 8;
        decimal = decimal / 8;
        x++;
    }
    printf("Octal value : ");
    for (int y = x - 1; y >= 0; y--) {
        printf("%d", oct[y]);
    }
    printf("\n");

}

void decimalToHexa(int decimal) {
    int hexa[100], x = 0;
    while (decimal != 0) {
        hexa[x] = decimal % 16;
        decimal = decimal / 16;
        x++;
    }
    printf("Hexa value : ");
    for (int y = x - 1; y >= 0; y--) {
        if (hexa[y] > 9) {
            printf("%c", hexa[y] + 55);
        } else {
            printf("%d", hexa[y]);
        }
    }
    printf("\n");
}

void decTobin(int dec) {
    int bin[100], x = 0, y = 0;
    while (dec != 0) {
        bin[x] = dec % 2;
        dec = dec / 2;
        x++;
    }
    printf("Binary value : ");
    for (int y = x - 1; y >= 0; y--) {
        printf("%d", bin[y]);
    }
}

void hexaToDec(char hexa[]) {
    int length = 0, base = 1, dec = 0;
    for (length = 0; hexa[length] != '\0'; length++);

    for (int y = length --; y >= 0; y--) {
        if (hexa[y] >= '0' && hexa[y] <= '9') {
            dec += (hexa[y] - 48) * base;
            base *= 16;
        }else if (hexa[y] >= 'A' && hexa[y] <= 'F') {
            dec += (hexa[y] - 55) * base;
            base *= 16;
        }else if(hexa[y] >= 'a' && hexa[y] <= 'f'){
            dec += (hexa[y]-87)*base;
            base *= 16;
        }
    }
    printf("Hexadecimal number = %s\n", hexa);
    printf("Decimal number = %d\n", dec);
}
