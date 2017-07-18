from flask import Flask
from flask import request

TEST_TOKEN = 'xoxp-212186059425-213950604099-213773140256-7887874f2c25319fe09a6bcdd4424ec6';

from classes.helper import Helper
from classes.slack_api import Slack

# Instiantiate Slack API class
sc = Slack(TEST_TOKEN);

# Instantiate app from flask
app = Flask(__name__)

TEST_CHANNEL = "C68MNQ02W"

# Respond to the / path
@app.route('/')
def home():
    message = "Hello Summarizer App"
    sc.send_message(TEST_CHANNEL,message)
    return "Completed."

# Respond the slack tags
@app.route('/slack/summarize', methods=['POST'])
def summarize_text():
    channel_id = TEST_CHANNEL
    user_id= request.form['user_id']
    ts = Helper.get_timestamp(user_id)
    info = sc.channel_info(channel_id, ts)
    summary = "test_summary"
    return summary

# Run the app in main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
