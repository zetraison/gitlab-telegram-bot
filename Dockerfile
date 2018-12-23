FROM python:3

WORKDIR /src

RUN pip install japronto python-telegram-bot PySocks

ADD *.py ./

CMD [ "python", "/src/gitlab-telegram-bot.py" ]