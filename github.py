import requests
################# ADD TOKEN ###########################
token = '' # here add your token
header = dict()
if token:
    header['Authorization'] = 'Token {}'.format(token)
#########################################################


class GitHub:

    def __init__(self, owner, repo, resources):
        self.__owner = owner
        self.__repo = repo
        self.__resources = resources
        self.counter = 1

    @property
    def owner(self):
        return self.__owner

    @property
    def repo(self):
        return self.__repo

    @property
    def resources(self):
        return self.__resources

    def sha_commit(self, jso):
        abc = list() # save all sha for this page
        for x in jso:
            abc.append(x['sha'])
        return abc

    def get_sha_commits(self, repos, response):
        abc = list() # save all sha for this page
        for x in response.json():
            abc.append(x['sha'])
        
        evr = dict()
        for i,val in enumerate(abc):
                sha_url = 'https://api.github.com/repos/{user}/{repo}/commits/{sha}'.format(
                    user=self.owner,
                    repo=repos,
                    sha=val
                )
                comi_sha = requests.get(sha_url, headers=header)
                if comi_sha.status_code == 200 and comi_sha.json():
                    #evr[sha_url] = response.json()[i]['sha']
                    evr[sha_url] = response.json()[i]['commit']['message']
        return evr
            

    def read(self):
        bucket = dict()
        for repos in self.repo:
            resource_dict = dict()
            for res in self.resources:
                url = 'https://api.github.com/repos/{user}/{repo}/{resource}?page={page}'.format(
                        user=self.owner,
                        repo=repos,
                        resource=res,
                        page=self.counter
                    )
                response = requests.get(url, headers=header)
                if response.status_code==200 and response.json():
                    if res == "commits": # special case for commits
                        evr = self.get_sha_commits(repos,response)
                        
                        resource_dict["commits"] = {
                                'url': url,
                                'data': evr
                            }
                    else:
                        resource_dict[res] = {
                                'url': url,
                                'data': response.json()
                            }
            if resource_dict: # add to bucket only if hasmore data
                bucket[repos] = resource_dict
        
        self.counter += 1 # next page

        if bucket: # return the bucket if has any data or None
            return bucket
        else:
            return None 

