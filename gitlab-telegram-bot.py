import os
import sys
import json
import logging
from pprint import pformat
from telegram.ext import Updater
from japronto.app import Application
from request import Request

TELEGRAM_PROXY_HOST = os.getenv('TELEGRAM_PROXY_HOST')
TELEGRAM_PROXY_PORT = os.getenv('TELEGRAM_PROXY_PORT')
TELEGRAM_PROXY_USERNAME = os.getenv('TELEGRAM_PROXY_USERNAME')
TELEGRAM_PROXY_PASSWORD = os.getenv('TELEGRAM_PROXY_PASSWORD')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_BOT_CHAT_ID = os.getenv('TELEGRAM_BOT_CHAT_ID')
GITLAB_WEBHOOK_PORT = int(os.getenv('GITLAB_WEBHOOK_PORT'))


# Initialize logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.basicConfig(level=logging.DEBUG, format=formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


REQUEST_KWARGS={
    'proxy_url': 'socks5://{}:{}'.format(TELEGRAM_PROXY_HOST, TELEGRAM_PROXY_PORT),
    'urllib3_proxy_kwargs': {
        'username': TELEGRAM_PROXY_USERNAME,
        'password': TELEGRAM_PROXY_PASSWORD,
    }
}

# Initialize telegram bot
updater = Updater(token=TELEGRAM_BOT_TOKEN, request_kwargs=REQUEST_KWARGS)
updater.start_polling()


def construct_message(data):
    if data.object_kind == 'push':
        message = ' '.join([data.user_name, '(' + data.user_username + ')', data.event_name,
                            data.commits[0].get('url'), ':', data.commits[0].get('message')])
    else:
        message = ' '.join([data.user_name, data.event_name])

    return message


def send_message(message: str):
    updater.bot.send_message(chat_id=TELEGRAM_BOT_CHAT_ID, text=message)


def webhook_handler(request):
    try:
        request_json = request.json
    except json.JSONDecodeError as e:
        logger.error(e)
    else:
        obj = Request(request_json)
        message = construct_message(obj)
        send_message(message)

        logger.info(pformat(request_json))

        return request.Response(json=request_json)

    return request.Response(json={})


def healthcheck(request):
    return request.Response(json={'status': 'ok'})


# Initialize gitlab webhook handler
app = Application()
router = app.router
router.add_route('/webhook', webhook_handler, method='POST')
router.add_route('/healthcheck', healthcheck, method='GET')
app.run(port=GITLAB_WEBHOOK_PORT)