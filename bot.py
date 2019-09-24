import telebot
bot = telebot.TeleBot('916099039:AAFYJZr93eHu0LuUHDfbFLWQO-kK_1uy-28')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет,ублюдок,пока что ты можешь посмотреть расписание,просто введи "расписание"')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'расписание':
        bot.send_message(message.chat.id, 'Понедельник : Математика,Захист,Физика\nВторник: География,История,Информатика\nСреда: Физкультура,Английский язык,Украинский язык\nЧетверг: Економика,История,Физика\nПятница: Биолигия,Украинская лит-ра,Зар. лит-ра')
    elif message.text == 'Расписание':
        bot.send_message(message.chat.id, 'Понедельник : Математика,Захист,Физика\nВторник: География,История,Информатика\nСреда: Физкультура,Английский язык,Украинский язык\nЧетверг: Економика,История,Физика\nПятница: Биолигия,Украинская лит-ра,Зар. лит-ра")')
    else :
        bot.send_message(message.chat.id, 'Сам понял что высрал?(пока что доступна только команда "расписание")')
bot.polling()
