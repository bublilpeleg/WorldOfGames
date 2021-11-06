from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# s=Service("/app/chromedriver_linux64/chromedriver")
# driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome(executable_path="/app/chromedriver_linux64/chromedriver")


# def test_scores_service(url):
#     driver.get(url)
#     my_url = driver.find_element_by_id("score")
#     return int(my_url) in range(1, 100)
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
    return 0 if test_scores_service("http://127.0.0.1:8777/") else -1


main_function()
