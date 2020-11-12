import React, { useState, useEffect } from "react";
import './MovieCard.scss';
import axios from "axios";

const base_url = "https://image.tmdb.org/t/p/original";

function MovieCard( data ) {
  const [movie, setMovie] = useState("")
  useEffect(() => {
    var id = data.data.id;
    function get_movie_details(id) {
      var config = {
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${id}`,
        headers: { 
          'Content-Type': 'application/json'
        },
      };
      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        setMovie(response.data);        
      })
      .catch(function (error) {
        console.log(error);
      });
    };
    get_movie_details(id);
    
  }, []);

  function truncate (str,n)
        {
                return str?.length > n ? str.substr(0,n-1) + "..." : str;
        }
        console.log(movie.genres)
    return (
    <div className="MovieCard">
        <div className="movie_card" id="ave">
          <div className="info_section">
            <div className="movie_header">
              <img className="locandina" src={`${base_url}${movie.poster_path}`} alt={movie.title}/>
             <h1><a href={movie.homepage} target="_blank">{movie.title}</a></h1>
    <h3>{movie.tagline}</h3>
    <h4>{movie.release_date}, Popularity {movie.popularity}%</h4>               
     <span className="minutes">{movie.runtime} min</span>              
              <p className="type">Language : {movie.original_language}</p><br />

            </div>
            <br />
            <br />
            <div className="movie_desc">
              <p className="text">
               {truncate(movie?.overview,300)}</p>
            </div>
            <div className="movie_social">
              <ul>
                <li><a href="#"><i className="fa fa-share" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-heart" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-comment" style={{color:"grey"}} /></a></li>
              </ul>
            </div>
          </div>
          <div className="blur_back" style={{ backgroundImage :`url(${base_url}${movie.backdrop_path} )`}} />
        </div>
    </div>
     );
    }
    
export default MovieCard;
