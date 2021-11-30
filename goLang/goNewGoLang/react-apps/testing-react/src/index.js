import React,{ Component } from "react";
import ReactDom from "react-dom";

import AppHeader from "./AppHeader";
import AppContent from "./AppContent";
import AppFooter from "./AppFooter";

import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import './index.css'

class App extends Component{
  render() {
  
    return (
      <div className="app">

        <AppHeader />
        <AppContent />
        <AppFooter />

      </div>
    )
  }
}
ReactDom.render(<App />, document.getElementById("root"));