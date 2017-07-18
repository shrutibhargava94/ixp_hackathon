from slackclient import SlackClient
import json
import time

TEST_TOKEN = 'xoxp-212186059425-213950604099-213773140256-7887874f2c25319fe09a6bcdd4424ec6';
TOKEN = TEST_TOKEN;
slack_client = SlackClient(TOKEN);

## Send a mesage to a channel
# @param - channel_id: internal slack id of a channel_id
# @param - message: The message text
def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='pythonbot',
        icon_emoji=':robot_face:'
    )

## Obtain info from a channel
# @param - channel_id: internal slack id of a channel_id
def channel_info(channel_id, ts):
    history = slack_client.api_call(
      "channels.history",
      channel=channel_id,
      oldest=ts
    )
    return history

timestamps = dict();

## Obtain the last timestamp of the user_id
# @param - user_id: the id of the user from the Slack API
# if first time seeing user return 0
# else return the last time a user was seen
def get_timestamp(user_id):
    global timestamps
    if user_id in timestamps: ts = timestamps[user_id]
    else: ts = 0
    timestamps[user_id] = time.time()
    return ts

#send_message("C68MNQ02W","This is a test");

from flask import Flask
from flask import request

# Instantiation app from flask
app = Flask(__name__)

# Respond to the / path
@app.route('/')
def home():
    return "Hello Summarizer App!"

# Respond the slack tags
@app.route('/slack/summarize', methods=['POST'])
def summarize_text():
    channel_id = "C68MNQ02W"
    user_id= request.form['user_id'];
    ts = get_timestamp(user_id);
    info = channel_info(channel_id, ts);
    summary = "test_summary"
    return summary

# Run the app in main
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3000)
