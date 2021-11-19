package main

import "fmt"

func main() {
	x := 42
	y := "James Bonds"
	z := true
	fmt.Println(x,y,x)
	fmt.Printf("%v\t%T\n",x,x)
	fmt.Printf("%v\t%T\n",y,y)
	fmt.Printf("%v\t%T\n",z,z)
}