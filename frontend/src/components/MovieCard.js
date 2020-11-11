import React from 'react';
import './MovieCard.scss';
function MovieCard(card) {
  return (
    <div className="MovieCard">
        <div className="movie_card" id="ave">
          <div className="info_section">
            <div className="movie_header">
              <img className="locandina" src={card.image} />
             <h1>{card.title}</h1>
                <h4>{card.year}, {card.directoe}</h4>
                <span className="minutes">{card.duration}</span>
              <p className="type">{card.genre}, {card.genre},{card.genre}</p>
            </div>
            <div className="movie_desc">
              <p className="text">
               {card.description}</p>
            </div>
            <div className="movie_social">
              <ul>
                <li><a href="#"><i className="fa fa-share" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-heart" style={{color:"grey"}} /></a></li>
                <li><a href="#"><i className="fa fa-comment" style={{color:"grey"}} /></a></li>
              </ul>
            </div>
          </div>
          <div className="blur_back ave_back" />
        </div>

    </div>
     );
    }
    
export default MovieCard;
    