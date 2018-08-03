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
    if len(resp) > 0:
        update.message.reply_text(resp)
    # extraxt context


    if 'cuisine' in response['context']:
        cuisine = str(response['context']['cuisine'])
        print(cuisine)
        # retrieve data in database
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where cuisine='" + cuisine + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%s is a  restaraunt that has %s cuisine with rating %d with timings %d am to %d pm' % (
            row[0], row[1], row[2], row[3], row[4])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None

    if (('item' in response['intents'][0]['intent']) and ('root' in response['context']['system']['dialog_stack'][0]['dialog_node'])):
        fooditem = str(response['context']['itemname'])
        print(fooditem)
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select rest from food1 where item='" + fooditem + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%s' % row[0]
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None

    if ('resturant' in response['context']) and ('Rest_name' in response['intents'][0]['intent']) and ('root' in response['context']['system']['dialog_stack'][0]['dialog_node']):
        resturant = str(response['context']['resturant'])
        if resturant == '1947':
            update.message.reply_text(
                "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/5/r/n/p5052-14613188305719f4aeb70e5.jpg?w=1200")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9021139,77.5178936/1947+Indian+Restaurant,+No.+292%2FA,+12th+Cross,+Ideal+Home+Township,+Rajarajeshwari+Nagar,+Bengaluru,+Karnataka+560098/@12.9135372,77.5079008,15z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3e56259efa27:0x423342fa79f44707!2m2!1d77.5162398!2d12.9260798!3e0")

        elif resturant == 'alphas':
            update.message.reply_text("http://images.notquitenigella.com/images/alpha/__alpha-restaurant-1.jpg")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9021214,77.518066/RNS+Institute+of+Technology,+Dr.+Vishnuvardhana+Road,R+R+Nagar+Post,+Channasandra,+Bengaluru,+Karnataka+560098/@12.9025245,77.5164309,17z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3fa7243af9c3:0x9bed6669a38d1c3!2m2!1d77.518582!2d12.9021902!3e0")
        elif resturant == 'amande':
            update.message.reply_text(
                "http://www.lifestylebrno.cz/wp-content/uploads/2018/01/nahled-1200px-_MG_5907-600x400.jpg")
            update.message.reply_text("https://www.google.com/maps/dir/12.9075373,77.5405867/Amand%C3%A9+Patisserie,+UB+City,+2nd+Floor,+24+Vittal+Mallya+Road,+KG+Halli,+D+Souza+Layout,+Sampangi+Rama+Nagar,+KG+Halli,+D'+Souza+Layout,+Ashok+Nagar,+Bengaluru,+Karnataka+560001/@12.9390628,77.5341141,13z/data=!3m1!4b1!4m16!1m6!3m5!1s0x3bae16775b93ba2d:0x1dfc5ece035b49c2!2sAmand%C3%A9+Patisserie!8m2!3d12.971854!4d77.5962681!4m8!1m1!4e1!1m5!1m1!1s0x3bae16775b93ba2d:0x1dfc5ece035b49c2!2m2!1d77.5962681!2d12.971854")

        elif resturant == 'ambrosia':
            update.message.reply_text(
                "https://media-cdn.tripadvisor.com/media/photo-s/03/d6/ee/da/ambrosia-restaurant.jpg")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Ambrosia,+15%2F3A,+Ganakal,+Srinivaspura,+Noojibail+Nursery+Compound,+Dr+Vishnuvardhan+Road,+Bengaluru,+Karnataka+560060/@12.911609,77.489522,13z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3f0f26de751f:0xa976f3d6b4dae110!2m2!1d77.509326!2d12.904113!3e0")

        elif resturant == 'cafe noir':
            update.message.reply_text(
                "https://i2.wp.com/media.hungryforever.com/wp-content/uploads/2016/10/05163523/fun-in-bangalore-cafe-noir.jpg?ssl=1?w=356&strip=all&quality=80")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9021437,77.5181176/Cafe+Noir,+UB+City,+Unit+No+206,+The+Collection,+No+24,+Vittal+Mallya+Rd,+Bengaluru,+Karnataka+560001/@12.9270741,77.4795432,12z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae1677673c026d:0x63ecec8574add020!2m2!1d77.596098!2d12.9717691!3e0")

        elif resturant == 'cheffu n steffu':
            update.message.reply_text(
                "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/2/h/d/p20311-1501326153597c6b4935956.jpg?w=1200&q=100")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9021284,77.5181345/Cheffu+N+Stuffu,+1,+12th+Cross+Rd,+Remco+Bhel+Layout,+Ideal+Homes+Twp,+RR+Nagar,+Bengaluru,+Karnataka+560098/@12.9143196,77.5079008,15z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3ef88ee91e19:0x455d4a66dd12dd6d!2m2!1d77.514922!2d12.926511!3e0")

        elif resturant == 'communiti':
            update.message.reply_text("https://media-cdn.tripadvisor.com/media/photo-s/0e/5b/2f/93/front-elevation.jpg")
            update.message.reply_text("https://www.google.com/maps/dir/12.9075373,77.5405867/Communiti+Pub,+Ashok+Nagar,+Bengaluru,+Karnataka/@12.9390912,77.5392831,13z/data=!3m2!4b1!5s0x3bae16775b3b1d3d:0x5ce03bb2785b2a10!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bae168715000011:0xa532c0481a45059d!2m2!1d77.6080186!2d12.9723464")

        elif resturant == 'cream byte':
            update.message.reply_text(
                "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/3/l/p/p38177-15202269685a9cd29892763.jpg?w=1200")
            update.message.reply_text("https://www.google.com/maps/dir/12.9075373,77.5405867/Cream+Byte+Indo+Italian+Cafe.,+BEML+Layout,+RR+Nagar,+Bengaluru,+Karnataka/@12.90995,77.521781,15z/data=!3m2!4b1!5s0x3bae16775b3b1d3d:0x5ce03bb2785b2a10!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bae3e5357e2d917:0xe45b0a105978b2bc!2m2!1d77.5204231!2d12.9170654")

        elif resturant == 'dejavu':
            update.message.reply_text(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReLVES2dUUfDt-a_UI5xFGa3nW8p1kPfjNVeMwqCl9oqigMAJC6A")
            update.message.reply_text("https://www.google.com/maps/dir/12.9075373,77.5405867/Deja+Vu+Restaurant,+3rd+Phase,+JP+Nagar,+Bengaluru,+Karnataka/@12.9117648,77.5352949,13z/data=!3m2!4b1!5s0x3bae16775b3b1d3d:0x5ce03bb2785b2a10!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bae15045487d37d:0x6c1599eca5944d0e!2m2!1d77.5995362!2d12.9140622")

        elif resturant == 'echo':
            update.message.reply_text(
                "https://im1.dineout.co.in/images/uploads/restaurant/sharpen/3/v/l/p31070-1494998747591bdedb0968c.jpg?w=1200")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Echoes,+44,+4th+B+Cross+Road,+5th+Block,+Koramangala+Industrial+Layout,+Koramangala,+Bengaluru,+Karnataka+560034/@12.9386592,77.5458951,13z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae1451d70c70f9:0xe3e44fad44d74b50!2m2!1d77.6156238!2d12.9339701!3e0")

        elif resturant == 'fab cafe':
            update.message.reply_text(
                "https://content3.jdmagicbox.com/comp/bangalore/k2/080pxx80.xx80.160201193748.c8k2/catalogue/fab-cafe-rajarajeshwari-nagar-bangalore-restaurants-p3ei54.jpg")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Fab+Cafe,+915,+Kenchena+Halli+Road,+Remco+Bhel+Layout,+Kenchenhalli,+RR+Nagar,+Bengaluru,+Karnataka+560098/@12.9418582,77.5138932,14z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3e58bee99c5f:0x410ec542edf8ae2!2m2!1d77.5173607!2d12.9340754!3e0")

        elif resturant == 'kappi katti':
            update.message.reply_text(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTbDPOM5p-nnzhUMibwdU6lK9Uf_m5rQ2x0c_s9fc_BVQGE_g-1g")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Kaapi+Katte,+BEML+Layout,+RR+Nagar,+Bengaluru,+Karnataka+560098/@12.9299278,77.5149526,14z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3fab6da331cd:0xeb1b95106a577c8!2m2!1d77.52067!2d12.9163444!3e0")

        elif resturant == 'krishna grand':
            update.message.reply_text("https://www.partyone.in/suploads/2017/Mar/08/19034/1488952369413%20krish.JPG")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9021285,77.5180799/The+Krishna+Grand,+25%2F1,+27th+Cross+Rd,+Banashankari+Stage+II,+Banashankari,+Bengaluru,+Karnataka+560070/@12.900769,77.5111673,13z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae1582845721f7:0x1c2358159550bec0!2m2!1d77.5710312!2d12.9214165!3e0")

        elif resturant == 'mint masala':
            update.message.reply_text("https://media-cdn.tripadvisor.com/media/photo-s/0f/ec/d0/c3/photo0jpg.jpg")
            update.message.reply_text("https://www.google.com/maps/dir//Mint+Masala,+147+Infantry+Road,+Opposite+to+Police+Commissioner+Office,+Bengaluru,+Karnataka+560001/data=!4m7!4m6!1m1!4e2!1m2!1m1!1s0x3bae166f2997e8af:0xd735ac59bc31c8d3!3e0")

        elif resturant == 'nandhana palace':
            update.message.reply_text("https://pbs.twimg.com/profile_images/1902744860/nandhanagroup_logo.jpg")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Nandhana+Palace-Andhra+Style+Restaurant-RR+Nagar,+%23162,+Channasandra+Road,+BEML+Layout,+Opp+SBI+Bank,+5th+Stage,+RR+Nagar,+Bengaluru,+Karnataka+560098/@12.9196883,77.5157505,14z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3fa664c8be2b:0x6f13795981820b0!2m2!1d77.5212677!2d12.9049324!3e0")

        elif resturant == 'onesta':
           update.message.reply_text("http://s3.india.com/travel/wp-content/uploads/2015/12/03travel-onesta.jpg")
           update.message.reply_text("https://www.google.com/maps/dir/12.9860162,77.5552047/Onesta,+4th+Block,+562,+8th+Main+Rd,+Koramangala+4th+Block,+Koramangala,+Bengaluru,+Karnataka+560034/@12.9573175,77.5560994,13z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae145ce69b779b:0x2d1c77f1c559698d!2m2!1d77.6270347!2d12.9336765!3e0")
        elif resturant == 'pakaashala':
            update.message.reply_text("https://paakashalarestaurant.com/wp-content/uploads/2014/12/Restaurant-8.jpg")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Paakashala+Restaurant,+335,+1st+Floor,+Ideal+Home+Township,+Phase+1,+Sector+-+B,+Opp+Bata+Showroom,+Rajarajeshwari+Nagar,+Remco+Bhel+Layout,+Javarandoddi,+Bengaluru,+Karnataka+560098/@12.9396596,77.5126905,14z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae3ef7f2f8e5fb:0xc1bf30dd092ebfa3!2m2!1d77.5149054!2d12.9300544!3e0")


        elif resturant == 'prost':
            update.message.reply_text(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR46dUhUaOPsblLVlYjxebyL7zVjA7QMDO7KYWmd4fF_ynuuJpBVQ")
            update.message.reply_text("https://www.google.co.in/maps/dir/12.9365451,77.5447454/Prost,+749,+10th+Main,+80+Feet+Road,+4th+Block,+Near+Maharaja+Hotel,+Koramangala,+Bengaluru,+Karnataka+560035/@12.9377126,77.5187183,12z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae14678835bbc1:0x2184ee852f45232c!2m2!1d77.6307065!2d12.933118!3e0")

        elif resturant == 'royal andhra spice':
            update.message.reply_text(
                "https://content3.jdmagicbox.com/comp/bangalore/r6/080pxx80.xx80.110324130432.b8r6/catalogue/royal-andhra-spice-restaurant-rajarajeshwari-nagar-bangalore-andhra-restaurants-5y0wm.jpg")
            update.message.reply_text("https://www.google.com/maps/dir//Royal+Andhra+Spice,+60+Feet+Rd,+Near-BMTC+Depot,+BEML+Layout,+5th+Stage,+RR+Nagar,+Bengaluru,+Karnataka+560098/data=!4m7!4m6!1m1!4e2!1m2!1m1!1s0x3bae3fa612b1de91:0xd5778d1521b294d7!3e0")

        elif resturant == 'stories':
            update.message.reply_text("https://metrosaga.com/wp-content/uploads/2017/10/6-7-1024x536.jpg")
            update.message.reply_text("https://www.google.com/maps/dir/12.9236992,77.5815168/Stories,+N-15,+3rd+Floor,+24th+Main+Road,+JP+Nagar,+1st+Phase,+Above+RBL+Bank,+Opp+Cakewala,+Bengaluru,+Karnataka+560078/@12.9186356,77.5793752,16z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae150cda6a5fc9:0x178839167032eee9!2m2!1d77.585519!2d12.913572!3e0")

        elif resturant == 'the vintage':
            update.message.reply_text(
                "https://media.gobymobile.com/mediaresources/restaurant/5229/tagmedia/354a89a0-3dc4-4eb7-8f06-108ec69af08d.jpg")
            update.message.reply_text("https://www.google.com/maps/place/The+Vintage+Cafe/@12.9301834,77.5468135,15z/data=!4m2!3m1!1s0x0:0x1161650a5dfb41aa?sa=X&ved=2ahUKEwiA5I3__cjcAhUMTn0KHXU9AMsQ_BIwD3oECAoQCw")

        elif resturant == 'truffles':
            update.message.reply_text(
                "https://dontgetserious.com/wp-content/uploads/2017/05/truffles-cafe-bangalore.png")
            update.message.reply_text("https://www.google.com/maps/dir/12.9236992,77.5815168/Stories,+N-15,+3rd+Floor,+24th+Main+Road,+JP+Nagar,+1st+Phase,+Above+RBL+Bank,+Opp+Cakewala,+Bengaluru,+Karnataka+560078/@12.9186356,77.5793752,16z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x3bae150cda6a5fc9:0x178839167032eee9!2m2!1d77.585519!2d12.913572!3e0")


        elif resturant == 'woodlands':
            update.message.reply_text(
                "https://static1.squarespace.com/static/56e03252ab48ded0e100ec12/t/56e050580c4a689277e6692d/1457541208037/1000w/")
            update.message.reply_text("https://www.google.com/maps/dir/''/WoodLand,+Shop+No.+44,45,+Opposite+Pizza+Corner,+Brigade+Road,+Shanthala+Nagar,+Ashok+Nagar,+Bengaluru,+Karnataka+560001/data=!4m5!4m4!1m0!1m2!1m1!1s0x3bae167dfe7700f7:0xd13a75bce9d031a7?sa=X&ved=0ahUKEwiw6sSDxcjcAhUJtY8KHe0ZBBcQiBMILDAA")


        # retrieve data in database
        print('++++++++++++++++++++++++++++++', response['intents'][0]['intent'], '+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        update.message.reply_text("menu:")
        query = "select * from food1 where rest='" + resturant + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%s is a %s option from %s priced at %d'%(row[1], row[3], row[0], row[2])
            r = r.capitalize()
            update.message.reply_text(r)

        conn.commit()
        conn.close()
        context = None

    if ('resturant' in response['context']) and ('popularity' in response['intents'][0]['intent']) and ('root' in response['context']['system']['dialog_stack'][0]['dialog_node']):
        resturant = str(response['context']['resturant'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++', response['intents'][0]['intent'], '+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where name='" + resturant + "'"
        rows = c.execute(query)
        for row in rows:
            r = '%d is the rating of %s ' % (row[2], resturant)
            r = r.capitalize()
            update.message.reply_text(r)
            conn.commit()
            conn.close()
            context = None

    if ('ratings' in response['context']) and ('resturant' in response['entities'][0]['entity']) and ('root' in response['context']['system']['dialog_stack'][0]['dialog_node']):
        rating=str(response['context'])
        # retrieve data in database
        print('++++++++++++++++++++++++++++++', response['intents'][0]['intent'], '+++++++++++++++++++++++++++s')
        conn = sqlite3.connect('pro1.db')
        c = conn.cursor()
        query = "select * from rest where publicity='" + rating + "'"
        rows = c.execute(query)

        update.message.reply_text('the restaurants with %s rating' % rating)
        for row in rows:
            r = ' %s ' % (row[0])
            r = r.capitalize()
            update.message.reply_text(r)
        conn.commit()
        conn.close()
        context = None

    if ('area' in response['context'])and ('root' in response['context']['system']['dialog_stack'][0]['dialog_node']):
        area = str(response['context']['area'])
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


    if (('resturant' in response['context']) and ('itemname' in response['context']) and ('quantity' in response['context'])):
        print("okay")
        conn=sqlite3.connect('pro1.db')
        c=conn.cursor()
        resturant = str(response['context']['resturant'])
        fooditem = str(response['context']['itemname'])
        quantity= (response['context']['quantity'])
        query1="select price from food1 where rest='"+resturant+ "'and item='"+fooditem+"'"
        print('price retrieved')
        rows=c.execute(query1)
        for row in rows:
            row1=row[0]
        row2=row1*quantity
        d=list()
        d = [resturant,fooditem,quantity,row1,row2]
        print(d)
        c.execute("INSERT INTO orders (rest,item,quantity,price,amount) values (?1,?2,?3,?4,?5)", (d[0], d[1], d[2], d[3], d[4]))
        conn.commit()
        conn.close()
        context=None
    if('terminate' in response['intents'][0]['intent']):
        conn=sqlite3.connect('pro1.db')
        c=conn.cursor()
        s=0
        print('no')
        query="select * from orders"
        rows=c.execute(query)
        for row in rows:
            r=None
            r='Restaurant:{}\nItemname:{}\nQuantity:{}\nPrice:{}\nAmount:{}'.format(row[0],row[1],row[2],row[3],row[4])
            print(r)
            update.message.reply_text(r)
            s+=row[4]
        t='TOTAL AMOUNT=%d'%s
        update.message.reply_text(t)
        c.execute("delete from orders")
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
