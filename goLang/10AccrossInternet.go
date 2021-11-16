package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	resp, _ := http.Get("https://www.w3schools.com/tags/tag_textarea.asp")
	fmt.Println(resp)
	bytes, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(bytes)
	strBody := string(bytes)
	fmt.Println(strBody)
	resp.Body.Close()
}
