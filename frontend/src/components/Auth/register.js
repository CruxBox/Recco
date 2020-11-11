import React, { useState } from "react";
import axios from "axios";
import loginImg from "../../login.svg";

export const Register = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    //const data = new FormData(event.target);
    var data = {
      username: username,
      password: password,
      email:email
    };
    data = JSON.stringify(data);
    var config = {
      method: "post",
      url: "http://127.0.0.1:8000/users/register",
      headers: {
        "Content-Type": "application/json",
      },
      data: data,
    };

    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        localStorage.setItem("user", JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
    <div className="base-container" ref={props.containerRef}>
      <div className="header">Register</div>
      <div className="content">
        <div className="image">
          <img src={loginImg} alt="Register" />
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form">
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                type="text"
                name="username"
                placeholder="username"
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                type="email"
                name="email"
                placeholder="email"
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                type="password"
                name="password"
                placeholder="password"
              />
            </div>
          </div>
          <div className="footer">
        <button type="submit" className="btn">
          Register
        </button>
      </div>
        </form>
      </div>
    </div>
  );
};
