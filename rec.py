import requests
import chat_response as ct
import random
import json
from googleapiclient import discovery
import random as rd
import app
build = discovery.build
api_key = ''
youtube = build('youtube', 'v3', developerKey=api_key)

def dialog_recommender(intent,entity,chat_id,resp):
    txt = ''
    value = ''
    likes = "yes" if intent!="deny" else "no"
    data = {
        "intent": intent,
        "entity": entity,
        "likes":  likes,
    }
    try:
        response = requests.post('link do Andre', json=data)
        txt = response.txt
    except:
        json_const = ct.json_reply(value, resp)
        message = json_const.get('post_rec_bad_request')[random.randint(0,2)].get("text")
        return message

    data = json.loads(txt)
    '''
    if data.get("id_recomendação") == "fim da recomendação"
        dialog_summarize(historic)
    '''
    return data

def stream_explanation():
    att = app.getAtt()
    mm = app.getMovie()
    movie = mm.pop()
    txtRec = dialog_summarize(att,movie)
    return txtRec




def dialog_summarize(att,imdbId):
    txt = ''
    attributes = []
    lenVec = len(att[0])
    i = 0
    while i <= lenVec:
       try: 
            attributes.append(att[len(att)-1][i]['object'])
       except:
            none=''
       i = i +1  

    data = {
        "imdbId": imdbId,
        "profileAttributes": attributes
        
    }
    try:
        response = requests.post('', json=data)
        a = response.text
        txt = json.loads(a)
        exp = txt.get("explanation")
        if exp == None:
            jsonConst = ct.json_reply()
            exp = jsonConst.get("something_wrong")[random.randint(0, 2)].get("text")
    except:
        jsonConst = ct.json_reply()
        exp = jsonConst.get("something_wrong")[random.randint(0, 2)].get("text")
    return exp


def youtube_link(q,max):
    req = youtube.search().list(q=q, part='id', type='video', maxResults=1, order='relevance' )
    response = req.execute()
    return response

def youtube_link_one(chave):
    response = youtube_link(chave,1)
    lenght = len(response.get("items"))
    link = "https://www.youtube.com/watch?v="+response.get("items")[0].get("id").get("videoId")
    return link
