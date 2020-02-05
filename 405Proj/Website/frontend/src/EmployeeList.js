import React, { Component } from 'react';
import logo from './logo.svg';
import './EmployeeList.css'
import './App.css'

class Table extends Component 
{
    constructor(props) 
    {
       super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
       this.state = { //state is by default an object
          employees: [
             { id: 1, name: 'Bob'},
             { id: 2, name: 'Hank'},
             { id: 3, name: 'Fred'},
             { id: 4, name: 'Jennifer'}
          ]
       }
    }



    renderTableHeader() {
        let header = Object.keys(this.state.employees[0]);
        return header.map((key, index) => {
          return React.createElement("th", { key: index }, key.toUpperCase());
        });
      }


 
    renderTableData() 
    {
        return this.state.employees.map((employee, index) => 
        {
           const { id, name} = employee//destructuring
           return (
              <tr key={id}>
                 <td>{id}</td>
                 <td>{name}</td>
              </tr>
           )
        })
     }
  
     render() 
     {
        return (
          React.createElement("div", null,
          React.createElement("h1", { id: "title" }, "Employees"),
          React.createElement("table", { id: "employees" },
          React.createElement("tbody", null,
          React.createElement("tr", null, this.renderTableHeader()),
          this.renderTableData()))));
    }
    
 }

 export default Table;