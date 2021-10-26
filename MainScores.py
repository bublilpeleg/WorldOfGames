from flask import Flask
from Utils import SCORE_FILE_NAME
from Utils import BAD_RETURN_CODE
from pathlib import Path


app = Flask(__name__)


@app.route('/')
def hello():
    scores_file = Path(SCORE_FILE_NAME)
    try:
        Current_score = int(scores_file.read_text())
        return """<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{score}</div></h1>
</body>
</html>""".format(score=Current_score)
    except ValueError:
        return """<html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">{ERROR}</div></h1>
</body>
</html""".format(ERROR=BAD_RETURN_CODE)



