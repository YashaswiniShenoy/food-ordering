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
    if 'itemname' in response['context']:
        fooditem=str(response['context']['itemname'])
        print(fooditem)
        conn=sqlite3.connect('pro1.db')
        c=conn.cursor()
        query="select rest from food1 where item='"+ fooditem+"'"
        rows=c.execute(query)
        for row in rows:
            print(row)
            r='%s' %row[0]
            r=r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context=None
    if ('resturant' in response['context']) and ('Rest_name' in response['intents'][0]['intent']) :
        resturant = str(response['context']['resturant'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from food1 where rest='" + resturant + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%s is a %s option from %s priced at %d' % (row[1], row[3], row[0], row[2])
            r = r.capitalize()
            update.message.reply_text(r)

        if resturant == '1947':
            update.message.reply_text("https://im1.dineout.co.in/images/uploads/restaurant/sharpen/5/r/n/p5052-14613188305719f4aeb70e5.jpg?w=1200")
        elif resturant  == 'alphas':
            update.message.reply_text()

        elif resturant =='amande':
            update.message.reply_text()

        elif resturant =='ambrosia':
            update.message.reply_text()

        elif resturant =='cafe noir':
            update.message.reply_text()

        elif resturant =='cheffu n steffu':
            update.message.reply_text()

        elif resturant =='communiti':
            update.message.reply_text()

        elif resturant =='cream byte':
            update.message.reply_text()

        elif resturant =='dejavu':
            update.message.reply_text()

        elif resturant =='echo':
            update.message.reply_text()

        elif resturant =='fab cafe':
            update.message.reply_text()

        elif resturant =='kappi katte':
            update.message.reply_text()

        elif resturant =='krishna grand':
            update.message.reply_text()

        elif resturant =='mint masala':
            update.message.reply_text("https://b.zmtcdn.com/data/pictures/7/51367/379001e88e392e22f722ad5163c708b1.jpg?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A")

        elif resturant =='nandhana palace':
            update.message.reply_text()

        elif resturant =='onesta':
            update.message.reply_text()

        elif resturant =='pakaashala':
            update.message.reply_text()

        elif resturant =='prost':
            update.message.reply_text()

        elif resturant =='royal andhra spice':
            update.message.reply_text()

        elif resturant =='stories':
            update.message.reply_text()

        elif resturant ==' the vintage':
            update.message.reply_text()

        elif resturant =='truffles':
            update.message.reply_text()

        elif resturant =='woodlands':
            update.message.reply_text()



        conn.commit()
        conn.close()
        context=None
    if ('resturant' in response['context'])and ('popularity' in response['intents'][0]['intent']) :
        resturant = str(response['context']['resturant'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where name='" + resturant + "'"
        rows = c.execute(query)
        print(rows)
        for row in rows:
            r = '%d is the rating of %s ' % (row[2],resturant)
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context=None
    if ('ratings' in response['context'])and ('resturant' in response['entities'][0]['entity']) :
        rating= str(response['context']['ratings'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where publicity='" + rating + "'"
        rows = c.execute(query)
        print(rows)
        update.message.reply_text('the restaurants with %s rating'%rating)
        for row in rows:
            r = ' %s ' % (row[0])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context=None
    if ('ratings' in response['context'])and ('ratings' in response['entities'][0]['entity']) :
        rating= str(response['context']['ratings'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where publicity='" + rating + "'"
        rows = c.execute(query)
        print(rows)
        update.message.reply_text('the restaurants with %s rating'%rating)
        for row in rows:
            r = ' %s ' % (row[0])
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
