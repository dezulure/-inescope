from custom_requester.custom_requester import CustomRequester
from config.base_urls import MOVIES_BASE_URL

MOVIES = '/movies'


class MoviesApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=MOVIES_BASE_URL)

    def create_movie(self, movie_data, expected_status=201):
        return self.send_request(
            method="POST",
            endpoint=MOVIES,
            data=movie_data,
            expected_status=expected_status,
        )

    def get_movies(self, expected_status=200):
        return self.send_request(
            method="GET",
            endpoint=MOVIES,
            expected_status=expected_status
        )

    def get_current_movie(self, film_id, expected_status=200):
        return self.send_request(
            method="GET",
            endpoint=f"{MoviesApi}/{film_id}",
            expected_status=expected_status
        )

    def delete_movie(self, film_id, expected_status=200):
        return self.send_request(
            method="DELETE",
            endpoint=f"{MoviesApi}/{film_id}",
            expected_status=expected_status
        )

    def update_movie(self, film_id, movie_data, expected_status=200):
        return self.send_request(
            method="PATCH",
            endpoint=f"{MoviesApi}/{film_id}",
            data=movie_data,
            expected_status=expected_status
        )
