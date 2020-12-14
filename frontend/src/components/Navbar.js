import React, {useState, useEffect} from 'react';
import { Link, useHistory } from 'react-router-dom';
import { UserContext } from './Auth/userContext';
import axios from "axios";


import './Navbar.css';
function Navbar() {
  const { user,logout } = React.useContext(UserContext);
  const [name, setName] = useState("");
  const history = useHistory({});
 function handleSubmit(event) {
  event.preventDefault();
  console.log(name)
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
      state: { data: response.data,name:name }
})
  })
  .catch(function (error) {
    console.log(error);
  });
  } 
  useEffect(() => {
  }, [user]);
  function rec(e){
    //e.preventDefault();
    console.log(user)
    var info=JSON.parse(localStorage.getItem("user"))
    console.log(info)
    var config = {
      method: 'get',
      url: `http://127.0.0.1:8000/movies/rec/?username=${info.user.username}`,
      headers: { }
    };
    axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
      setName("");
      history.push({
        pathname: '/reccomendations',
        state: { data: response.data,name:"fav" }
  })
    })
    .catch(function (error) {
      console.log(error);
    });


  }

  function Logout(){
    logout(user);
    history.push({
      pathname: '',
})

  }

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
                {user.auth && <li><a onClick={()=>rec()}>My Reccomendations</a></li>}
                {user.auth && <li><Link to="/watchlist">My Watchlist</Link></li>}
  <li>{!user.auth && <Link to="/login"> Login/Register </Link>}{user.auth && <a onClick={Logout} > Logout </a>}</li>
              </ul>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Navbar;
