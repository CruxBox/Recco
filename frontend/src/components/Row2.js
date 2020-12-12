import React, { useState,useEffect } from "react";
import axios from "./axios";
import requests from './requests';
import { useHistory } from 'react-router-dom';
import "./Row.css";
import Youtube from "react-youtube";
import movieTrailer from "movie-trailer";

const base_url = "https://image.tmdb.org/t/p/original/";

function Row2({title,fetchUrl,isLargeRow}){
        const [movies,setMOvies] = useState([]);
        const [trailerUrl,setTrailerUrl] = useState("");
        //A snippet of code which runs based on our condition//
        useEffect(()=> {
                //[] this idicates only to run page once
                async function fetchData() {
                        const request = await axios.get(fetchUrl);
                        setMOvies(request.data.results);
                        return request;
                }
                fetchData();
        },[fetchUrl]);
        
        console.table(movies);
        const opts = {
                height: "590",
                width: "1300",
                playerVars: {
                        autoplay: 1,
                },
        };
        
        const handleClick = (movie) => {
                if(trailerUrl){
                        setTrailerUrl("");
                }
                else
                {
                        movieTrailer(movie?.name || "")
                        .then((url) => {
                                const urlParams = new URLSearchParams(new URL(url).search);
                                setTrailerUrl(urlParams.get("v"));
                        })
                        .catch((error) => console.log(error))
                }
        }
        
        return (
                <div className="row">
                        <h2>{title}</h2>
                        {/*title */}

                        <div className="row_posters">

                                {movies.map((movie) => (
                                        <img
                                         key={movie.id}
                                         onClick={() => handleClick(movie)}
                                         className={`row_poster ${isLargeRow && "row_posterLarge"}`}
                                         src={`${base_url}${
                                                 isLargeRow ? movie.poster_path : movie.backdrop_path
                                                }`}
                                                 alt={movie.name}/>
                                ))}
                        </div>
                        {trailerUrl && <Youtube videoId={trailerUrl} opts={opts} />}
                </div>
        )
}

export default Row2;