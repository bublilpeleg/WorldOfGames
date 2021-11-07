FROM python:3.8
WORKDIR /app
COPY . /app
#RUN pip install selenium
#RUN pip install webdriver_manager
RUN pip install -r ./requirements.txt
#CMD ["/usr/local/bin/python -m pip install --upgrade pip"]
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]

