import React,{useState} from 'react'
import axios from "axios";
import { toast } from 'react-toastify';

export const UserContext = React.createContext({ token: '', auth: true,details:{} });
export const  UserProvider = ({ children }) => {
    // User is the name of the "data" that gets stored in context
    const [user, setUser] = useState({ token: '', auth: true,details:{} });
 var a={"user":{"id":15,"username":"test12","email":"te@te.com","contribution":0},"token":"cb283a71a6054d5a52d4b33794d4dd01ae9e8b35"}
    // Login updates the user data with a name parameter
    const login = (user) => {
      setUser((user) => ({
        token: user.token,
        auth: true,
        details:user.user
      }));
    };
  
    // Logout updates the user data to default
    const logout = (user) => {
      var info=JSON.parse(localStorage.getItem("user"))
      var config = {
        method: 'delete',
        url: 'http://127.0.0.1:8000/users/token-auth/logout',
        headers: { 
          'Authorization': `Token ${info.token}`
        },
      };
      axios(config)
      .then(function (response) {
      })
      .catch(function (error) {
        console.log(error);
      });
      setUser((user) => ({
        name: '',
        auth: false,
      }));
      localStorage.setItem("user","")

    };
  
    return (
      <UserContext.Provider value={{ user, login, logout }}>
        {children}
      </UserContext.Provider>
    );
  }
