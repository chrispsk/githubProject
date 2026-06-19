from github import GitHub


if __name__ == "__main__":
    owner = "moby"
    repos = ["buildkit", "tool"]
    resources = ["issues", "commits", "pulls"]

    github_client = GitHub(owner, repos, resources)

    data = github_client.read()

    while data is not None:
        print(data)
        print("############### GOING TO NEXT PAGE ###############")
        data = github_client.read()
