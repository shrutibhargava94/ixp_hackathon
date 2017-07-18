from slackclient import SlackClient

class Slack:

    def __init__(self, token):
        self.TEST_TOKEN = 'xoxp-212186059425-213950604099-213773140256-7887874f2c25319fe09a6bcdd4424ec6';
        self.slack_client = SlackClient(token);

    ## Send a mesage to a channel
    # @param - channel_id: internal slack id of a channel_id
    # @param - message: The message text
    def send_message(self,channel_id, message):
        sefl.slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=message,
            username='pythonbot',
            icon_emoji=':robot_face:'
        )

    ## Obtain info from a channel
    # @param - channel_id: internal slack id of a channel_id
    def channel_info(self,channel_id, ts):
        history = self.slack_client.api_call(
          "channels.history",
          channel=channel_id,
          oldest=ts
        )
        return history
