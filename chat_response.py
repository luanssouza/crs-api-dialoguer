from bucket import bucket
from chat import chat_message as cm

#adequar o return, para retornar array com mensagem e o movie_ID
def response(resp, telegram, telegram_id):
    print(resp)
    
    # Textual response
    if resp == 'I liked the recommendation':
        return cm.liked_recommendation(telegram)

    if resp == 'Bye':
        return cm.goodbye()

    if resp == 'hello' or resp == 'Hello':
        dialog, r = cm.greet(telegram_id, telegram)
        bucket.save_object(dialog.telegram_id, dialog)
        return r

    r = ''
    dialog = bucket.loads_object(telegram_id)

    if resp == 'Explain this recommendation':
        dialog, r = cm.explain_rec(dialog, telegram)
      
    elif resp == 'Recommend':
        dialog, r = cm.force_rec(dialog, telegram)
    
    elif resp == 'Back Page':
        dialog, r = cm.back_page(dialog, telegram)
        
    elif resp == 'Something else':
        dialog, r = cm.something_else(dialog, telegram)
    
    elif resp == "I'm not authorized":
        dialog.auth = 0
        dialog, r = cm.user_authorize(dialog, telegram)
      
    elif resp == "I'm authorized":
        dialog, r = cm.user_authorize(dialog, telegram)

    if r:
        bucket.save_object(dialog.telegram_id, dialog)
        return r
         
    # Step response
    if dialog.step == 1:
        dialog, r = cm.user_about(telegram_id, telegram, resp)
    
    elif dialog.step == 2:
        dialog, r = cm.characteristic(dialog, telegram, resp)
        
    elif dialog.step == 3:
        dialog, r = cm.properties(dialog, telegram, resp)
    
    bucket.save_object(dialog.telegram_id, dialog)
    
    return r