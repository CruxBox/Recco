import React, {useState, useEffect} from 'react';
import { Link, useHistory } from 'react-router-dom';
import { UserContext } from './Auth/userContext';

import './Navbar.css';
function Navbar() {
  const { user,logout } = React.useContext(UserContext);
  const [name, setName] = useState("");
  const history = useHistory({});
 function handleSubmit(event) {
  event.preventDefault();
  var axios = require('axios');
  var config = {
    method: 'get',
    url: `http://127.0.0.1:8000/movies/search/?query=${name}&language=en&max_results=10`,
    headers: { }
  };
  axios(config)
  .then(function (response) {
    console.log(JSON.stringify(response.data));
    setName("");
    history.push({
      pathname: '/list',
      state: { data: response.data }
})
  })
  .catch(function (error) {
    console.log(error);
  });
  } 
  useEffect(() => {
  }, [user]);
  return (
    <div className="Navbar">
      <header>
        <div className="container">
          <div className="row">
            <div className="brand-name"> 
              <a className="logo">Recco</a>
            </div>
      <div className="wrap">
        <form onSubmit={handleSubmit}>
        <div className="search">     
          <input type="text" value ={name} onChange={e => setName(e.target.value)} className="searchTerm" placeholder="What are you looking for?" />
          <button type="submit" className="searchButton">
            <i className="fa fa-search" />
          </button>
          
        </div>
        </form>
      </div>
      &nbsp;
            <div className="navbar">
              <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/upcoming">Upcoming</Link></li>
                <li><Link to="/watchlist">My Watchlist</Link></li>
  <li>{!user.auth && <Link to="/login"> Login </Link>}{user.auth && <a onClick={logout(user)} > Logout </a>}</li>
              </ul>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Navbar;
