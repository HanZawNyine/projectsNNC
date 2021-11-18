package main

import (
	"fmt"
)

func main() {
	n, err := fmt.Println("Hello", 0, 1, true)
	_,_ =fmt.Println(n, err)

}
