from .worker import Worker
from bs4 import BeautifulSoup

from bitbucket.exceptions import (
    UnknownError,
    InvalidIDError,
    NotFoundIDError,
    NotAuthenticatedError,
    PermissionError,
)


class BitBucket:
    def __init__(self, user, password, owner=None):
        worker = Worker(user, password, owner=None)
        self.repo_slugs = worker.get_repos_slugs()
        # self.repo_files = [
        #     self.gen_file_list(repo_slug) for repo_slug in self.repo_slugs
        # ]

    def gen_file_list(self, repo_slug, params=None):
        # GENERATE FILE TREE FOR THE REPO
        return None

    # ============================== WORKING ON THE STRUCTURE ==============================

    def gen_json_obj(self, params=None):

        json_obj = {
            "repositories": {},
        }

    # ============================== WORKING ON THE STRUCTURE ==============================
