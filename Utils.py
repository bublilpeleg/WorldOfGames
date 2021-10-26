import os
SCORE_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = "Something went wrong.."


def Screen_cleaner():
    command = 'cls'
    if os.name == 'nt':
        command = 'clear'

    os.system(command)


