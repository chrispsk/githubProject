# githubProject

Small Python project for ingesting large amounts of paginated data from the GitHub API.

The script reads repository resources such as issues, commits, and pull requests from one or more GitHub repositories. It keeps requesting the next API page until no more data is returned.

## Features

- Ingests paginated GitHub API data
- Supports large datasets across multiple pages
- Supports multiple repositories
- Supports issues, commits, and pull requests
- Extracts commit messages
- Optional GitHub token support
- Simple loop-based data streaming

## Requirements

- Python 3.x
- requests

## Setup

Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Usage

Run the script:

python driver.py

By default, the script reads data from:

owner = "moby"
repos = ["buildkit", "tool"]
resources = ["issues", "commits", "pulls"]

The read() method returns one page of data at a time.
When there is no more data to read, it returns None.

Example flow:

data = github_client.read()

while data is not None:
    print(data)
    data = github_client.read()

## GitHub Token

A GitHub token is optional, but recommended for higher API rate limits.

Windows CMD:

set GITHUB_TOKEN=your_token_here
python driver.py

PowerShell:

$env:GITHUB_TOKEN="your_token_here"
python driver.py

## Notes

This project is a simple example of API pagination and data ingestion.

It is useful for learning how to:

- Connect to an external REST API
- Read paginated API responses
- Process data page by page
- Work with multiple repositories and resources
- Prepare API data for storage or further processing

## License

This project is open source.
