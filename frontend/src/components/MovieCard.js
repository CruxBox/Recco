import React from 'react';
import './MovieCard.scss';

const base_url = "https://image.tmdb.org/t/p/original";

function MovieCard( data ) {
  function truncate (str,n)
        {
                return str?.length > n ? str.substr(0,n-1) + "..." : str;
        }
  var card=data.data;
    return (
    <div className="MovieCard">
        <div className="movie_card" id="ave">
          <div className="info_section">
            <div className="movie_header">
              <img className="locandina" src={`${base_url}${card.poster_path}`} alt={card.title}/>
             <h1>{card.title}</h1>
    <h4>{card.release_date} Popularity {card.popularity}%</h4>
                <span className="minutes">{card.duration}</span>
              <p className="type">{card.genre_ids}, {card.genre},{card.genre}</p><br/>
              <p className="type">{card.original_language}</p>
            </div>
            <div className="movie_desc">
              <p className="text">
               {truncate(card?.overview,300)}</p>
            </div>
            <div className="movie_social">
              <ul>
                <li><a href="#"><i className="fa fa-share" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-heart" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-comment" style={{color:"grey"}} /></a></li>
              </ul>
            </div>
          </div>
          <div className="blur_back" style={{ backgroundImage :`url(${base_url}${card.backdrop_path})`}} />
        </div>
    </div>
     );
    }
    
export default MovieCard;
