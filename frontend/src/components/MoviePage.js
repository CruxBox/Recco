import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "./MoviePage.css";
const base_url = "https://image.tmdb.org/t/p/original";

function MoviePage() {
  let { movieId } = useParams();
  console.log(movieId);
  const [movie, setMovie] = useState({
    genres: "hello",
    meta_data: {
      genres: "hello",
      scoring: "hello",
      offers: [{ urls: { standard_web: "" } }],
    },
  });
  const [providers, setProviders] = useState([]);
  useEffect(() => {
    var id = movieId;
    function get_movie_details(id) {
      var config = {
        method: "get",
        url: `http://0.0.0.0:8000/movies/${id}/`,
        headers: {
          "Content-Type": "application/json",
        },
      };
      axios(config)
        .then(function (response) {
          console.log(response.data);
          setMovie(response.data);
          var provider = [];
          var exist = [];
          for (let offer of movie.meta_data.offers) {
            var temp = {};
            //console.log(offer)
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
                break;
              default:
                continue;
            }
            if (!exist.includes(temp.className)) {
              temp.url = offer.urls.standard_web;
              provider.push(temp);
              console.log(temp)
              exist.push(temp.className);
            }
          }
          setProviders(provider);
          console.log(provider);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    get_movie_details(id);
  }, []);

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
  const ageid = "1";
  return (
    <div>
      <div class="Moviepage">
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
                <a className="video" href="#">
                  <i className="video1" />
                  WATCH TRAILER
                </a>
                <a className="book" href="#">
                  <i className="book1" />
                  ADD TO WATCHLIST
                </a>
              </div>
              <div className="fade"></div>
            </div>
          </div>
        </div>
        <div class="part">
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
                        name
                        placeholder="Name"
                      />
                    </div>
                    <div className="col-6">
                      <input
                        type="text"
                        className="form-control"
                        name
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
                      <a href>REVIEW</a>
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
              {movie.meta_data.scoring && search("imdb:score", movie.meta_data.scoring, "provider_type")}
            </a>
            <a className="rot" href="#">
              <i className="rot1" /> :{" "}
              {movie.meta_data.scoring && search(
                "tmdb:popularity",
                movie.meta_data.scoring,
                "provider_type"
              )}
            </a>
            <a className="tmdb" href="#">
              <i className="tmdb1" /> :{" "}
              {movie.meta_data.scoring && search("tmdb:score", movie.meta_data.scoring, "provider_type")}
            </a>
              <h1>Now Streaming</h1>
            {providers.map((offer) => (
              <a
                key={offer.className}
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
