import React, { useEffect, useState } from "react";
import { UserContext } from "./Auth/userContext";
import axios from "axios";
import { toast } from "react-toastify";
import "./Watchlist.css";
import requests from "./requests";
import { useHistory } from "react-router-dom";
import "./Row.css";
const base_url = "https://image.tmdb.org/t/p/original/";

export default function Card({ id }) {
  const [movie, setMovie] = useState("");
  const history = useHistory();
  useEffect(() => {
    function get_movie_details(id) {
      var config = {
        method: "get",
        url: `http://127.0.0.1:8000/movies/${id}/`,
        headers: {
          "Content-Type": "application/json",
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
    }
    get_movie_details(id);
  }, []);

  return (
    <div className="card" style={{"backgroundImage":`url(${base_url}${movie.poster_path})`}}   onClick={() => history.push(`/movie/${movie.id}`)}>

    </div>
  );
}
