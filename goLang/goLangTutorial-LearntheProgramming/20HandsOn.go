package main

import "fmt"

type x int

var y x

func main() {
	y = 10
	fmt.Printf("%v",y)
	fmt.Printf("%T",y)
}