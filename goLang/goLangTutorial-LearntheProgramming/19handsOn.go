package main

import "fmt"

type zz int
var x zz

func main() {
	fmt.Println(x)
	fmt.Printf("%T\n",x)
	x = 42
	fmt.Println(x)
}