FROM python:3.8-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /home/telegram_bot

WORKDIR /home/telegram_bot
RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]
