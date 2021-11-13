package main

import "fmt"

func main() {
	a := 10
	b := &a
	fmt.Println(*b)
	*b = 5
	fmt.Println(a)
	*b = *b * *b
	fmt.Println(a)
}
