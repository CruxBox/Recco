import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { UserContext } from './Auth/userContext';
import axios from "axios";
import { toast } from 'react-toastify';
import "./MoviePage.css";
const base_url = "https://image.tmdb.org/t/p/original";

function MoviePage() {
  const { user } = React.useContext(UserContext);
  // const [isLoaded, setIsLoaded] = useState(false);
  let { movieId } = useParams();
  const [movie, setMovie] = useState({
    genres: " ",
    meta_data: {
      genres: ["", ""],
      scoring: "",
      offers: [{ urls: { standard_web: "" } }],
    },
  });
  const [providers, setProviders] = useState([]);
  useEffect(() => {
    var id = movieId;
    async function get_movie_details(id) {
      var config = {
        method: "get",
        url: `http://127.0.0.1:8000/movies/${id}/`,
        headers: {
          "Content-Type": "application/json",
        },
      };
      axios(config)
        .then(function (response) {
          console.log(response.data);
          var provider = [];
          var exist = [];
          for (let offer of response.data.meta_data.offers) {
            var temp = {};
            switch (offer.provider_id) {
              case 8:
                temp.className = "netflix";
                break;
              case 122:
                temp.className = "hotstar";
                break;
              case 119:
                temp.className = "prime";
                break;
              case 3:
                temp.className = "google";
                break;
              case 2:
                temp.className = "itunes";
                break;
              case 232:
                temp.className = "zee5";
              case 192:
                response.data.youtube = offer.urls.standard_web;
                break;
              default:
                continue;
            }
            if (!exist.includes(temp.className)) {
              temp.id = offer.provider_id;
              temp.url = offer.urls.standard_web;
              provider.push(temp);
              console.log(temp);
              exist.push(temp.className);
            }
          }
          setProviders(provider);
          setMovie(response.data);
          //setIsLoaded(true)
          //console.log(provider);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    get_movie_details(id);
  }, [movieId]);

  function truncate(str, n) {
    return str?.length > n ? str.substr(0, n - 1) + "..." : str;
  }
  function search(nameKey, myArray, key) {
    for (var i = 0; i < myArray.length; i++) {
      if (myArray[i][key] === nameKey) {
        return myArray[i].value;
      }
    }
  }

 function add_to_fav(e){
   e.preventDefault()
   var info=JSON.parse(localStorage.getItem("user"))
   console.log(info.user.favourite)
   console.log(":hellooo")
   var data={}
   data.movies=[{tmdb_id:movie.id}]
   var config = {
    method: 'post',
    url: `http://127.0.0.1:8000/watchlists/${info.user.favourite}/add`,
    headers: { 
      'Authorization': `Token ${info.token}`, 
      'Content-Type': 'application/json'
    },
    data : data
  };
  axios(config)
  .then(function (response) {
    console.log(JSON.stringify(response.data));
    toast.success('Added to favourites', {
      position: "bottom-right",
      autoClose: 2000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      });
  })
  .catch(function (error) {
    console.log(error);
  });
 }
 function add_to_seen(e){
  e.preventDefault()
  var info=JSON.parse(localStorage.getItem("user"))
  console.log(info.user.favourite)
  console.log(":hellooo")
  var data={}
  data.movies=[{tmdb_id:movie.id}]
  var config = {
   method: 'post',
   url: `http://127.0.0.1:8000/watchlists/${info.user.seen}/add`,
   headers: { 
     'Authorization': `Token ${info.token}`, 
     'Content-Type': 'application/json'
   },
   data : data
 };
 axios(config)
 .then(function (response) {
   console.log(JSON.stringify(response.data));
   toast.success('Added to seen list', {
     position: "bottom-right",
     autoClose: 2000,
     hideProgressBar: false,
     closeOnClick: true,
     pauseOnHover: true,
     draggable: true,
     progress: undefined,
     });
 })
 .catch(function (error) {
   console.log(error);
 });
}

  return (
    <div>
      <div className="Moviepage">
        <div className="full">
          <div className="main">
            <div
              className="header1"
              style={{
                backgroundImage: `url(${base_url}${movie.backdrop_path} )`,
              }}
            >
              <div className="header-info">
                <h1>
                  <a href={movie.homepage} target="_blank" />
                  {movie.title}
                </h1>
                <h3>{movie.tagline}</h3>
                <p className="review">
                  Runtime &nbsp;&nbsp;&nbsp;: &nbsp;&nbsp; {movie.runtime} min
                </p>
                <p className="review reviewgo">
                  Genre &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp;{" "}
                  {movie?.genres[0].name} {movie?.genres[1]?.name}{" "}
                  {movie?.genres[3]?.name} {movie?.genres[4]?.name}
                </p>
                <p className="review">
                  Release &nbsp;&nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;{" "}
                  {movie.release_date}
                </p>
                <p className="special">{truncate(movie?.overview, 400)}</p>
                <a className="video" href={movie?.youtube}>
                  <i className="video1" />
                  WATCH TRAILER
                </a>
                <a className="book" onClick={add_to_fav}>
                  <i className="book1" />
                  ADD TO WATCHLIST
                </a>
                <a className="book" onClick={add_to_seen}>
                  <i className="book2" />
                  ADD TO SEENLIST
                </a>
              </div>
              <div className="fade"></div>
            </div>
          </div>
        </div>
        <div className="part">
          <section className="contact-us" id="contact">
            <div className="container">
              <div className="row"></div>
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
                      <input
                        type="text"
                        className="form-control"
                        name=""
                        placeholder="Name"
                      />
                    </div>
                    <div className="col-6">
                      <input
                        type="text"
                        className="form-control"
                        name=""
                        placeholder="Your Rating"
                      />
                    </div>
                  </div>
                  <div className="row">
                    <div className="col-12">
                      <textarea
                        className="form-control"
                        placeholder="Your Comment"
                        defaultValue={""}
                      />
                    </div>
                  </div>
                  <div className="row">
                    <div className="button text-right">
                      <a>REVIEW</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <div className="stream">
            <h1>Ratings</h1>
            <a className="imdb" href="#">
              <i className="imdb1" /> :{" "}
              {movie.meta_data.scoring &&
                search("imdb:score", movie.meta_data.scoring, "provider_type")}
            </a>
            <a className="rot" href="#">
              <i className="rot1" /> :{" "}
              {movie.meta_data.scoring &&
                search(
                  "tmdb:popularity",
                  movie.meta_data.scoring,
                  "provider_type"
                )}
            </a>
            <a className="tmdb" href="#">
              <i className="tmdb1" /> :{" "}
              {movie.meta_data.scoring &&
                search("tmdb:score", movie.meta_data.scoring, "provider_type")}
            </a>
            <h1>Now Streaming</h1>
            {providers.map((offer,i) => (
              <a
                key={i}
                className={offer.className}
                href={offer.url}
                target="_blank"
              />
            ))}
            <h1>Cast</h1>
            <ul>
              <li>
                <a>Maurice</a>
              </li>
              <li>
                <a>Verdine</a>
              </li>
              <li>
                <a>Don</a>
              </li>
              <li>
                <a>Philip</a>
              </li>
              <li>
                <a>Roland</a>
              </li>
              <li>
                <a>Jessica</a>
              </li>
              <li>
                <a>Larry</a>
              </li>
              <li>
                <a>Ralph</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MoviePage;
