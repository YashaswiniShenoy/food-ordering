from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from watson_developer_cloud import ConversationV1
import json
import sqlite3

context = None

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Received /start command')
    update.message.reply_text('Hi!')


def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Help!')


def error_callback(bot, update, error):
    """Log Errors caused by Updates."""
    print('Update "%s" caused error "%s"', update, error)

def message(bot, update):
    print('Received an update')
    global context

    conversation = ConversationV1(username='551ef9bd-a3b2-4b2b-9765-c0c16cbc67c4',  # TODO
                                  password='533TSLvTQtru',  # TODO
                                  version='2018-02-16')

    # get response from watson
    response = conversation.message(
        workspace_id='1c5ddddb-cbd3-432c-9f39-246525ccf4e3',  # TODO
        input={'text': update.message.text},
        context=context)
    print(json.dumps(response, indent=2))
    context = response['context']
    # build response
    resp = ''
    for text in response['output']['text']:
        resp += text
    if len(resp)>0:
        update.message.reply_text(resp)
    #extraxt context
    if 'cuisine' in response['context']:
        cuisine = str(response['context']['cuisine'])
        print(cuisine)
        # retrieve data in database
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where cuisine='" + cuisine + "'"
        rows=c.execute(query)
        for row in rows:
             r='%s is a  restaraunt that has %s cuisine with rating %d with timmings %d %d'%(row[0],row[1], row[2], row[3],row[4])
             r=r.capitalize()
        update.message.reply_text(r)
        conn.commit()
        conn.close()
        context=None
    if 'resturant' in response['context']:
        resturant = str(response['context']['resturant'])
        print(resturant)
        # retrieve data in database
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from food1 where rest='" + resturant + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%s is a %s option from %s priced at %d' % (row[1], row[3], row[0], row[2])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context=None

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('691666941:AAEDTjvGB0H3GDXNpa25WDLTZ_jeaVj0jlk')  # TODO

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, message))
    
    dp.add_error_handler(error_callback)


    # Start the Bot
    updater.start_polling()


    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    


if __name__ == '__main__':
    main()
