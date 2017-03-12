from slacker import Slacker


from configs import TOKEN
from configs import COMMIT_CHANNEL


slack = Slacker(TOKEN)

# slack.chat.post_message('#1commit', 'Commit Bot Test')


def send_commit_warning(username):
    attachments_dict = dict()
    attachments_dict['pretext'] = "엔샵 커밋봇 경고 알람"
    attachments_dict['title'] = "커밋하라"
    attachments_dict['title_link'] = "Do Commit!"
    attachments_dict['fallback'] = "오늘 하루가 얼마 남지 않았어!"
    attachments_dict['text'] = "%s님 커밋하세요!" % (username)
    attachments_dict['mrkdwn_in'] = ['text', 'pretext']
    attachments = [attachments_dict]

    slack.chat.post_message(channel=COMMIT_CHANNEL, text=None, attachments=attachments, as_user=False)
