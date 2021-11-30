package main

import (
	"log"
)

func main() {
	Dog := dog{a:"aa",b:"a"}
	log.Println(Dog)
	print(Dog)
}

type animal interface {
	add() int
	sub() string
}

type dog struct {
	a string
	b string
}

func (s dog) sub() string {
	return "this is sub"
}

func (s dog) add() int {
	return 4
}
func print(a animal) {
	log.Println(a.add(),a.sub())
}
