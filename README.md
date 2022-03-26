# A Twitter & Youtube bot

This bot manages "Daniel Labelle" Twitter fan page [@DanielLabelleFP](https://twitter.com/DanielLabelleFP). It syncs videos shared on Youtube and Twitter.

## Features

- Get youtube channel videos automatically
- Get latest tweets from twitter
- Compare latest twitter video & latest youtube video
- Download new videos and upload to twitter

## Requirements
- Twitter developer platform elevated access (its a bit difficult to be accepted)

## Installation

Install the dependencies

```sh
pip install -r requirements.txt
```

Create credentials.json with this structure:

```json
{
    "twitter": {
        "access_token": "",
        "access_secret" : "",
        "consumer_key": "",
        "consumer_secret": ""        
    },
    "youtube": {
        "channel_url": ""
    }
}
```


## Usage

Run the scripts directly or create a cronjob which regularly runs the script.

```
python bot.py
```
