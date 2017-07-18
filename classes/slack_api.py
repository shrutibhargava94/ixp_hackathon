from slackclient import SlackClient

class Slack:

    def __init__(self, token):
        self.slack_client = SlackClient(token);

    ## Send a mesage to a channel
    # @param - channel_id: internal slack id of a channel_id
    # @param - message: The message text
    def send_message(self,channel_id, message):
        self.slack_client.api_call(
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
