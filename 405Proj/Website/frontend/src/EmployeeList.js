
import React, { Component } from 'react';
import logo from './logo.svg';
//import './EmployeeList.css'
import './App.css';
import './NewEmployee';
import { ThemeProvider } from '@material-ui/core';
import ReactTable from "react-table-6";
import 'react-table-6/react-table.css';

class Table extends Component 
{
    constructor(props) 
    {
       super(props) 
       this.state = { 
         employees: []
       }
    }

    componentDidMount(){
         this.getItems();
    }

    getItems(){
      fetch( "/employees").then(response => response.json())
      .then(response => this.setState({employees: response}));
    }


/*     renderTableHeader() {
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
     } */
  
     render() 
     {
         //const { data } = this.state.employees;
         return (
           <div>
             <ReactTable
               data = { this.state.employees }
               columns={[
                  {
                    Header: "ID",
                    accessor: "employee_id"  
                  },
                  {
                   Header: "Name",
                   accessor: "employee_name"
                  
                 },
                 {
                   Header: "Email",
                   accessor: "employee_email"
                 
                 }
               ]}
               defaultPageSize={20}
               style={{
                 height: "400px" // This will force the table body to overflow and scroll, since there is not enough room
               }}
               className="-striped -highlight"
             />
             <br />
           </div>
         );
       }
      
    
 }

 export default Table;

