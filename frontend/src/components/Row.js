import React, { useState,useEffect } from "react";
import axios from "./axios";
import requests from './requests';
import { useHistory } from 'react-router-dom';
import "./Row.css";
// import Youtube from "react-youtube";
// import movieTrailer from "movie-trailer";

const base_url = "https://image.tmdb.org/t/p/original/";

function Row({title,fetchUrl,isLargeRow}){
        const [movies,setMOvies] = useState([]);
        const history = useHistory();
        useEffect(()=> {
                //[] this idicates only to run page once
                async function fetchData() {
                        const request = await axios.get(fetchUrl);
                        setMOvies(request.data.results);
                        return request;
                }
                fetchData();
        },[fetchUrl]);
        
     
        
        return (
                <div className="row">
                        <h2>{title}</h2>
                        {/*title */}

                        <div className="row_posters">
                                {/*Swveral Row Posters*/}

                                {movies.map((movie) => (
                                        <img
                                         key={movie.id}
                                         onClick={() => history.push(`/movie/${movie.id}`)} 
                                         className={`row_poster ${isLargeRow && "row_posterLarge"}`}
                                         src={`${base_url}${
                                                 isLargeRow ? movie.poster_path : movie.backdrop_path
                                                }`}
                                                 alt={movie.name}/>
                                ))}
                        </div>
                        {/* {trailerUrl && <Youtube videoId={trailerUrl} opts={opts} />} */}
                </div>
        )
}

export default Row;