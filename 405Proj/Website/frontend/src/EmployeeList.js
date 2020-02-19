import React, { Component } from 'react';
import logo from './logo.svg';
import './EmployeeList.css'
import './App.css'
import { ThemeProvider } from '@material-ui/core';

class Table extends Component 
{
    constructor(props) 
    {
       super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
       this.state = { //state is by default an object
          employees: []
       }
    }

    componentDidMount(){
         this.getItems();
    }

    getItems(){
      fetch("/employees").then(response => response.json())
      .then(response => this.setState({employees: response}));
    }


    renderTableHeader() {
        let header = ["id", "name", "email"];
        return header.map((key, index) => {
          return React.createElement("th", { key: index }, key.toUpperCase());
        });
      }


 
    renderTableData() 
    {
        return this.state.employees.map((employee, index) => 
        {
           return (
              <tr key={index}>
                 <td>{employee.employee_id}</td>
                 <td>{employee.employee_name}</td>
                 <td>{employee.employee_email}</td>
              </tr>
           )
        })
     }
  
     render() 
     {
        return (
          React.createElement("div", null,
          React.createElement("h1", { id: "title" }, "Employees"),
          React.createElement("table", { id: "employee" },
          React.createElement("tbody", null,
          React.createElement("tr", null, this.renderTableHeader()),
          this.renderTableData()))));
    }
    
 }

 export default Table;