from Utils import SCORE_FILE_NAME
from pathlib import Path


def add_score(difficulty):
    scores_file = Path(SCORE_FILE_NAME)
    try:
        Current_score = int(scores_file.read_text())
    except:
        Current_score = 0
    Current_score = Current_score + (difficulty * 3) + 5
    scores_file.write_text(repr(Current_score))
