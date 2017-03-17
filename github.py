# -*- coding: utf-8 -*-
"""This module is for calling GitHub API in order to get the last commit time."""
import requests
import json
from pprint import pprint
import datetime
import configparser


from commitmember import CommitMember


Config = configparser.ConfigParser()
Config.read('configs.ini')

OAUTH_TOKEN = Config.get('Configuration', 'OAUTH_TOKEN')

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
    headers = {'Authorization': 'token %s' % (OAUTH_TOKEN)}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
     
    repos = []
    for repo in json_data:
        repos.append(repo.get('name'))

    return repos


def check_user_commit(member):
    ret_val = False
    headers = {'Authorization': 'token %s' % (OAUTH_TOKEN)}

    repos = member.repos
    username = member.username

    for repo_name in repos:
        url = LAST_COMMIT_HASH_API_URL % (username, repo_name)
        response = requests.get(url, headers=headers)
        json_data = json.loads(response.text)
        pprint(json_data)
        
        try:
            commit_url = json_data.get('object').get('url')
        except AttributeError as error: # when no repository exists
            message = json_data.get('message')
            print(message)
            continue

        commit_time_str = get_commit_time(commit_url)
        committed = did_commit_today(commit_time_str)

        if committed:
            ret_val = True
            break

    return ret_val


def did_commit_today(commit_time_str):
    commit_time = github_date_to_localtime(commit_time_str)
    ret_val = is_today(commit_time)
    return ret_val


def get_commit_time(url):
    headers = {'Authorization': 'token %s' % (OAUTH_TOKEN)}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    commit_time = json_data.get('committer').get('date')

    return commit_time


def github_date_to_localtime(commit_date_str):
    commit_time  = datetime.datetime.strptime(commit_date_str, '%Y-%m-%dT%H:%M:%SZ')
    commit_time += datetime.timedelta(hours=9)

    return commit_time


def is_today(commit_time):
    return commit_time.date() == datetime.date.today()
