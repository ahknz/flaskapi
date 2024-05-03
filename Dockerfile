FROM python:3

WORKDIR /python-docker

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY .  .

ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]