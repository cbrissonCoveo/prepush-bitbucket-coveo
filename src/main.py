from bitbucket.client import Client
from pprint import pprint


def main():
    client = Client("cbrissonts", "zLS55TY3qxnj2tNYuBb3")
    print(client.enum_files("dummy_bitbucket-cb"))


if __name__ == "__main__":
    main()
