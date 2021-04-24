import React,{useState} from 'react'
import { useHistory } from 'react-router-dom'; 
import axios from "axios";
import { toast } from 'react-toastify';


const localState = JSON.parse(localStorage.getItem("user"));
//var state=Object.keys(localState).length === 0 && localState.constructor === Object;
var state=true;
console.log(state)
export const UserContext = React.createContext({ token: '', auth: !state,details:{} });
export const  UserProvider = ({ children }) => {
    // User is the name of the "data" that gets stored in context
    //const history = useHistory();
    const [user, setUser] = useState({ token: '', auth: !state,details:{} });
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
     //var info=JSON.parse(localStorage.getItem("user"))
      var config = {
        method: 'delete',
        url: 'http://127.0.0.1:8000/users/token-auth/logout',
        headers: { 
          'Authorization': `Token`
        },
      };
      // axios(config)
      // .then(function (response) {

      // })
      // .catch(function (error) {
      //   console.log(error);
      // })

        //console.log(info)
        setUser((user) => ({
          name: '',
          auth: false,
        }));
        localStorage.setItem("user","{}");
    };
  
    return (
      <UserContext.Provider value={{ user, login, logout }}>
        {children}
      </UserContext.Provider>
    );
  }
