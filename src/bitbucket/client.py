import requests
from bs4 import BeautifulSoup

from bitbucket.exceptions import (
    UnknownError,
    InvalidIDError,
    NotFoundIDError,
    NotAuthenticatedError,
    PermissionError,
)


class Client(object):
    BASE_URL = "https://api.bitbucket.org/"

    def __init__(self, user, password, owner=None):
        self.user = user
        self.password = password
        user_data = self.get_user()

        if owner is None:
            owner = user_data.get("username")
        self.username = owner

    def get_user(self, params=None):

        return self._get("2.0/user", params=params)

    def get_repos_slugs(self, params=None):

        """Returns a list of slugs for each repo"""
        # raw_repos_data contains the raw value of each repos in a list format
        raw_repos_data = self._get(f"2.0/repositories/{self.username}", params=params)[
            "values"
        ]
        return list(x["slug"] for x in raw_repos_data)

    def enum_files(self, repo_slug, params=None):
        '''Returns a dict of filename: href to fetch the content of the script'''
        raw_data = self._get(f"2.0/repositories/{self.username}/{repo_slug}/src")

        # I'm hurt
        file_list = list(x["path"] for x in raw_data["values"])
        raw_href_list = list(x["links"]["self"]["href"] for x in raw_data["values"])
        
        return dict(zip(file_list, raw_href_list))

    def get_code_body(self, repo_slug, params=None):
        # ==================================================================
        # WE'RE HERE NOW
        # ==================================================================

    def _get(self, endpoint, params=None):
        response = requests.get(
            self.BASE_URL + endpoint, params=params, auth=(self.user, self.password)
        )
        return self._parse(response)

    def _parse(self, response):
        status_code = response.status_code
        if "application/json" in response.headers["Content-Type"]:
            r = response.json()
        else:
            r = response.text
        if status_code in (200, 201):
            return r
        if status_code == 204:
            return None
        message = None
        try:
            if "errorMessages" in r:
                message = r["errorMessages"]
        except Exception:
            message = "No error message."
        if status_code == 400:
            raise InvalidIDError(message)
        if status_code == 401:
            raise NotAuthenticatedError(message)
        if status_code == 403:
            raise PermissionError(message)
        if status_code == 404:
            raise NotFoundIDError(message)
        raise UnknownError(message)
