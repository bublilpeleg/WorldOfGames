FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install selenium
RUN pip install -r ./requirements.txt
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]

