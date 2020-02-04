import React from 'react';
import logo from './logo.svg';
import './App.css';
import homePage from './components/pages/homePage';
import loginPage from './components/pages/loginPage';
import Nav from './components/Nav';

function App() {
  return (
    <div className="App">
      
        <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
          <p>
            Watchmen GPS Tracking App
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Login Here 
          </a>
        </header>
    
    </div>
  );
}
/* putting commemtns in here is weird anyways... 
where "Login here" this will be a redirectional to the login page
this login page will be linked a href= ... */
export default App;
