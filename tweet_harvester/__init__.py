from flask import Flask, request, json, render_template, redirect, url_for
import tweepy

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
@app.route('/home')
def hello_world():
    return render_template('home.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_intsrverr(e):
    return render_template('500.html'), 500
    
def get_tweets(username):
    try:
        tweets = tweepy_api.user_timeline(screen_name=username)
        return [{
                'tweet': t.text,
                'created_at': t.created_at,
                'username': username,
                'headshot_url': t.user.profile_image_url}
                for t in tweets]
    except tweepy.TweepError as e:
        return 0


@app.route('/tweet-harvester/<string:username>')
def tweets(username):
    tweets = get_tweets(username)
    if tweets:
        return render_template('tweets.html', tweets=tweets, title=username)
    else:
        return render_template('Tweet_404.html'), 404

        
        