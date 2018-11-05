from src.larabot import LaraBot

bot_data = {
    'website': "http://example.com",
}

bot = LaraBot(bot_data)
bot.init_form("http://orod.tv/register")
