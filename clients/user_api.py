from custom_requester.custom_requester import CustomRequester
from config.base_urls import AUTH_BASE_URL

USER = '/user'


class UserApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=AUTH_BASE_URL)

    def create_user(self, user_data):
        return self.send_request("POST", USER, data=user_data, expected_status=201)

    def get_user_info(self, user_id, **kwargs):
        return self.send_request("GET", f"{USER}/{user_id}", expected_status=200, **kwargs)

    def delete_user(self, user_id, **kwargs):
        return self.send_request("DELETE", f"{USER}/{user_id}", expected_status=200, **kwargs)

    def delete_users(self, *user_ids, **kwargs):
        for user_id in user_ids:
            self.delete_user(user_id, **kwargs)