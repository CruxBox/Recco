import React, { useState } from "react";
import { Link, useHistory } from 'react-router-dom';
import axios from "axios";
import { UserContext } from './userContext';
import { toast } from 'react-toastify';
import loginImg from "../../login.svg";

export const Login = (props) => {
  const { login } = React.useContext(UserContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory({});

  function handleSubmit(event) {
    event.preventDefault();
    //const data = new FormData(event.target);
    var data = {
      username: username,
      password: password,
    };
    data = JSON.stringify(data);
    var config = {
      method: "post",
      url: "http://127.0.0.1:8000/users/token-auth/login",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        localStorage.setItem("user",JSON.stringify(response.data))
        toast.success('Logged in Succesfully', {
          position: "bottom-right",
          autoClose: 2000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          });
          login(JSON.stringify(response.data))
          setUsername("");
          setPassword("")
          history.push({
         pathname: '/home'
      })
        
      })
      .catch(function (error) {
        console.log(error);
        toast.error('Server Error', {
          position: "bottom-right",
          autoClose: 2000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          });
      });
  }

  return (
    <div className="base-container" ref={props.containerRef}>
      <div className="header">Login</div>
      <div className="content">
        <div className="image">
          <img src={loginImg} alt="Login" />
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form">
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                name="username"
                placeholder="username"
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                name="password"
                placeholder="password"
              />
            </div>
            <div className="footer">
              <button type="submit" className="btn">
                Login
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};
