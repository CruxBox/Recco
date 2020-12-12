import React from 'react';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Signup from './components/Signup';
import Home from './components/Home';
import Movielist from './components/Movielist';
import Watchlist from './components/Watchlist';
import MoviePage from './components/MoviePage';
import {BrowserRouter as Router,Switch,Route} from 'react-router-dom'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Upcoming from './components/Upcoming';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/home" component={Home} />
          <Route path="/login" component={Signup} />
          <Route path="/upcoming" component={Upcoming} />
          <Route path="/list" component={Movielist}/>
          <Route path="/watchlist" component={Watchlist}/>
          <Route path="/movie/:movieId" component={MoviePage}/>
        </Switch>
        <ToastContainer />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
