import att_message as body
import json
import random

from dialog.dialog import Dialog
from keyboard import keyboard as kb
from recommender import recommender
from summarizer import summarizer
from youtube import youtube
from nlp import nlp

def explain_rec(dialog, telegram):
    message = summarizer.dialog_summarize(dialog.attributes, dialog.recommendation_id, dialog.movie)

    message = "I hope you enjoy this explanation...\n\n" + str(message)
    
    keyboard = kb.explain_keyboard(telegram)

    return dialog, __chat_message(telegram, message, keyboard)

def force_rec(dialog, telegram):
    recommendation_id, text = recommender.rec_force(dialog.dialog_id, dialog.telegram_id)

    dialog.recommendation_id = recommendation_id

    return __recommendation_message(telegram, dialog, text)

def back_page(dialog, telegram):
    message = __get_intent_message('back_page')

    dialog.paginate.prev_page()

    keyboard = kb.back_page_keyboard(telegram, dialog.paginate)

    return dialog, __chat_message(telegram, message, keyboard)

def something_else(dialog, telegram):
    message = __get_intent_message('something_else')

    dialog.paginate.next_page()

    keyboard = kb.something_else_keyboard(telegram, dialog.paginate)            
    
    return dialog, __chat_message(telegram, message, keyboard)
    

def user_about(telegram_id, telegram, resp):
    age = nlp.get_age(resp)
        
    dialog = Dialog(telegram_id, int(age), 1)

    dialog.step = 2
    
    if int(age) < 18:

        message = __get_intent_message('minor')

        keyboard = kb.auth_keyboard(telegram)

        return dialog, __chat_message(telegram, message, keyboard)

    return user_authorize(dialog, telegram)

def user_authorize(dialog, telegram):
    message = __get_intent_message('user_about')

    dialog_id, properties = recommender.rec_init(dialog.telegram_id, dialog.age, dialog.auth)

    dialog.dialog_id = dialog_id
    dialog.paginate = properties

    keyboard = kb.properties_keyboard(telegram, dialog.paginate)
    
    return dialog, __chat_message(telegram, message, keyboard)

def characteristic(dialog, telegram, resp):
    message = __get_intent_message('characteristic')

    value = resp #body.get_entity_value(resp)
        
    json_file = recommender.rec_second(value, dialog.dialog_id, dialog.telegram_id)

    if "error" in json_file:
        text = json_file.get("error")
        
        keyboard = kb.liked_keyboard(telegram)

        return dialog, __chat_message(telegram, text, keyboard)

    dialog.ask = json_file.get("ask")
    
    message = body.try_except_entity(message,'property', value)
    
    dialog.paginate = json_file.get('characteristics')

    dialog.step = 3
    
    keyboard = kb.properties_keyboard(telegram, dialog.paginate)
    
    return dialog, __chat_message(telegram, message, keyboard)

def properties(dialog, telegram, resp):
    message = __get_intent_message("property")

    #value = body.get_entity_value(resp)#valor digitado pelo usuário
    value = resp.split(') ')[1].split(' (')[0] if ') ' in resp else resp
            
    if(dialog.state == 0): #caso esteja no estado 0, fará requesição no endpoit/third
        recommendation_id, text = recommender.rec_third(value, dialog.dialog_id, dialog.telegram_id)
        dialog.state = 1

        dialog.recommendation_id = recommendation_id
        
        
        return __ask_message(telegram, message, dialog, text)
    
    else: 
        #value = resp.get("text")
        value = resp
        recommendation_id, json_text = recommender.rec_awnser(dialog.ask, value, dialog.dialog_id, dialog.telegram_id)
        dialog.recommendation_id = recommendation_id
    
        return __ask_message(telegram, message, dialog, json_text)

def liked_recommendation(telegram):
    text = "I'm really happy to help you! I hope you enjoyed my explanations and recommendations. If you want to talk with me again, choose 'hello' or send me a message whenever you want"
        
    keyboard = kb.liked_keyboard(telegram)

    return __chat_message(telegram, text, keyboard)

def greet(telegram_id, telegram):
    message = __get_intent_message("greet")

    dialog = Dialog(telegram_id, 0, 0)
    dialog.step = 1

    keyboard = kb.greet_keyboard(telegram)
        
    return dialog, __chat_message(telegram, message, keyboard)

def goodbye():
    message = __get_intent_message("goodbye")
    survey = '\nBefore you leave, answer a little survey about this conversation: \nhttps://forms.gle/JC9imLE2gwBAXzzG9 \n\nThank you! Bye, bye.'
    message += '\n' + survey
    return [message]

def __recommendation_message(telegram, dialog, json_text):
    
    message = __get_intent_message('recommendation')

    if "error" in json_text:
        text = json_text.get("error")
        
        keyboard = kb.liked_keyboard(telegram)

        return dialog, __chat_message(telegram, text, keyboard)
    
    value = json_text.get('recommendation')
    
    dialog.attributes = json_text.get('properties')
    
    #dialog.movie = json_text.get("imdbId")
    dialog.movie = json_text.get("movie_id")
        
    video = youtube.youtube_link_one(value + " movie trailer") 

    value += "\n"+ youtube.youtube_link_one(value)
    
    message = body.try_except_entity(message,'recommendation',value)
    
    message = message + "\n" + str(video)

    keyboard = kb.rec_keyboard(telegram)

    return dialog, __chat_message(telegram, message, keyboard)

def __chat_message(telegram, message, keyboard):
    reply_kb_markup = telegram.ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    return [message,reply_kb_markup]

def __ask_message(telegram, message, dialog, json_text):

    if "error" in json_text:
        text = json_text.get("error")
        
        keyboard = kb.liked_keyboard(telegram)

        return dialog, __chat_message(telegram, text, keyboard)
    
    dialog.ask = json_text.get("ask")

    if json_text.get("response"):
        text = json_text.get("response")
        
        keyboard = kb.liked_keyboard(telegram)

        return dialog, __chat_message(telegram, text, keyboard)
        
    if dialog.ask == 0:
        dialog.paginate = json_text.get('attributes')
        keyboard = kb.attributes_keyboard(telegram, json_text.get('attributes'))

        return dialog, __chat_message(telegram, message, keyboard)
    else:
        return __recommendation_message(telegram, dialog, json_text)
        
def __get_intent_message(intent):
    data = ''
    with open("json_intent_answ_teste", "r") as file:
        data = json.loads(file.read())
    return data.get(intent)[random.randint(0,2)].get("text")