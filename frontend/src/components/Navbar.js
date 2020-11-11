import React from 'react';
import './Navbar.css';
function Navbar() {
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
            <div className="navbar">
              <ul>
                <li><a href="home" className="active">Home</a></li>
                <li><a href="trending">Trending</a></li>
                <li><a href="upcoming">Upcoming</a></li>
                <li><a href="watchlist">My Watchlist</a></li>
                <li><a href="login">Login/Signup</a></li>
              </ul>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Navbar;
