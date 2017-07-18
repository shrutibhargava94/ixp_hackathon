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
