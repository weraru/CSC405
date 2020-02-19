import React, { Component } from 'react';
import Table from './EmployeeList'
import NewEmployee from './NewEmployee'

class EmployeePage extends Component {
    render(){
        return (
            <div>
                <Table/>
                <NewEmployee/>
            </div>
        );
    }
}

export default EmployeePage;