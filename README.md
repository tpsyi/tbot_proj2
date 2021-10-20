# tbot_proj2
University project, telegram bot for ordering meals.

To setup this project:
1) install packages: \
  `pip install python-telegram-bot, python-telegram-bot-pagination, sqlalchemy, python-dotenv`
2) create **vars.env** file at root directory and type in: \
`     TELEGRAM_TOKEN = [Bot token]`\
`     DATABASE = "sqlite:///database//tbot.db"`
`     PAYMENT_TOKEN = [Payment api token]`\
`     SALT_LENGTH = [salt length, required for password, recommended >= 16]`\
`     KEY_LENGTH = [Generated key length, required for password, recommended >= 64]`\
`     ITERATION_COUNT = [Hash iteration count; the more the better, but also the slower. Recommended >=10000]`
3) change less significant values in config.py. Their meaning is documented to the best of my abilities.
Keep in mind that variables in **vars.env** will take precedence over those in config.
4) change **localizations/en.py, ru.py** to your liking. Change **names/used_names.py** to suit your needs.
5) put your images in **assets/meals**, put your meals in **ins_meals.py**. \
6) **run main.py**
