from bitbucket import bitbucket
import json

from pprint import pprint


def main():
    bbucket = bitbucket.BitBucket("cbrissonts", "zLS55TY3qxnj2tNYuBb3")
    data = json.loads(bbucket.gen_json_obj())
    pprint(data)


if __name__ == "__main__":
    main()
