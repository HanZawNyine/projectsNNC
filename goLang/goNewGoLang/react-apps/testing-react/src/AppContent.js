import React, { Component } from "react";

export default class AppContent extends Component {
    state = {
        posts: []
    };
    fetchList = () => {
        fetch('https:/jsonplaceholder.typicode.com/posts')
            .then((Response) => Response.json())
            .then(json => {
                this.setState({posts:json})
            })
    }
    clickedItem = (x) => {
        console.log("Click",x)
    }
        
    render() {        
        return (
            <p>
                This is AppContent.<br />
                <button onClick={this.fetchList} class="btn btn-primary">Fetch Data</button>     
                <hr />
                <p>Posts is { this.state.posts.length} items long</p>
                <ol>
                    {this.state.posts.map((c) => (
                        <li key={c.id}>
                            <a href="#" onClick={() => this.clickedItem(c.id)}>
                                {c.title}
                            </a>
                        </li>
                    ))

                }

                </ol>
           </p>
           
       )
    }
}