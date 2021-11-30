package main

import (
	"fmt"
	"net/http"
	"text/template"
)

const port = ":8000"

func main() {
	http.HandleFunc("/", home)
	http.HandleFunc("/about", about)
	fmt.Printf("Starting server localhost%v", port)
	http.ListenAndServe(port, nil)
}

func home(rw http.ResponseWriter, r *http.Request) {
	RenderTemplate(rw, "home.html")
}

func about(rw http.ResponseWriter, r *http.Request) {
	RenderTemplate(rw, "about.html")
}

func RenderTemplate(rw http.ResponseWriter, fileName string) {
	praseTempate, _ := template.ParseFiles(fileName)
	sages := map[string]string{
		"a":"b",
		"b":"c"}
	err := praseTempate.Execute(rw,sages)
	if err != nil {
		fmt.Println(err)
	
	}
	

}
