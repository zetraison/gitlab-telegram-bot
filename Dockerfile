FROM python:3

WORKDIR /src

RUN pip install python-telegram-bot
RUN pip install git+git://github.com/squeaky-pl/japronto@master#egg=japronto

ADD *.py ./

CMD [ "python", "/src/gitlab-telegram-bot.py" ]
