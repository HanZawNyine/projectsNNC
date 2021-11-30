package main

import (
	"fmt"
	"strconv"
	"unsafe"
)

func compress(data string) int {
	shift := 0
	for _, v := range data {
		// fmt.Printf("%c %T %d\n", v, v, v)
		shift <<= 7
		shift |= int(v)
		// fmt.Printf("%b\n",shift)
	}
	return shift
}

func decompress(decompressData int) string {
	orgData := ""
	for v := 0; v < len(IntegerToBinary(decompressData))-1; v += 7 {
		// fmt.Printf("v : %d\n",v)
		bits := decompressData >> v & 0b1111111
		// fmt.Printf("%b %d\n", bits, bits)
		orgData += fmt.Sprintf("%c", bits)

	}
	// fmt.Println(orgData)
	orgData = Reverse(orgData)
	// fmt.Println(orgData)
	return orgData
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func IntegerToBinary(n int) string {
	return strconv.FormatInt(int64(n), 2)
}

func main() {
	data := "Hello"
	fmt.Println("Original Data : ", data)
	fmt.Println("Original Sizes : ", unsafe.Sizeof(data), "bytes")
	fmt.Println("************************************")

	shift := compress(data)
	fmt.Printf("Compresed Data : %b\n", shift)
	fmt.Printf("Compresed Sizes : %d bytes\n", unsafe.Sizeof(shift))
	fmt.Println("************************************")

	decomData := decompress(shift)
	fmt.Printf("Decompressed Data : %v\n", decomData)
	fmt.Printf("Decompressed Sizes : %d bytes\n", unsafe.Sizeof(decomData))
	fmt.Println("************************************")

}
