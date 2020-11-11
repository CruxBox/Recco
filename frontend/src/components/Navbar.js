import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
function Navbar() {

  localStorage.setItem('rememberMe', JSON.stringify({hello:"hi"}));
  return (
    <div className="Navbar">
      <header>
        <div className="container">
          <div className="row">
            <div className="brand-name"> 
              <a href className="logo">Recco</a>
            </div>
      <div className="wrap">
        <div className="search">
          <input type="text" className="searchTerm" placeholder="What are you looking for?" />
          <button type="submit" className="searchButton">
            <i className="fa fa-search" />
          </button>
        </div>
      </div>
      &nbsp;
            <div className="navbar">
              <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/upcoming">Upcoming</Link></li>
                <li><Link to="/watchlist">My Watchlist</Link></li>
                <li><Link to="/login">Login/Signup</Link></li>
              </ul>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Navbar;
