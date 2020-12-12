import React from 'react';
import requests from './requests';
import Row2 from './Row2';
import Youtube from "react-youtube";
import movieTrailer from "movie-trailer";
import "./Home.css";

function Upcoming() {
  return (
    <div className="Upcoming" style={{marginTop:"60px"}}>
       
         <Row2 title="Upcoming Movies" fetchUrl={requests.fetchUpcomingMovies} isLargeRow />
         <Row2 title="Arriving Today" fetchUrl={requests.fetchUpcomingTv} isLargeRow />       
    </div>
  );
}

export default Upcoming;
