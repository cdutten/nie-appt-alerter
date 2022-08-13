from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Main:
    def __init__(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main("http://www.python.org")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
