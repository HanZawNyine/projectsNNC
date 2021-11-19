package main

import "fmt"

// var a int
type hotdog int
var b hotdog
func main() {
	b= 10
	fmt.Printf("%T\n",b)
}