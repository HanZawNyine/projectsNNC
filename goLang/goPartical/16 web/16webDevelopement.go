package main

import (
	"fmt"
	"net/http"
	"text/template"
)

func index_handler(w http.ResponseWriter, r *http.Request) {

	fmt.Fprintf(w, "<h1>Hello Client </h1>")
}

type NewsAddPage struct {
	Title string
	News  string
}

func agg(w http.ResponseWriter, r *http.Request) {

	p := NewsAddPage{Title: "Agg", News: "News"}
	t, _ := template.ParseFiles("index.html")
	
	fmt.Println(t.Execute(w, p))

}

func main() {
	http.HandleFunc("/", index_handler)
	http.HandleFunc("/agg/", agg)
	http.ListenAndServe(":8000", nil)
}
