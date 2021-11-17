package main

import (
	"fmt"
)

type car struct {
	a uint16
	b uint16
	c int16
	t float64
}

func (c car) kmh() car {
	c.a += 1
	return c
}

func (c *car) mmh(varTest float64) {
	c.t = varTest
}

func main() {
	fmt.Println("Welcome Go")
	a_car := car{1, 2, 3, 5.6}
	fmt.Println(a_car)
	fmt.Println(a_car.kmh())
	fmt.Println(a_car)
	// fmt.Println(a_car.t)
	a_car.mmh(12.5)
	fmt.Println(a_car)
}
