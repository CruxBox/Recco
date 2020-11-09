from typing import List

import tmdbsimple as tmdb

tmdb.API_KEY = '6d343765c641930b74aae2d4a89c22f8'


class IncomingApiManager:
    """
    The Movie Database API (https://developers.themoviedb.org/)
    """

    @staticmethod
    def search_tv_shows(query: str=' ', max_results: int=None) -> List:
        """
        Searches tv shows by specified search string and returns matches.
            Specify query in URL,
            assigns ' ' by default which returns no results
            --> `/search/hello` will return all results having "hello"
            Allows specifying max results to return,
            returns all matching results by default
            --> `/search/hello/20` will return first 20 results
        """

        search = tmdb.Search()
        results = []

        tv_response = search.tv(query=query)
        for page in range(1, tv_response['total_pages']+1):
            results.extend(search.tv(query=query, page=page)['results'])
            if max_results and len(results) > max_results:
                    results = results[:max_results]
                    break

        return results

    @staticmethod
    def search_movies(query: str=' ', max_results: int=None) -> List:
        """
        Searches movies by specified search string and returns matches.
            Specify query in URL,
            assigns ' ' by default which returns no results
            --> `/search/hello` will return all results having "hello"
            Allows specifying max results to return,
            returns all matching results by default
            --> `/search/hello/20` will return first 20 results
        """
        search = tmdb.Search()
        results = []

        movie_response = search.movie(query=query)
        for page in range(1, movie_response['total_pages']+1):
            results.extend(search.movie(query=query, page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_popular_movies(max_results: int=None) -> List:
        """
        Returns popular movies.
            Allows specifying max results to return,
            returns 1000 by default as the TMDb API does
            --> `/popular/20` will return top 20
        """

        movies = tmdb.Movies()
        results = []

        response = movies.popular()
        for page in range(1, response['total_pages']+1):
            results.extend(movies.popular(page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_latest_movies() -> List:
        """
        Returns latest movies.
        """

        movies = tmdb.Movies()
        result = [movies.latest()]

        return result

    @staticmethod
    def get_top_rated(max_results: int=None) -> List:
        """
        Returns top-rated movies.
            Allows specifying max results to return,
            returns all matching results by default
            --> `/top-rated/20` will return first 20
        """

        movies = tmdb.Movies()
        results = []

        response = movies.top_rated()
        for page in range(1, response['total_pages']+1):
            results.extend(movies.top_rated(page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_upcoming(max_results: int=None) -> List:
        """
        Returns upcoming movies.
            Allows specifying max results to return,
            returns all matching results by default
            --> `/upcoming/20` will return first 20
        """

        movies = tmdb.Movies()
        results = []

        response = movies.upcoming()
        for page in range(1, response['total_pages']+1):
            results.extend(movies.upcoming(page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results