import React from 'react';
import './MovieCard.scss';
function MovieCard() {
  return (
    <div className="MovieCard">
        <div className="movie_card" id="ave">
          <div className="info_section">
            <div className="movie_header">
              <img className="locandina" src="https://mr.comingsoon.it/imgdb/locandine/235x336/53715.jpg" />
              <h1>Black Panther</h1>
              <h4>2018, Ryan Coogler</h4>
              <span className="minutes">134 min</span>
              <p className="type">Action, Adventure, Sci-Fi</p>
            </div>
            <div className="movie_desc">
              <p className="text">
                T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake. 
              </p>
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
    