import React, { useEffect, useState } from 'react';
import './App.css';
import homePage from './homePage';
import SignInSide from './SignInSide';
import Nav from './Nav';
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SignUp from './SignUp';
import forgotPassword from './forgotPassword';
import EmployeePage from './EmployeePage';
import {ProtectedRoute} from "./protected.route";
import 'bootstrap/dist/css/bootstrap.min.css';

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
          <Route path="/" exact component={SignInSide} />
          <Route path="/login" component={SignInSide} />
          <Route path="/signup" component={SignUp} />
          <Route path="/forgotpassword" component={forgotPassword} />
          <ProtectedRoute
          path="/EmployeePage" component={EmployeePage}/>
        </Switch>
      </div>
    </Router>
  );
}


/* putting commemtns in here is weird anyways... 
where "Login here" this will be a redirectional to the login page
this login page will be linked a href= ... */
export default App;
