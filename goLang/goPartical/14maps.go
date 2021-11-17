package main

import "fmt"

func main() {
	grades := make(map[string]float32)

	grades["a"] = 1
	grades["b"] = 2
	fmt.Println(grades)
	// delete(grades, "a")
	// fmt.Println(grades)

	for k,v := range grades{
		fmt.Println(k,":",v)
	}
}
