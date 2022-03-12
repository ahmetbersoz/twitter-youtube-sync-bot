import tweepy
import scrapetube
from pytube import YouTube 
import json
import os

# read credentials
f = open('credentials.json')
creds = json.load(f)

# connect to twitter api
auth = tweepy.OAuthHandler(creds['twitter']['consumer_key'], creds['twitter']['consumer_secret'])
auth.set_access_token(creds['twitter']['access_token'], creds['twitter']['access_secret'])
api = tweepy.API(auth)

# get last video tweet
latest_tweet = api.user_timeline(count=1)[0].text

# get rid of the 'https://t.co/'
latest_twitter_video_title = latest_tweet.split(' https://t.co/')[0]

# get latest channel video information
youtube_videos = scrapetube.get_channel(channel_url=creds['youtube']['channel_url'], limit=1)
latest_youtube_video_title = ''
latest_youtube_video_id = ''

for video in youtube_videos:
    latest_youtube_video_title = video['title']['runs'][0]['text']
    latest_youtube_video_id = video['videoId']

# detect is there a new video
if (latest_twitter_video_title != latest_youtube_video_title):
    youtube_link = "https://www.youtube.com/watch?v=" + latest_youtube_video_id
    video_filename = latest_youtube_video_id + '.mp4'
    video_path = './' + video_filename

    # try: 
    # download te video
    yt = YouTube(youtube_link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='.', filename=video_filename)

    # upload the video to twitter
    media =  api.media_upload(video_path, media_category='tweet_video')
    
    # send tweet
    api.update_status(status=latest_youtube_video_title, media_ids=[media.media_id])

    # delete the video
    os.remove(video_path)   

    print('New video uploaded')     
    # except: 
    #     # delete the video
    #     os.remove(video_path)   

    #     print("Error occured")
else:
    print('No new video')




