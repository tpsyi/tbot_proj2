import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
load_dotenv('vars.env')
Base = declarative_base()


CURRENCY = "UZS"        # Currency, used for payments and to describe prices
MAX_ORDERS = 30         # Maximum orders one particular person can have in db at the same time.

# DEFAULT SETTING FOR ENVIRONMENT VARIABLES, SET THEM IN vars.env!!
# Where to store log file, contains rejected  and completed orders
ORDERS_LOG = os.environ.get("ORDERS_LOG", "log/orders_log.txt")
# Default database location
DATABASE = os.environ.get("DATABASE", "sqlite:///database//tbot.db")
# Generated salt length, required for password, recommended >= 16 ; SET THE VALUE IN VARS.ENV
SALT_LENGTH = int(os.environ.get("SALT_LENGTH", 8))
# Generated key length, required for password, recommended >= 64 ; SET THE VALUE IN VARS.ENV
KEY_LENGTH = int(os.environ.get("KEY_LENGTH", 8))
# Hash iteration count; the more the better, but also the slower. Recommended >=10000 ; SET THE VALUE IN VARS.ENV
ITERATION_COUNT = int(os.environ.get("ITERATION_COUNT", 100))


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Your Telegram bot token ; SET THE VALUE IN VARS.ENV
PAYMENT_TOKEN = os.environ.get("PAYMENT_TOKEN")  # Your Payment system token ; SET THE VALUE IN VARS.ENV
