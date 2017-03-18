"""This module executes commit examination once in a day """
import schedule
import time
import configparser
import json


from commitbot import send_commit_warning_to_member
from commitmember import CommitMember


Config = configparser.ConfigParser()
Config.read('configs.ini')
usernames = json.loads(Config.get('Username', 'usernames'))

print(usernames)

def job():
    for username in usernames:
        member = CommitMember(username)
        send_commit_warning_to_member(member)

schedule.every().day.at("23:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
