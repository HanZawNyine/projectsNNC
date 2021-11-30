package main

import (
	"encoding/json"
	"log"
)

type Person struct {
	FirstName string `json:"firstName"`
	LastName  string `json:"lastName"`
}

func main() {
	myjson := `
	[
		{
			"firstName":"HanZaw",
			"lastName":"Nyine"
		},
		{
			"firstName":"win",
			"lastName":"htut"
		}
	]`
	var Unmarshaled []Person
	err := json.Unmarshal([]byte(myjson), &Unmarshaled)
	if err != nil {
		log.Println("Error ", err)
	}
	log.Println(Unmarshaled)
}
