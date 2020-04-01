# githubProject
small library that can ingest unlimited amounts of data from GitHub
Description
You will build an class that streams batches of data from GitHub out to the caller (the user of your object).

The class will operate as a stream, or an iterable - such that every call to get more data, produces only a portion of that data (as the actual data can be arbitrarily large).

The class will enable it’s user to get multiple types of data on multiple repositories owned by the same owner/organization using a single API

Requirements:
Implement a single class, called GitHub

The class constructor is initiated using three variables
The basic input parameters will be
owner - A string representing the Owner name
repo - A list of strings representing Repository names
resources - A list of desired resource names

Please include ‘commits’ in the supported resources and pick at least 2 more (‘issues’, ‘commits’, ‘users’, etc.) - this will be your “Supported Resources” list and this will define what values may be passed in the resources argument.

* Note, that the endpoint “{repository_name}/commits” does not return all the metadata of the commit,
  So you first need to get all the commits ids and then for each commit fetch “{repository_name}/commits/{sha}”


The class must implement at least one function called read() that takes no arguments.

Each call to read will return a portion of data: a list of data points returned from the API (e.g a list of dictionaries)
The class must iterate of every repository and resource combination as the user calls read() multiple times.

The resources in the input must be a subset of the support resources, meaning you might support N different resources inside the class, but the caller may only be interested in M resources, so M is a subset of N. (you do not need to validate input, this is simply to illustrate that the user might request less resources than the class supports)

For each resource make sure you iterate on all the pages of the result (it can be more than a single request) - but don’t read all pages in a single call to read, instead, every call should fetch the next page until the resource is depleted, then move on to the next resource and/or next repository.

When there is no more data to return, return None

Example
If the input is:
owner=”moby”
repositories=[‘moby’,’buildkit, ‘tool’]
resources=[‘issues’, ‘commits’, ‘pull_requests’]

As we call read repeatedly, it will return all the issues, commits & pull requests for the repositories at moby/moby, moby/buildkit, moby/tool (no particular order, see notes)

Usage
Your class will be used in a manner similar to the sample below:

gh = GitHub(arguments)

data = gh.read()
while data is not None:
    # do something with the data
    data = gh.read() # fetch next batch

Notes
Order of iteration is not important for this assignment.
No need to perform input validation (you can if you want to, but it’s not a requirement for the task)
Don’t use any existing github library/SDK, make direct calls to the API
We only care for reading data from github, not writing to it.

What Are We Looking For?
We are trying to estimate your optimal code quality and have a peek at your thought process. All this without time limitations, or (too many) restrictive conditions, so please follow best practices. Consider conventions, comments, documentation, and tests. We wish this to be built by the same quality standards you'd like to see in your production code, so consider Network issues, Error handling and recovery when possible, Consider the API rate limit, etc. 
