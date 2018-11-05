from src.larabot import LaraBot

bot_data = {
    'website': "http://example.tv",
}

register_data = {
    "city_id": "1",
    "email": "test@gmail.com",
    "password": "password",
    "mobile": "09120000000",
    "name": "Ali Sharifi Neyestani",
    "password_confirmation": "password",
    "reagant_code": "25",
    "type_id": "3"
}



bot = LaraBot(bot_data)
bot.register(register_data)
