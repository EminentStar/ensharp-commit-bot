# -*- coding: utf-8 -*-
from slacker import Slacker
import configparser


from github import get_all_repos
from github import check_user_commit


Config = configparser.ConfigParser()
Config.read('configs.ini')

TOKEN = Config.get('Configuration', 'TOKEN')
COMMIT_CHANNEL = Config.get('Configuration', 'COMMIT_CHANNEL')

slack = Slacker(TOKEN)


def send_commit_warning(username):
    attachments_dict = dict()
    attachments_dict['pretext'] = "엔샵 커밋봇 경고 알람"
    attachments_dict['title'] = "커밋하라"
    attachments_dict['title_link'] = "Do Commit!"
    attachments_dict['fallback'] = "오늘 하루가 얼마 남지 않았어!"
    attachments_dict['text'] = "%s님 커밋하세요![(프로토타입은 master branch만 체크합니다.)]" % (username)
    attachments_dict['mrkdwn_in'] = ['text', 'pretext']
    attachments = [attachments_dict]

    slack.chat.post_message(channel=COMMIT_CHANNEL, text=None, attachments=attachments, as_user=False)


def send_commit_warning_to_member(username):
    repos = get_all_repos(username)
    committed = check_user_commit(username, repos)

    if committed is False:
        print("[%s]Send Slack Warning!" % username)
        send_commit_warning(username)
