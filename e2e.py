from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="/app/chromedriver_linux64/chromedriver")


def test_scores_service(url):
    driver.get(url)
    my_url = driver.find_element_by_id('score')
    if my_url > 100:
        return True
    else:
        return False


def main_function():
    return 0 if test_scores_service("peleg") else -1
