import React from 'react';
import requests from './requests';
import Row from './Row';

import "./Home.css";

function Upcoming() {
  return (
    <div className="Upcoming" style={{marginTop:"60px"}}>
       
         <Row title="Upcoming Movies" fetchUrl={requests.fetchUpcomingMovies} isLargeRow />
         <Row title="Arriving Today" fetchUrl={requests.fetchUpcomingTv} isLargeRow />       
    </div>
  );
}

export default Upcoming;
