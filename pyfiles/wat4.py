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
             r='%s is a  restaraunt that has %s cuisine with rating %d with timings %d am to %d pm'%(row[0],row[1], row[2], row[3],row[4])
             r=r.capitalize()
             update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None

    if 'itemname' in response['context']:
        fooditem=str(response['context']['itemname'])
        print(fooditem)
        conn=sqlite3.connect('pro1.db')
        c=conn.cursor()
        query="select rest from food1 where item='"+ fooditem+"'"
        rows=c.execute(query)
        for row in rows:
            r='%s' %row[0]
            r=r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None



    if ('resturant' in response['context']) and ('Rest_name' in response['intents'][0]['intent']) :
        resturant = str(response['context']['resturant'])
        if resturant == '1947':
            update.message.reply_text("https://im1.dineout.co.in/images/uploads/restaurant/sharpen/5/r/n/p5052-14613188305719f4aeb70e5.jpg?w=1200")
        elif resturant  == 'alphas':
            update.message.reply_text("http://images.notquitenigella.com/images/alpha/__alpha-restaurant-1.jpg")
        elif resturant =='amande':
            update.message.reply_text("http://www.lifestylebrno.cz/wp-content/uploads/2018/01/nahled-1200px-_MG_5907-600x400.jpg")
        elif resturant =='ambrosia':
            update.message.reply_text("https://media-cdn.tripadvisor.com/media/photo-s/03/d6/ee/da/ambrosia-restaurant.jpg")
        elif resturant =='cafe noir':
            update.message.reply_text("https://i2.wp.com/media.hungryforever.com/wp-content/uploads/2016/10/05163523/fun-in-bangalore-cafe-noir.jpg?ssl=1?w=356&strip=all&quality=80")
        elif resturant =='cheffu n steffu':
            update.message.reply_text("https://im1.dineout.co.in/images/uploads/restaurant/sharpen/2/h/d/p20311-1501326153597c6b4935956.jpg?w=1200&q=100")
        elif resturant =='communiti':
            update.message.reply_text("https://media-cdn.tripadvisor.com/media/photo-s/0e/5b/2f/93/front-elevation.jpg")
        elif resturant =='cream byte':
            update.message.reply_text("https://im1.dineout.co.in/images/uploads/restaurant/sharpen/3/l/p/p38177-15202269685a9cd29892763.jpg?w=1200")
        elif resturant =='dejavu':
            update.message.reply_text("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReLVES2dUUfDt-a_UI5xFGa3nW8p1kPfjNVeMwqCl9oqigMAJC6A")
        elif resturant =='echo':
            update.message.reply_text("https://im1.dineout.co.in/images/uploads/restaurant/sharpen/3/v/l/p31070-1494998747591bdedb0968c.jpg?w=1200")
        elif resturant =='fab cafe':
            update.message.reply_text("https://content3.jdmagicbox.com/comp/bangalore/k2/080pxx80.xx80.160201193748.c8k2/catalogue/fab-cafe-rajarajeshwari-nagar-bangalore-restaurants-p3ei54.jpg")
        elif resturant =='kappi katti':
            update.message.reply_text("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTbDPOM5p-nnzhUMibwdU6lK9Uf_m5rQ2x0c_s9fc_BVQGE_g-1g")
        elif resturant =='krishna grand':
            update.message.reply_text("https://www.partyone.in/suploads/2017/Mar/08/19034/1488952369413%20krish.JPG")
        elif resturant =='mint masala':
            update.message.reply_text("https://media-cdn.tripadvisor.com/media/photo-s/0f/ec/d0/c3/photo0jpg.jpg")
        elif resturant =='nandhana palace':
            update.message.reply_text("https://pbs.twimg.com/profile_images/1902744860/nandhanagroup_logo.jpg")
        elif resturant =='onesta':
            update.message.reply_text("http://s3.india.com/travel/wp-content/uploads/2015/12/03travel-onesta.jpg")
        elif resturant =='pakaashala':
            update.message.reply_text("https://paakashalarestaurant.com/wp-content/uploads/2014/12/Restaurant-8.jpg")
        elif resturant =='prost':
            update.message.reply_text("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR46dUhUaOPsblLVlYjxebyL7zVjA7QMDO7KYWmd4fF_ynuuJpBVQ")
        elif resturant =='royal andhra spice':
            update.message.reply_text("https://content3.jdmagicbox.com/comp/bangalore/r6/080pxx80.xx80.110324130432.b8r6/catalogue/royal-andhra-spice-restaurant-rajarajeshwari-nagar-bangalore-andhra-restaurants-5y0wm.jpg")
        elif resturant =='stories':
            update.message.reply_text("https://metrosaga.com/wp-content/uploads/2017/10/6-7-1024x536.jpg")
        elif resturant =='the vintage':
            update.message.reply_text("https://media.gobymobile.com/mediaresources/restaurant/5229/tagmedia/354a89a0-3dc4-4eb7-8f06-108ec69af08d.jpg")
        elif resturant =='truffles':
            update.message.reply_text("https://dontgetserious.com/wp-content/uploads/2017/05/truffles-cafe-bangalore.png")
        elif resturant =='woodlands':
            update.message.reply_text("https://static1.squarespace.com/static/56e03252ab48ded0e100ec12/t/56e050580c4a689277e6692d/1457541208037/1000w/")
         # retrieve data in database
        print('++++++++++++++++++++++++++++++', response['intents'][0]['intent'], '+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from food1 where rest='" + resturant + "'"
        rows=c.execute(query)
        update.message.reply_text("menu:")
        for row in rows:
            r = '%s is a %s option from %s priced at %d' % (row[1], row[3], row[0], row[2])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None


    if ('resturant' in response['context'])and ('popularity' in response['intents'][0]['intent']) :
        resturant = str(response['context']['resturant'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where name='" + resturant + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%d is the rating of %s ' % (row[2],resturant)
            r = r.capitalize()
            update.message.reply_text(r)
            conn.commit()
            conn.close()
            context = None



    if ('ratings' in response['context'])and ('resturant' in response['entities'][0]['entity']) :
        rating= str(response['context']['ratings'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++',response['intents'][0]['intent'],'+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where publicity='" + rating + "'"
        rows = c.execute(query)

        update.message.reply_text('the restaurants with %s rating'%rating)
        for row in rows:
            r = ' %s ' % (row[0])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None


    if('area' in response['context']):
        area=str(response['context']['area'])
        # retrieve data in database
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where loc='" + area + "'"
        rows = c.execute(query)

        update.message.reply_text('the restaurants near %s' % area)
        for row in rows:
            r = ' %s ' % (row[0])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None



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
