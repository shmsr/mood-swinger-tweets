def remove_non_ascii(text):
    return "".join(i for i in text if ord(i) < 128)


def moody(rec_tweet):
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object('config')
    from watson_developer_cloud import ToneAnalyzerV3
    ta_username = app.config['TONE_ANALYSER_USERNAME']
    ta_password = app.config['TONE_ANALYSER_PASSWORD']
    tone_analyzer = ToneAnalyzerV3(username=ta_username,password=ta_password,version='2017-09-21')
    texts = rec_tweet
    texts = remove_non_ascii(texts)
    print(texts+"\n")
    tone_analysis = tone_analyzer.tone({'text': texts},'application/json')
    return tone_analysis


def isemotional(tone):
    if tone in ('anger', 'fear', 'joy', 'sadness'):
        return True
    return False


def recommend_playlist(rec_tweet):
    tone_json = moody(rec_tweet)
    tones_list = tone_json.get_result()["document_tone"]["tones"]

    mood = ""
    mood_id = ""
    max_score = -1
    playlist_url = ""

    for tone in enumerate(tones_list):
        if isemotional(tone[1]["tone_id"]) and tone[1]["score"] > max_score:
            max_score = tone[1]["score"]
            mood = tone[1]["tone_name"]
            mood_id = tone[1]["tone_id"]

    if max_score <= 0:
        return -1

    if mood_id == "anger":
        playlist_url = "https://www.youtube.com/embed/Q1jE25zn8RU"
    if mood_id == "fear":
        playlist_url = "https://www.youtube.com/embed/xo1VInw-SKc"
    if mood_id == "joy":
        playlist_url = "https://www.youtube.com/embed/LjhCEhWiKXk"
    if mood_id == "sadness":
        playlist_url = "https://www.youtube.com/embed/aJOTlE1K90k"

    mood_play = {"mood": mood, "url": playlist_url, "json_res": tones_list}
    return mood_play
