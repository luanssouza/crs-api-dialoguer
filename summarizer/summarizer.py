import requests
import random
import json
import os

from services.explanation_service import insert_explanation_dict

def dialog_summarize(attr, recommendation_id, imdb_id):
    txt = ''
    attributes = []
    success = False
    
    #for i in range(len_attr):
    for a in attr:
        try: 
            #attributes.append(attr[len(attr)-1][i]['object'])
            attributes.append(a['object'])
        except:
            none=''

    data = {
        "movieId": imdb_id,
        "profileAttributes": attributes
    }
    try:
        response = requests.post(os.environ.get("SUMMARIZER_API") + '/summarize', json=data)
        txt = json.loads(response.text)
        exp = txt.get("explanation")
        success = True
        if exp == None:
            exp = __get_intent_message("something_wrong")
    except:
        exp = __get_intent_message("something_wrong")

    insert_explanation_dict({"recommendationId": recommendation_id, "success": success})

    return exp

def __get_intent_message(intent):
    data = ''
    with open("json_intent_answ_teste", "r") as file:
        data = json.loads(file.read())
    return data.get(intent)[random.randint(0,2)].get("text")