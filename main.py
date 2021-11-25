from bitbucket import bitbucket

# from pprint import pprint


def main():
    bbucket = bitbucket.BitBucket("cbrissonts", "zLS55TY3qxnj2tNYuBb3")
    print(bbucket.repo_slugs)


if __name__ == "__main__":
    main()
