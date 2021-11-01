from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="/app/chromedriver_linux64/chromedriver")


def test_scores_service(url):
    driver.get(url)
    my_url = driver.find_element_by_id("score")
    return int(my_url) in range(1, 100)


def main_function():
    return 0 if test_scores_service("http://127.0.0.1:8777/") else -1


main_function()
