import React, { Component,Fragment } from "react";
import { Link } from "react-router-dom";

export default class Movies extends Component{
    state = {
        movies: []
    };

    componentDidMount() {
        this.setState({
            movies: [
                { id: 1, title: "The Venom", runtime: 142 },
                { id: 2, title: "The Denom", runtime: 152 },
                { id: 3, title: "The Cenom", runtime: 132 },
                { id: 4, title: "The Eenom", runtime: 122 },
                { id: 5, title: "The Fenom", runtime: 112 },
                
            ]
        })
    }

    render() {
        return (
            <Fragment>
                <h2>Choose a movies</h2>
                <ul>{this.state.movies.map((m) => (
                    <li key={m.id}>
                        <Link to={`/movies/${m.id}`}>
                            {m.title}
                        </Link>
                    </li>
                ))}</ul>
           </Fragment>
        );
    }
}