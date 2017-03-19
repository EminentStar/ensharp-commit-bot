"""This module executes commit examination once in a day """
import schedule
import time
import configparser
import json
import yaml


from commitbot import send_commit_warning_to_member
from commitmember import CommitMember


stream = open('configs.yml', 'r')
config = yaml.load(stream)

SCHEDULED_TIME = config.get('scheduled_time')
usernames = config.get('usernames')


def job():
    for username in usernames:
        member = CommitMember(username)
        send_commit_warning_to_member(member)

schedule.every().day.at(SCHEDULED_TIME).do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
