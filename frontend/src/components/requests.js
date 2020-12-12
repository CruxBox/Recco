const API_KEY = "2675e893b0c550858a1036dd8ea05bfd";

const requests  = {
        fetchTrending : `/trending/all/week?api_key=${API_KEY}&language=en-US`,
        fetchTopRated : `/movie/top_rated?api_key=${API_KEY}&language=en-US&page=1`,
        fetchActionMovies : `/discover/movie?api_key=${API_KEY}&language=en-US&with_genres=28`,
        fetchComedyMovies : `/discover/movie?api_key=${API_KEY}&with_genres=35`,
        fetchHorrorMovies : `/discover/movie?api_key=${API_KEY}&with_genres=27`,
        fetchRomanceMovies : `/discover/movie?api_key=${API_KEY}&with_genres=10749`,
        fetchDocumentryMovies : `/discover/movie?api_key=${API_KEY}&with_genres=99`,
        fetchNetflixOriginals: `/discover/tv?api_key=${API_KEY}&language=en-US&sort_by=popularity.desc&page=1&timezone=America%2FNew_York`,
        fetchUpcomingMovies : `/movie/upcoming?api_key=${API_KEY}&language=en-US&page=1`,
        fetchUpcomingTv : `/tv/airing_today?api_key=${API_KEY}&language=en-US&page=1`,
}

export default requests;        