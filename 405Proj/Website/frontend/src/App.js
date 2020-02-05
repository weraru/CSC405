import React from 'react';
import './App.css';
import homePage from './homePage';
import SignInSide from './SignInSide';
import Nav from './Nav';
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import createAccountPage from './createAccountPage';
import forgotPassword from './forgotPassword';

function App() {
  return (

    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={homePage} />
          <Route path="/login" component={SignInSide} />
          <Route path="/createaccount" component={createAccountPage} />
          <Route path="/forgotpassword" component={forgotPassword} />
        </Switch>
      </div>
    </Router>
  );
}


/* putting commemtns in here is weird anyways... 
where "Login here" this will be a redirectional to the login page
this login page will be linked a href= ... */
export default App;
