#from wit import Wit
#import chat_response as ct

#access_token = 
#client = Wit(access_token = access_token)
#message_text = ''
#while message_text != 'quit':
#    if message_text == 'quit':
#        continue
#    message_text = input()
#    resp = client.message(message_text) #por aqui conseguimos a resposta da api pra uma entrada de texto
#    print(ct.response(resp))


#def wit_response(message_text): #função ainda em teste, a ser utilizada em webhook_server.py
#    resp = client.message(message_text)
#    return ct.response(resp)