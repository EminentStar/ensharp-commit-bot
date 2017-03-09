"""This module is for calling GitHub API in order to get the last commit time."""
import requests
import json
from pprint import pprint



ALL_REPOS_API_URL = 'https://api.github.com/users/%s/repos'
LAST_COMMIT_HASH_API_URL = 'https://api.github.com/repos/%s/%s/git/refs/heads/master'
LAST_COMMIT_TIME_URL = 'https://api.github.com/repos/%s/%s/git/commits/%s'

"""
    0. Commit Group 유저리스트 체크

    1. 한 유저의 전체 repo 목록 저장: https://api.github.com/users/:user/repos

    2. 한 유저의 특정 리포의 마지막 커밋 hash값 확인:
    https://api.github.com/repos/:user/:repo/git/refs/heads/master

    3. 한 유저의 특정 리포의 마지막 커밋의 시간 확인:
    https://api.github.com/repos/:user/:repo/git/commits/:hashvalue
"""


def get_all_repos(username):
    url = ALL_REPOS_API_URL % (username)
    response = requests.get(url)
    json_data = json.loads(response.text)
     
    repos = []
    pprint(json_data)
    for repo in json_data:
        repos.append(repo.get('name'))

    return repos


def did_user_commit(username, repos):
    for repo_name in repos:
        url = LAST_COMMIT_HASH_API_URL % ('eminentstar', repo_name)
        response = requests.get(url)
        json_data = json.loads(response.text)

        commit_url = json_data.get('object').get('url')
        commit_time = get_commit_time(commit_url)
        pprint(commit_time)



def get_commit_time(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    commit_time = json_data.get('committer').get('date')

    return commit_time



"""example test"""
repos = get_all_repos('eminentstar')
did_user_commit('eminentstar', repos)

