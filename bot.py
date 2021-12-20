from classes.main import Main
from classes.auth import Auth
from dotenv import load_dotenv
import os

load_dotenv()

BOT_NAME = os.getenv('Tiger_Inu_Referral_Bot')
COUNT = os.getenv('16')
REFER_ID = os.getenv('REFER_ID')
DELAY_MIN = os.getenv('DELAY_MIN')
DELAY_MAX = os.getenv('DELAY_MAX')
AUTH = os.getenv('AUTH')
RUN = os.getenv('RUN')


bot = Main(BOT_NAME, COUNT, DELAY_MIN, DELAY_MAX, REFER_ID)
auth = Auth()
if (int(AUTH) != 0):
    auth.start()
if (int(RUN) != 0):
    bot.start()
    print("Done")
