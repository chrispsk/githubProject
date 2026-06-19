import os
import requests


class GitHub:
    def __init__(self, owner, repos, resources):
        self.owner = owner
        self.repos = repos
        self.resources = resources
        self.page = 1
        self.headers = self._build_headers()

    def _build_headers(self):
        token = os.environ.get("GITHUB_TOKEN")

        if token:
            return {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
            }

        return {
            "Accept": "application/vnd.github+json",
        }

    def _get(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if not data:
            return None

        return data

    def get_commit_messages(self, repo, commits):
        commit_messages = {}

        for commit in commits:
            sha = commit.get("sha")
            message = commit.get("commit", {}).get("message")

            if sha and message:
                commit_url = (
                    f"https://api.github.com/repos/"
                    f"{self.owner}/{repo}/commits/{sha}"
                )
                commit_messages[commit_url] = message

        return commit_messages

    def read(self):
        bucket = {}

        for repo in self.repos:
            resource_data = {}

            for resource in self.resources:
                url = (
                    f"https://api.github.com/repos/"
                    f"{self.owner}/{repo}/{resource}?page={self.page}"
                )

                data = self._get(url)

                if not data:
                    continue

                if resource == "commits":
                    resource_data[resource] = {
                        "url": url,
                        "data": self.get_commit_messages(repo, data),
                    }
                else:
                    resource_data[resource] = {
                        "url": url,
                        "data": data,
                    }

            if resource_data:
                bucket[repo] = resource_data

        self.page += 1

        return bucket if bucket else None
