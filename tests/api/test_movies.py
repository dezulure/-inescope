class TestMoviesPositive:
    def test_create_movie(self,api_manager,test_movie):
        create_response = api_manager.movies_api.create_movie(test_movie)
        create_data = create_response.json()
        assert create_data["name"] == test_movie["name"]
        assert create_data["description"] == test_movie["description"]
        assert create_data["location"] == test_movie["location"]


