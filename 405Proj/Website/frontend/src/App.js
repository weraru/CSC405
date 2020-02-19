import React, { useEffect, useState } from 'react';
import './App.css';
import homePage from './homePage';
import SignInSide from './SignInSide';
import Nav from './Nav';
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import createAccountPage from './createAccountPage';
import forgotPassword from './forgotPassword';
import EmployeePage from './EmployeePage'

function App() {
  useEffect(() => {
    fetch("/employees").then(response => 
      response.json().then(data => {
        console.log(data)
    })
    );
  }, []);
  return (
    <Router>
;      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={homePage} />
          <Route path="/login" component={SignInSide} />
          <Route path="/createaccount" component={createAccountPage} />
          <Route path="/forgotpassword" component={forgotPassword} />
          <Route path="/EmployeePage" component={EmployeePage}/>
        </Switch>
      </div>
    </Router>
  );
}


/* putting commemtns in here is weird anyways... 
where "Login here" this will be a redirectional to the login page
this login page will be linked a href= ... */
export default App;
