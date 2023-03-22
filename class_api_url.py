import requests


class ApiUrl:

    def __init__(self, api_url, headers=None, params=None):
        self._api_url = api_url
        self._headers = headers
        self._params = params

    def get_response(self):
        response = requests.get(self._api_url, headers=self._headers, params=self._params)
        return response

