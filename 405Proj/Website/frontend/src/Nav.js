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
            <Link style={navStyle} to='/login' exact>
            <li>Home</li>
            </Link>

        </ul>
    </nav>
  );
}
/* Navigation */
export default Nav;
