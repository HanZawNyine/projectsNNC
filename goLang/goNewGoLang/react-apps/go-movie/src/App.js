import React, {  } from "react";
import { BrowserRouter as Router, Switch, Route, Link, useParams,useRouteMatch } from 'react-router-dom';
import Movies from './components/movies.js'
import Admin from './components/admin.js'
import Home from './components/home.js'
import Categories from './components/Categories.js'
import OneMovie from "./components/OneMovie.js";

export default function App() {
  return (
    <Router>
    <div className="container">
      <div className="row">
        <h1 className="mt-3">Go Watch Movies</h1>
        <hr className="mt-3" />       
      </div>
      <div className="row">
        <div className="col-md-2">
          <nav>
            <ul className="list-group">
              <li className="list-group-item">
                <Link to="/">Home</Link>  
              </li>
              <li className="list-group-item">
                <Link to="/movies">Movies</Link>      
              </li>
              <li className="list-group-item">
                <Link to="/admin">Admin</Link>           
                </li>
                <li className="list-group-item">
                <Link to="/by-category">By Categories</Link>           
              </li>
            </ul>
          </nav>
          </div>
          
          <div className="col-md-10">

            <Switch>
             
              <Route path="/movies/:id" component={OneMovie}/>
                

              <Route path="/admin">
                <Admin />
              </Route>

              <Route path="/movies">
                <Movies />
              </Route>

              <Route exact path="/by-category">
                <CategoryPage />
              </Route>
              
              <Route
                exact
                path="/by-category/drama"
                render={(props) => <Categories {...props} title={`drama`} />}
              />

               <Route
                exact
                path="/by-category/comedy"
                render={(props) => <Categories {...props} title={`comedy`} />}
              />
                <Route
                exact
                path="/by-category/action"
                render={(props) => <Categories {...props} title={`action`} />}
              />

              <Route path="/">
                <Home />
              </Route>

            </Switch>
        </div>
        
      </div>
      </div>

      </Router>
  );
}

function Movie() {
  let {id} = useParams()
  return <h2>Movies id:{id}</h2>
}

function CategoryPage() {
  let { path,url } = useRouteMatch(); 
  return (
    <div>
      <h2>CategoryPage</h2>
      <ul>
        <li><Link to={`${url}/comedy`}>Comedy</Link></li>
        <li><Link to={`${url}/drama`}>Drama</Link></li>
        <li><Link to={`${path}/action`}>Action</Link></li>
      </ul>
    </div>
    
  );
  
}