#include <stdio.h>
#define ARRAY_SIZE 100

int BinToDec(char OrgBin[]);
void DecToHexa(int OrgDecimal);
void DecToOctal(int OrgDecimal);
void DecToBin(int OrgDecimal);

int HexaToDec(char hex[]);

int main(void) {
    int decimal = 0;
//    char chr_bin[20] = "";
//    printf("Enter a Binary Number (0,1) : ");
//    gets(chr_bin);
//    decimal = BinToDec(chr_bin);
//    if (decimal != -1) {
//        printf("Binary Value : %s  == Decimal Value : %d \n", chr_bin, decimal);
//    } else {
//        printf("%s is not a Binary Value\n", chr_bin);
//    }
//

    HexaToDec("9AEa");
//    DecToHexa(decimal);
    DecToOctal(decimal);
//    DecToBin(decimal);

    return 0;
}

int BinToDec(char OrgBin[]) {
    int i = 0, number = 0, decimal = 0;
    while (OrgBin[i] != '\0') {
        number = OrgBin[i] - 48;
        if (number != 0 && number != 1) {
            return -1;
        }
        decimal = (decimal * 2) + number;
        i++;
    }
    return decimal;
}

void DecToHexa(int OrgDecimal) {
    int hexa[100], x = 0, y = 0;

    while (OrgDecimal != 0) {
        hexa[x] = OrgDecimal % 16;
        OrgDecimal = OrgDecimal / 16;
        x++;
    }
    printf("Hexa value : ");
    for (y = x - 1; y >= 0; y--) {
        if (hexa[y] > 9) {
            printf("%c", hexa[y] + 55);
        } else {
            printf("%d", hexa[y]);
        }
    }
}

void DecToOctal(int OrgDecimal) {
    int Oct[100], x = 0, y = 0;
    while (OrgDecimal != 0) {
        Oct[x] = OrgDecimal % 8;
        OrgDecimal = OrgDecimal / 8;
        x++;
    }
    printf("\nOctal value : ");
    for (y = x - 1; y >= 0; y--) {
        printf("%d", Oct[y]);
    }
}

void DecToBin(int OrgDecimal){
    int bin[100],x=0,y=0;
    while (OrgDecimal!=0){
        bin[x]=OrgDecimal%2;
        OrgDecimal=OrgDecimal/2;
        x++;
    }
    printf("\nDec To Binary value : ");
    for (y = x - 1; y >= 0; y--) {
        printf("%d", bin[y]);
    }
}

int HexaToDec(char hex[]){
    int decimal = 0, base = 1,length=0;

    for(length=0;hex[length]!='\0';length++);
    for(int i = length--; i >= 0; i--)
    {
        if(hex[i] >= '0' && hex[i] <= '9')
        {
            decimal += (hex[i] - 48) * base;
            base *= 16;
        }
        else if(hex[i] >= 'A' && hex[i] <= 'F')
        {
            decimal += (hex[i] - 55) * base;
            base *= 16;
        }
        else if(hex[i] >= 'a' && hex[i] <= 'f')
        {
            decimal += (hex[i] - 87) * base;
            base *= 16;
        }
    }
    printf("Hexadecimal number = %s\n", hex);
    printf("Decimal number = %d\n", decimal);

//    return decimal;
}