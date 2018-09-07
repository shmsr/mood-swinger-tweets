from flask import Flask, request, json, render_template
import tweepy
import string

# Name it the '__name__' of this module (tweet-harvest)
app = Flask(__name__)

# Load our config from an object, or module (config.py)
app.config.from_object('config')

# These config variables come from 'config.py'
auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'], app.config['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'], app.config['TWITTER_ACCESS_TOKEN_SECRET'])
tweepy_api = tweepy.API(auth)

# We define our URL route, and the controller to handle requests
@app.route('/')
def hello_world():
    return render_template('home.html', title='Home')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def handle_intsrverr(e):
    return render_template('500.html'), 500


def get_tweets(username, count):
    try:
        tweets = tweepy_api.user_timeline(screen_name=username, count=count)
        return [{
                'tweet': t.text,
                'created_at': t.created_at,
                'username': username,
                'headshot_url': t.user.profile_image_url,
                'name': t.user.name }
                for t in tweets]
    except tweepy.TweepError as e:
        return 0

@app.route('/tweet-harvester/<string:username>')
@app.route('/tweet-harvester/<string:username>/')
@app.route('/tweet-harvester/<string:username>/<int:count>')
def tweets(username, count=5):
    tweets = get_tweets(username, count)
    if tweets:
        img = tweets[0]['headshot_url'].replace("_normal","")
        name = tweets[0]['name']
        update = tweets[0]['tweet']
        return render_template('tweets.html', tweets=tweets, title=username, img=img, name=name, last=update)
    else:
        return render_template('Tweet_404.html'), 404