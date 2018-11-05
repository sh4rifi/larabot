from src.larabot import LaraBot

bot_data = {
    'website': "http://orod.tv",
}

register_data = {
    "city_id": "1",
    "email": "A_2@gmail.com",
    "password": "password",
    "mobile": "0912000020",
    "name": "Ali Sharifi Neyestani",
    "password_confirmation": "password",
    "reagant_code": "25",
    "type_id": "3"
}


bot = LaraBot(bot_data)
# bot.register(register_data)


login_data = {
    'email': 'sh4rifi@orod.com',
    'password': 'password',
}


bot.login(login_data, login_patch="/admin/login")


