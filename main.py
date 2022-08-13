from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


class Main:
    def __init__(self, url):
        # set xvfb display since there is no GUI in docker container.
        display = Display(visible=0, size=(800, 600))
        display.start()

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
        display.stop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main("http://www.python.org")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
