import React, { Component } from 'react'
import './NewEmployee.css'

class NewEmployee extends Component {
    constructor(props) {
        super(props)

        this.state = {
            usrname: '',
            email: ''
        }

    }

    changeHandler = (e) => {
        this.setState({ [e.target.usrname]: e.target.value })
    }

    addHandler = e => {
        e.preventDefault()
        console.log(this.state)
    }

    renderForm() {
        const { usrname, email } = this.state
        return (
            <form onAdd ={this.addHandler} >
                <div>
                    < input type = "text"
                    name = "usrname"
                    value = {usrname}
                    onChange = {this.changeHandler}
                    placeholder = 'username here'
                    />
                </div>
                <div>
                    <input type="text" 
                    name="email" value={email} 
                    onChange={this.changeHandler}
                    placeholder = 'email here'/>
                </div>
                <button type="Add">Add</button>
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
