from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_scores_service():
    svc = Service(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=svc)
    my_driver.maximize_window()
    my_driver.get("http://127.0.0.1:8777/")
    score = my_driver.find_element(By.ID, "score").text
    if 1 < int(score) < 1000:
        return True
    else:
        return False


def main_function():
    test_score = test_scores_service()
    if test_score:
        exit(0)
    else:
        exit(-1)


main_function()
