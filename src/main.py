from bitbucket.client import BitBucket
from pprint import pprint


def main():
    client = BitBucket("cbrissonts", "zLS55TY3qxnj2tNYuBb3")
    """ data = client.get_code_body("dummy_bitbucket-cb")
    for x in data:
        print(x, ": ", data[x]) """


if __name__ == "__main__":
    main()
