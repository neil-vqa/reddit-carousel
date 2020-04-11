from flask import Flask, render_template, url_for
import praw


app = Flask(__name__)


reddit = praw.Reddit(client_id='iGMNdhNR4e_Atg',
                    client_secret='xkuIbmiS2GHhNr-NkpmzPGRVYMI',
                    user_agent='web:github.com/neil-vqa/reddit-carousel:v1.0 (by /u/neilthegreatest)')

pick_astro = []
pick_art = []
pick_shower = []
pick_til = []
pick_iam = []
pick_meme = []
pick_food = []
pick_data = []
pick_map = []


for submission in reddit.subreddit('astrophotography').top(time_filter='day', limit=10):
	if (submission.link_flair_css_class == 'image') or ((submission.is_self != True) and ((".jpg" in submission.url) or (".png" in submission.url))):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}'
		}
		pick_astro.append(pick)

for submission in reddit.subreddit('Art').top(time_filter='day', limit=10):
	if (submission.link_flair_css_class == 'image') or ((submission.is_self != True) and ((".jpg" in submission.url) or (".png" in submission.url))):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}'
		}
		pick_art.append(pick)

for submission in reddit.subreddit('Showerthoughts').top(time_filter='day', limit=10):
	pick = {
		'title': submission.title,
		'author': submission.author,
		'upvotes': submission.score,
		'link': f'https://www.reddit.com{submission.permalink}',
		'sub': submission.subreddit
	}
	pick_shower.append(pick)

for submission in reddit.subreddit('todayilearned').top(time_filter='day', limit=10):
	pick = {
		'title': submission.title,
		'author': submission.author,
		'upvotes': submission.score,
		'link': f'https://www.reddit.com{submission.permalink}',
		'sub': submission.subreddit
	}
	pick_til.append(pick)
	
for submission in reddit.subreddit('IAmA').top(time_filter='day', limit=10):
	pick = {
		'title': submission.title,
		'author': submission.author,
		'upvotes': submission.score,
		'link': f'https://www.reddit.com{submission.permalink}',
		'sub': submission.subreddit
	}
	pick_iam.append(pick)

for submission in reddit.subreddit('wholesomememes').top(time_filter='day', limit=10):
	if (submission.link_flair_css_class == 'image') or ((submission.over_18 != True) and ((".jpg" in submission.url) or (".png" in submission.url))):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}',
			'sub': submission.subreddit
		}
		pick_meme.append(pick)

for submission in reddit.subreddit('food').top(time_filter='day', limit=10):
	if (submission.link_flair_css_class == 'image') or ((".jpg" in submission.url) or (".png" in submission.url)):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}',
			'sub': submission.subreddit
		}
		pick_food.append(pick)

for submission in reddit.subreddit('dataisbeautiful').top(time_filter='day', limit=15):
	if (submission.link_flair_css_class == 'image') or ((".jpg" in submission.url) or (".png" in submission.url)):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}',
			'sub': submission.subreddit
		}
		pick_data.append(pick)

for submission in reddit.subreddit('imaginarymaps').top(time_filter='day', limit=10):
	if (submission.link_flair_css_class == 'image') or ((submission.is_self != True) and ((".jpg" in submission.url) or (".png" in submission.url))):
		pick = {
			'title': submission.title,
			'url': submission.url,
			'author': submission.author,
			'upvotes': submission.score,
			'link': f'https://www.reddit.com{submission.permalink}'
		}
		pick_map.append(pick)


@app.route('/reddit')
def home():
    return render_template('index.html', astros=pick_astro, arts=pick_art, showers=pick_shower, learns=pick_til, iams=pick_iam, memes=pick_meme, foods=pick_food, data=pick_data, maps=pick_map, zip=zip)
    


if __name__ == '__main__':
	app.run(debug=False)

