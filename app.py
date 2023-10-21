from att_message import get_entity, get_entity_value, get_intent
import logging
import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from wit import Wit
import os
import chat_response as bot_answer
import rec
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path) 

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
WIT_TOKEN = os.environ.get("WIT_TOKEN")
BOT_USER_NAME = os.environ.get("BOT_USER_NAME")
HEROKU_URL = os.environ.get("HEROKU_URL")
PORT = int(os.environ.get('PORT','8433'))


# olha, essa linha aí de baixo, eu não sei mto bem pra o que faz kkk
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)#Define Command Handlers

def start(updater, context):  
   """Handler for /start command"""
   updater.message.reply_text('Send a "Hello" to start our conversation or Send /help to see the interaction instructions.')

def help(updater, context):  
   """Handler for /help command"""
   updater.message.reply_text(
       'Send a \"Hello\" to start our conversation. \n'
       'When you send a message, I\'ll process the text and give you a response. \n'
       'Some responses can come with options, then you can select one of them. \n'
       'If you scroll the chat and the options disappear, you can show up it again by clicking the message button, as in the image.'
   )

   updater.message.reply_photo(open("button.png",'rb'))
   
# function to modelate all the user interaction with the bot:
def userText(updater, context):  
    """Function to reply to user text"""

    #wit_client = Wit(access_token = WIT_TOKEN)
    
    #client_answer = wit_client.message(updater.message.text)

    chat_id = updater.message.chat_id 
    #intent = get_intent(client_answer)
    
    try:
        #message = bot_answer.response(client_answer,telegram, chat_id, intent)
        message = bot_answer.response(updater.message.text,telegram, chat_id)
        try:    
            updater.message.reply_text(message[0],reply_markup = message[1])
        except Exception as e:
            print(e)
            updater.message.reply_text(message[0])
    except Exception as e:
        print(e)
        updater.message.reply_text("Ops! Something went wrong... Try again!")

def main():
   
    """starting the bot"""

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
 
    #getting the dispatchers to register handlers
    dp = updater.dispatcher
    
    #registering commands
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,userText))    #starting the bot
    #dp.add_handler(CallbackQueryHandler(form, pattern='form_*'))
    updater.start_webhook(listen = "0.0.0.0",
                      port = int(PORT),
                    #   port = int(8433),
                      url_path = TELEGRAM_TOKEN)

    updater.bot.set_webhook(HEROKU_URL+TELEGRAM_TOKEN)

    updater.idle()
    

if __name__ == '__main__':
   
    main()