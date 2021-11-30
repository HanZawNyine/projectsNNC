package main

import (
	"fmt"
	"sync"
	"time"
)

var do sync.WaitGroup

func foo(s string) {
	defer do.Done()
	for i := 0; i < 5; i++ {
		fmt.Println(s)
		time.Sleep(time.Microsecond*100)
	}
	
}
func main() {
	do.Add(1)
	go foo("Hello")
	do.Add(1)
	foo("Hay")
	do.Add(1)
	go foo("Hi")
	do.Wait()
}