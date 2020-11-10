import "./App.css";
import React from "react";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import Nav from "./components/Nav";
import Login from "./components/Login";
import Home from "./components/Home";
import Footer from "./components/Footer";

function App() {
  return (
    <div>
      <Nav />
      <BrowserRouter>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/login" component={Login} />
      </Switch>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
