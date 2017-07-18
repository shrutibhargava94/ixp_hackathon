class Helper
import json
import time


class Helper:

    
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
