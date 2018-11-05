from src.larabot import LaraBot

bot_data = {
    'website': "http://example.com",
}

bot = LaraBot(bot_data)
bot.write_log("test logging")
