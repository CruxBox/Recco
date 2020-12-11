import React from 'react';
import './MoviePage.css';


function MoviePage() {

  function truncate (str,n)
  {
          return str?.length > n ? str.substr(0,n-1) + "..." : str;
  }

const ageid = '1';
var moviedescription="The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.";
const streaming = '1';

  return (
    <div class="Moviepage">
      <div className="full">
        <div className="main">
          <div className="header1">
            <div className="header-info">
              <h1>MARAKATHAMANI</h1>

               {(() => {
                switch (ageid) {
                case '1':
                  return (<p className="age"><a href="#">All Age</a> Hero, Heroin ,actor 3</p> )
                case '2':
                  return (<p class="age1"><a href="#">18 + </a> Hero, Heroin ,actor 3</p>)
                default:
                      return ( <p className="age"><a href="#">All Age</a> Hero, Heroin ,actor 3</p>) }})()}

              <p className="review">Runtime	&nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;  143 min</p>
              <p className="review reviewgo">Genre	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp; Drama, Action, Comedy</p>
              <p className="review">Release &nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;&nbsp; 7 November 2014</p>
              <p className="special">{truncate(moviedescription,170)}</p>
              <a className="video" href="#"><i className="video1" />WATCH TRAILER</a>
              <a className="book" href="#"><i className="book1" />ADD TO WATCHLIST</a>
            </div>
            <div className="fade">
            </div>
          </div>
        </div>
      </div>
      <div class="part">
      <section className="contact-us" id="contact">
        <div className="container">
          <div className="row">
          </div>
          <div className="row">
            <div className="contact-form">
              <div className="row">
                <div className="text">
                  <h2>Review This Movie</h2>
                  <p>You can give your personal rating and review here</p>
                </div>
              </div>
              <div className="row space-between">
                <div className="col-6">
                  <input type="text" className="form-control" name placeholder="Name" />
                </div>
                <div className="col-6">
                  <input type="text" className="form-control" name placeholder="Your Rating" />
                </div>
              </div>
              <div className="row">
                <div className="col-12">
                  <textarea className="form-control" placeholder="Your Comment" defaultValue={""} />
                </div>
              </div>
              <div className="row">
                <div className="button text-right">
                  <a href>REVIEW</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <div className="stream">
        <h1>Ratings</h1>
        <a className="imdb" href="#"><i className="imdb1" /> : 9.8 </a>
        <a className="rot" href="#"><i className="rot1" /> : 0.8 </a>
        <a className="tmdb" href="#"><i className="tmdb1" /> : 1.8 </a>
        <h1>Now Streaming</h1>

        {(() => {
                switch (ageid) {
                case '1':
                  return ( <i className="netflix" /> )
                case '2':
                  return ( <i className="hotstar" /> )
                case '3':
                  return ( <i className="prime" /> )    
                case '4':
                  return ( <i className="google" /> )  
                case '5':
                  return ( <i className="itunes" /> ) 
                case '6':
                  return ( <i className="zee5" /> )                                       
                default:
                      return (  <i className="netflix" />) }})()}
      
        <h1>Cast</h1>
        <ul>
          <li><a>Maurice</a></li>
          <li><a>Verdine</a></li>
          <li><a>Don</a></li>
          <li><a>Philip</a></li>
          <li><a>Roland</a></li>
          <li><a>Jessica</a></li>
          <li><a>Larry</a></li>
          <li><a>Ralph</a></li>
        </ul>
      </div>
      </div>
    </div>
 );
}

export default MoviePage;
