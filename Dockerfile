FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r ./requirements.txt
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
#CMD [ "python3", "/app/MainScores.py" ]
EXPOSE 5000
CMD ["flask", "run"]

