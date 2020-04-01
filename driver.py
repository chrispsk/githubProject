from github import GitHub


if __name__ == "__main__":

    owner = "moby"
    repo = ["buildkit", "tool"]
    resources = ["issues", "commits", "pulls"]
    gh = GitHub(owner, repo, resources)

    data = gh.read()

    while data is not None:
        print(data)
        # here do something with data (save in db)
        print("############## GOING TO NEXT PAGE ################")
        data = gh.read() 
