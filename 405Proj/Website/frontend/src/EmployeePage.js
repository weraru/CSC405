import React, { Component } from 'react';
import EnhancedTable from './EmployeeList'
import NewEmployee from './NewEmployee'


class EmployeePage extends Component {
    render(){
        return (
            <div>
                <EnhancedTable/>
                <NewEmployee/>
                
            </div>
        );
    }
}

export default EmployeePage;