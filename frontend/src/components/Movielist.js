import React, { useState,useEffect } from "react";
import MovieCard from "./MovieCard"

const Movielist = ({ history }) => {
    const [movies, setMovies] = useState([]);
    useEffect(()=> {
        //[] this idicates only to run page once
        setMovies(history.location.state.data);
},[movies]);
    return (
        <div>
            {movies.map((movie) => (
                                        <MovieCard
                                         key={movie.id}
                                        data =  {movie}
                                         />
                                ))}
        </div>
    )
}

export default Movielist;
