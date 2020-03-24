import React, { Component } from 'react'
import './NewEmployee.css'

class NewEmployee extends Component {
    constructor(props) {
        super(props)

        this.state = {
            name: '',
            email: ''
        }

    }

    changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }






    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
    
        var raw = JSON.stringify(this.state);
    
        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };
        fetch('/add', requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
    }


    renderForm() {
        const { name, email } = this.state
        return (
            <form onSubmit={this.submitHandler}>
                <div id = "box">
                    < input id = "font1" type = "text"
                    name = "name"
                    value = {name}
                    onChange = {this.changeHandler}
                   // placeholder = 'username here'
                    
                    />
                </div>
                <div id = "box">
                    <input type="text" 
                    name="email" value={email} 
                    onChange={this.changeHandler}
                    //placeholder = 'email here'
                    id = 'font2'
                    />
                </div>
                <button id="butt" type="Add">Add</button>
            </form>
        )
    }

    render() 
     {
        return (
          React.createElement("div", {id: "head"},
          React.createElement("h3", null, "Add Employee"),
          React.createElement("form", {id: "form"}, this.renderForm())));
    }
}


export default NewEmployee