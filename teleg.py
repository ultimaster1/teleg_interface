from telegram import Bot
from telegram.ext import Filters, MessageHandler
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Updater, CommandHandler
import pandas as pd
bot = Bot(token='821621757:AAEvO3dWJ5XWxMM2y2OorZscnWPYnSOlkZY')
def put(update,contenxt):
    print('sdsdsdsd')
    par_string = 'Params:'
    value = update.message.text.partition(' ')[2]
    if par_string in value:
        values = value.split('Params: ')
        values_array = values[1].split(';')
        if (len(values_array) != 7):
            bot.sendMessage(chat_id=update.message.chat_id, text="Неверное число параметров")
            print('error')
        else:
            pd.options.display.max_columns = 7
            old_data = pd.read_csv('Params.csv',index_col=None)
            df = pd.DataFrame(columns = values_array)
            print(df)
            #df.to_csv('Params.csv', index=False)
            #con = pd.merge(old_data,df, how='outer')
            con = pd.concat([old_data,df],axis= 1)
            con.to_csv('Params.csv', index=False)
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Используйте ключевое слово Params:, для получения более подробной информации введите команду /help")
def start(update,context):
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте, добро пожаловать в торгового бота от компании хз. Данный бот предназначен для хз.\n"
                                                         "Для ввода параметров торговоли бота используйте команду /put, а затем ключевое слово Params:. Для получения более "
                                                         "подробной информации воспользуйтесь командой /help.")
def help(update,context):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Для ввода параметров используйте команду "/put" и ключевое слово "Params:",затем вводите параметры через точку с запятой как показано на примере \n '
                         '"/put Params: ETH/BTC; ETHBTC; 3.1; 3.14; 1.2; 40; 0.95". Пожалуйста вводите 7 параметров, подробное описание параметров вы можете увидеть ниже:\n'
                         '1.Symbol_bitqi(строка) - хз\n'
                         '2.Symbol_binance(строка) - хз\n'
                         '3.Log_base(число с плавающей точкой) - хз\n'
                         '4.Pi(число с плавающей точкой) - хз\n'
                         '5.Max_sleep(число с плавающей точкой) - хз\n'
                         '6.Stored_range(целое число) - хз\n'
                         '7.Sps_border(число с плавающей точкой) - хз\n' )
if __name__ == '__main__':
    updater = Updater('821621757:AAEvO3dWJ5XWxMM2y2OorZscnWPYnSOlkZY', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('put', put))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
