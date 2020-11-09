from typing import List

import tmdbsimple as tmdb

tmdb.API_KEY = '6d343765c641930b74aae2d4a89c22f8'

class TmdbApiManager:
    """
    The Movie Database API (https://developers.themoviedb.org/)
    """

    @staticmethod
    def search_tv_shows(**kwargs) -> List:
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
    def search_movies(**kwargs) -> List:
        """
        Searches movies by specified search string and returns matches.
            Specify query in URL,
            assigns ' ' by default which returns no results
            --> `/search/hello` will return all results having "hello"
            Allows specifying max results to return,
            returns all matching results by default
            --> `/search/hello/20` will return first 20 results
        Optional Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.
            include_adult: (optional) Choose whether to inlcude adult
                (pornography) content in the results.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.
            year: (optional) A filter to limit the results to a specific year
                (looking at all release dates).
            primary_release_year: (optional) A filter to limit the results to a
                specific primary release year.
        """
        search = tmdb.Search()
        results = []
        max_results = kwargs['max_results']
        movie_response = search.movie(query=kwargs['query'],
                                    language = kwargs['language'],
                                    include_adult = kwargs['include_adult'],
                                    region = kwargs['region'],
                                    year = kwargs['year'],
                                    primary_release_year = kwargs['primary_release_year'])

        for page in range(1, movie_response['total_pages']+1):
            results.extend(
                search.movie(query=kwargs['query'],
                            language = kwargs['language'],
                            include_adult = kwargs['include_adult'],
                            region = kwargs['region'],
                            year = kwargs['year'],
                            primary_release_year = kwargs['primary_release_year'],
                            page=kwargs['page'])['results']
                )
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_popular_movies(**kwargs) -> List:
        """
        Returns popular movies.
            Allows specifying max results to return,
            returns 1000 by default as the TMDb API does
            --> `/popular/20` will return top 20
        Optional Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.
        """

        movies = tmdb.Movies()
        results = []
        max_results = kwargs['max_results']
        response = movies.popular(language = kwargs['language'],
                                region = kwargs['region'])
        for page in range(1, response['total_pages']+1):
            results.extend(
                movies.popular(language = kwargs['language'],
                                region = kwargs['region'],
                                page=page)['results']
                )
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_latest_movies() -> List:
        """
        Args:
            language: (optional) ISO 639-1 code.
        Returns latest movies.
        """

        movies = tmdb.Movies()
        result = [movies.latest(language = kwargs['language'])]

        return result

    @staticmethod
    def get_top_rated(max_results: int=None) -> List:
        """
        Optional Args:
        language: (optional) ISO 639-1 code.
        page: (optional) Minimum 1, maximum 1000, default 1.
        region: (optional) Specify a ISO 3166-1 code to filter release
            dates. Must be uppercase.
        Returns top-rated movies.
            Allows specifying max results to return,
            returns all matching results by default
            --> `/top-rated/20` will return first 20
        """
        max_results = kwargs['max_results']
        movies = tmdb.Movies()
        results = []
        max_results = kwargs['max_results']
        response = movies.top_rated(language = kwargs['language'],
                                region = kwargs['region'])
        for page in range(1, response['total_pages']+1):
            results.extend(movies.top_rated(language = kwargs['language'],
                                region = kwargs['region'], page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results

    @staticmethod
    def get_upcoming(max_results: int=None) -> List:
        """
        Args:
        language: (optional) ISO 639-1 code.
        page: (optional) Minimum 1, maximum 1000, default 1.
        region: (optional) Specify a ISO 3166-1 code to filter release
            dates. Must be uppercase.
        Returns upcoming movies.
            Allows specifying max results to return,
            returns all matching results by default
            --> `/upcoming/20` will return first 20
        """

        movies = tmdb.Movies()
        results = []
        max_results = kwargs['max_results']
        response = movies.upcoming(language = kwargs['language'],
                                region = kwargs['region'])
        for page in range(1, response['total_pages']+1):
            results.extend(movies.upcoming(language = kwargs['language'],
                                region = kwargs['region'], page=page)['results'])
            if max_results and len(results) > max_results:
                results = results[:max_results]
                break

        return results


class IncomingApiManager(TmdbApiManager):
    pass