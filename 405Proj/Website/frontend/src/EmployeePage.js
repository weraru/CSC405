import React, { Component } from 'react';
import Tablee from './EmployeeList'
import NewEmployee from './NewEmployee'

class EmployeePage extends Component {
    render(){
        return (
            <div>
                <Tablee/>
                <NewEmployee/>
            </div>
        );
    }
}

export default EmployeePage;