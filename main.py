from bitbucket import bitbucket
import json

from pprint import pprint


def main():
    bbucket = bitbucket.BitBucket("cbrissonts", "zLS55TY3qxnj2tNYuBb3")
    pprint(json.dumps(bbucket.gen_json_obj(), indent=2))


if __name__ == "__main__":
    main()
