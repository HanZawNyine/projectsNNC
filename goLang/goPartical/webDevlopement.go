package main

import (
	"fmt"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1>Hello I am Web Server</h1>")
	fmt.Fprintf(w, "<p>Hello I am %s %s Server</p>","bold","<b>Hello</b>")
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8000", nil)
}
