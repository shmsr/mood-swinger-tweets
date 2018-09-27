from tweet_harvester import app
import os
port = os.environ['PORT']
# 'app' originates from the line 'app = Flask(__name__)'
app.run(host = '0.0.0.0', port)