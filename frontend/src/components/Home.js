import React from 'react';
import Banner from './Banner';
import requests from './requests';
import Row from './Row';

import "./Home.css";

function Home() {
  return (
    <div className="Home">
         <Banner />
         <Row title="OTT Originals" fetchUrl={requests.fetchNetflixOriginals} isLargeRow />
         <Row title="Trending Now" fetchUrl={requests.fetchTrending} />
         <Row title="Top Rated" fetchUrl={requests.fetchTopRated} />
         <Row title="Action Movies" fetchUrl={requests.fetchActionMovies} />
         <Row title="Comedy Movies" fetchUrl={requests.fetchComedyMovies} />
         <Row title="Horror Movies" fetchUrl={requests.fetchHorrorMovies} />
         <Row title="Romance Movies" fetchUrl={requests.fetchRomanceMovies} />
       
    </div>
  );
}

export default Home;
