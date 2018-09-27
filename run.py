from tweet_harvester import app
import os
# 'app' originates from the line 'app = Flask(__name__)'
app.run(host = '0.0.0.0',port = 8080 | os.environ['PORT'])