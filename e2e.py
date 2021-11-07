from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# from selenium.webdriver.chrome.service import Service
#
# s=Service("/app/chromedriver_linux64/chromedriver")
# driver = webdriver.Chrome(service=s)

# my_driver = webdriver.Chrome(executable_path="/chromedriver_linux64/chromedriver")


# def test_scores_service(url):
#     driver.get(url)
#     my_url = driver.find_element_by_id("score")
#     return int(my_url) in range(1, 100)
def test_scores_service():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    my_driver = webdriver.Chrome('/app/chromedriver_linux64/chromedriver', options=chrome_options)
    # driver.get('http://www.google.com')
    print('test')
    # s = Service(ChromeDriverManager().install())
    # svc = Service("/app/chromedriver_linux64/chromedriver")
    # my_driver = webdriver.Chrome(service=s)
    # my_driver.maximize_window()
    my_driver.get("http://127.0.0.1:8777/")
    score = my_driver.find_element(By.ID, "score").text
    if 1 < int(score) < 1000:
        return True
    else:
        return False


def main_function():
    return 0 if test_scores_service() else -1


main_function()
