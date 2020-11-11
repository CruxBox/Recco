import React from 'react';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Signup from './components/Signup';
import Home from './components/Home';
import MovieCard from './components/MovieCard';
import {BrowserRouter as Router,Switch,Route} from 'react-router-dom'
function App() {
  return (
    <Router>
      <div className="App">
          <Navbar/>
          <switch>
          <Route path="/" exact component={Home} />
          <Route path="/home" component={Home} />
          <Route path="/login" component={Signup} />
          </switch>
          <Footer/>
      </div>
    </Router>
  );
}

export default App;
