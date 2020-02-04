import React from 'react';
import './App.css';
import homePage from './homePage';
import SignInSide from './SignInSide';
import Nav from './Nav';
import {BrowserRouter as Router, Switch, Route } from 'react-router-dom';

function App() {
  return (

    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path="/" exact component={homePage} />
          <Route path="/login" component={SignInSide} />
        </Switch>
      </div>
    </Router>
  );
}


/* putting commemtns in here is weird anyways... 
where "Login here" this will be a redirectional to the login page
this login page will be linked a href= ... */
export default App;
