from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Video(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    published_at = db.Column(db.DateTime)
    thumbnails = db.Column(db.Text)

def fetch_and_store_videos():
    with app.app_context():    #to run in the current flask file
        API_KEY = 'Your api key'  #can not make mine public 
        base_url = 'https://www.googleapis.com/youtube/v3/search'
        published_after = (datetime.now(timezone.utc) - timedelta(seconds=100)).isoformat()

        params = {
            'key': API_KEY,
            'part': 'snippet',
            'type': 'video',
            'order': 'date',
            'q': 'cricket',  # search query can also call multiple at like(boating | rafting | fishing)
            'publishedAfter': published_after
        }
        response = requests.get(base_url, params=params)
        print(response.text)
        if response.status_code == 200:
            data = response.json()
            for item in data['items']:
                published_at_str = item['snippet']['publishedAt']                                        #to save in database these are needed
                published_at_datetime = datetime.fromisoformat(published_at_str.replace('Z', '+00:00'))  #to save in database these are needed
                video = Video(
                    title=item['snippet']['title'],
                    description=item['snippet']['description'],
                    published_at=published_at_datetime,
                    thumbnails=item['snippet']['thumbnails']['default']['url']
                )
                db.session.add(video)
            db.session.commit()
        else:
            print('Failed to fetch videos from YouTube API')

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_store_videos, 'interval', seconds=100)
scheduler.start()
# fetch_and_store_videos() #for testing purpose one can stop the scheduler and call the function only once ,comment the above 3 line and uncomment this one 

@app.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    videos = Video.query.order_by(Video.published_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    video_list = [{'title': video.title, 'description': video.description, 'published_at': video.published_at, 'thumbnails': video.thumbnails} for video in videos.items]
    return jsonify({
        'videos': video_list,
        'total_pages': videos.pages,
        'total_videos': videos.total
    })



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
