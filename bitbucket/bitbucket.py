from .worker import Worker
from bs4 import BeautifulSoup
import json

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

    def gen_file_list(self, repo_slug, params=None):
        # GENERATE FILE TREE FOR THE REPO
        worker.enum_files

    # ============================== WORKING ON THE STRUCTURE ==============================

    def gen_json_obj(self, params=None):

        pre_json_obj = {"repositories": []}

        # add all repos
        for repo in self.repo_slugs:
            pre_json_obj["repositories"].append(
                # {repo: list(x for x in self.gen_file_list(repo))}
                {repo: "test"}
            )
        return json.dumps(pre_json_obj)

    # ============================== WORKING ON THE STRUCTURE ==============================


"""

{[
    "repositories": [
        "repo1" : [
            "file1",
            "file2"
        ],
        "repo2": [
            "file1",
            "file2"
        ],
        "repo3": [
            "file1",
            "file2"
        ]
    ]
]}












"""
