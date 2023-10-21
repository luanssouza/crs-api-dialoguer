from googleapiclient import discovery

import os

build = discovery.build
api_key = os.environ.get("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)

def youtube_link(q,max):
    req = youtube.search().list(q=q, part='id', type='video', maxResults=1, order='relevance' )
    response = req.execute()
    return response

def youtube_link_one(chave):
    response = youtube_link(chave,1)
    link = "https://www.youtube.com/watch?v="+response.get("items")[0].get("id").get("videoId")
    return link
