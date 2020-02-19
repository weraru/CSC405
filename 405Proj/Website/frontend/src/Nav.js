import React from 'react';
import './App.css';
import {Link} from 'react-router-dom';


function Nav() {

  const navStyle = {
    color: 'white'
  };

  return (
    <nav>
        <h1>Watchmen
        </h1> 
        <ul className ="nav-Links">
            <Link style={navStyle} to='/' exact>
            <li>Home</li>
            </Link>
            <Link style={navStyle} to ='/login'>
            <li>Login</li>
            </Link>
            <Link style={navStyle} to ='/EmployeePage'>
            <li>Employees</li>
            </Link>
        </ul>
    </nav>
  );
}
/* Navigation */
export default Nav;
