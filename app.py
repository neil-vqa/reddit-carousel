from flask import Flask, render_template
from pathlib import Path
import praw
import os
from service import main

base_dir = Path('static/')
env_path = base_dir / '.env'

app = Flask(__name__)

CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent='web:github.com/neil-vqa/reddit-carousel:v1.0 (by /u/neilthegreatest)')


@app.route('/')
def home():
    subs = main(reddit)
    return render_template('index.html',
                           astros=subs['pick_astro'],
                           arts=subs['pick_art'],
                           showers=subs['pick_shower'],
                           learns=subs['pick_til'],
                           iams=subs['pick_iam'],
                           memes=subs['pick_meme'],
                           foods=subs['pick_food'],
                           data=subs['pick_data'],
                           maps=subs['pick_map'],
                           zip=zip)


if __name__ == '__main__':
    app.run(debug=True)
