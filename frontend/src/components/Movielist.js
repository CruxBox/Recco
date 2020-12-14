import React, { useState, useEffect } from "react";
import MovieCard from "./MovieCard";

const Movielist = ({ history }) => {
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    //[] this indicates only to run page once
    setMovies(history.location.state.data);
  }, [history.location.state.name]);
  return (
    <div>
      {movies.map((movie) => (
        <MovieCard key={movie?.id || movie?.tmdb_id } data={movie} />
      ))}
    </div>
  );
};

export default Movielist;
