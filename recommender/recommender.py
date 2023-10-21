import requests as req
import json
import os

from services.answer_service import insert_answer_dict
from services.recommendation_service import insert_recommendation_dict

import services.dialog_service as dg_service

def rec_init(telegram_id, age, auth):

    last_dialog = dg_service.get_last_dialog()

    is_proposal = last_dialog.id%2 > 0 if last_dialog else True

    data = {'dialogId': telegram_id,'age':age, 'ageAuth': auth, 'isProposal': is_proposal}

    response = req.post(os.environ.get("RECOMMENDER_API") + '/init',json=data)
    
    res_json = response.json()

    dialog_id = dg_service.insert_dialog_dict({"telegramId": telegram_id, "age": age, "authorization": auth, 'isProposal': is_proposal})

    return dialog_id, res_json.get('properties')

def rec_second(obj, dialog_id, telegram_id):

    data = {"property": obj,"dialogId": telegram_id}

    dg_service.update_property_dialog_dict(dialog_id, obj)

    response = req.post(os.environ.get("RECOMMENDER_API") + '/second',json=data)
    
    return response.json()

def rec_third(value, dialog_id, telegram_id):

    data = {"object": value,"dialogId": telegram_id}

    recommendation_id = 0

    dg_service.update_object_dialog_dict(dialog_id, value)

    response = req.post(os.environ.get("RECOMMENDER_API") + '/third',json=data)
        
    response = response.json()

    if "ask" in response and response['ask'] == 1:
        rec = {
            "dialogId": dialog_id, "movieId": response["movie_id"], 
            "imdbId": response["imdbId"], "properties": response["properties"]
        }

        recommendation_id = insert_recommendation_dict(rec)

    return recommendation_id, response

def rec_awnser(ask, resp, dialog_id, telegram_id):

    data = {"ask": ask, "resp": resp,"dialogId": telegram_id}

    recommendation_id = 0
    
    insert_answer_dict({"ask": ask, "answer": resp, "dialogId": dialog_id})

    response = req.post(os.environ.get("RECOMMENDER_API") + '/answer',json=data)
    
    response = response.json()
    
    if "ask" in response and response['ask'] == 1:
        rec = {
            "dialogId": dialog_id, "movieId": response["movie_id"], 
            "imdbId": response["imdbId"], "properties": response["properties"]
        }

        recommendation_id = insert_recommendation_dict(rec)

    return recommendation_id, response

def rec_force(dialog_id, telegram_id):

    data = {'dialogId': telegram_id}
    
    response = req.post(os.environ.get("RECOMMENDER_API") + '/recommend',json=data)

    response = response.json()
    
    rec = {
        "dialogId": dialog_id, "movieId": response["movie_id"], 
        "imdbId": response["imdbId"], "properties": response["properties"], 
        "requested": True
    }

    recommendation_id = insert_recommendation_dict(rec)

    return recommendation_id, response