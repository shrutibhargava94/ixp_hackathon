import json
import time

class Helper:

    def __init__(self):
        self.timestamps = dict();

    ## Obtain the last timestamp of the user_id
    # @param - user_id: the id of the user from the Slack API
    # if first time seeing user return 0
    # else return the last time a user was seen
    def get_timestamp(self,user_id):
        if user_id in self.timestamps: ts = self.timestamps[user_id]
        else: ts = 0
        self.timestamps[user_id] = time.time()
        return ts
