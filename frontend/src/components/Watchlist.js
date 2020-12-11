import React, { useEffect, useState } from "react";
import { UserContext } from "./Auth/userContext";
import axios from "axios";
import Card from "./card";
import { toast } from "react-toastify";
import "./Watchlist.css";
function Watchlist() {
  const { user } = React.useContext(UserContext);
  const [owned, setOwned] = useState([]);
  const [shared, setShared] = useState([]);

  useEffect(() => {
    function get_details() {
      var info = JSON.parse(localStorage.getItem("user"));
      console.log(info.user.favourite);
      var config = {
        method: "get",
        url: "http://127.0.0.1:8000/watchlists/",
        headers: {
          Authorization: `Token ${info.token}`,
          "Content-Type": "application/json",
        },
      };

      axios(config)
        .then(function (response) {
          console.log(JSON.stringify(response.data));
          let data = response.data;
          let owned = data.owned.movies;
          let shared = data.shared.movies;
          console.log(owned, data, shared);
          setOwned(data.owned);
          setShared(data.shared);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    get_details();
  }, []);

  return (
    <div className="Watchlist">
      <div class="row1">
        <h2>Owned Watchlists</h2>
        {owned.map((watch, i) => {
          return (
            <div class="row2" key={i}>
              <h3>{watch.name}</h3>
              <h5>{watch.description}</h5>
              {watch.movies.map((movie, id) => {
                return <Card key={id} id={movie.tmdb_id} />;
              })}
            </div>
          );
        })}
      </div>

      <div class="row3">
        <h2>Shared Watchlists</h2>
        {shared &&
          shared.map((watch, i) => {
            return (
              <div class="row2" key={i}>
                <h3>{watch.name}</h3>
                <h5>{watch.description}</h5>
                {watch.movies.map((movie, id) => {
                  return <Card key={id} id={movie.tmdb_id} />;
                })}
              </div>
            );
          })}
      </div>
    </div>
  );
}

export default Watchlist;
