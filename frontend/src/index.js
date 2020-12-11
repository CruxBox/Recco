import React from "react";
import ReactDOM from "react-dom";
import { UserProvider } from './components/Auth/userContext';
import App from "./App.js";

ReactDOM.render(
    <UserProvider>
      <App />
    </UserProvider>,
  document.getElementById('root')
);
