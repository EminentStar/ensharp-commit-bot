import schedule
import time
import configparser
import json


Config = configparser.ConfigParser()
Config.read('configs.ini')
usernames = json.loads(Config.get('Username', 'usernames'))

print(usernames)

def job():
    for username in usernames:
        send_commit_warning_to_member(username)


schedule.every().day.at("23:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
