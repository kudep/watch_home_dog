import telepot
import alarm_pygame
bot = telepot.Bot('TOKEN')
# response = bot.getUpdates()
# print(response) # chat_id
chat_id = 99999

alarm_pygame.daily_cock_alarm("01:00", lambda: bot.sendMessage(chat_id, 'ALARM: home door was opened!!!'))

