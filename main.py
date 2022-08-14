import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


class Main:
    def __init__(self, url):
        print("Starting...")
        # set xvfb display since there is no GUI in docker container.
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

        for i in range(2):
            print(f"Running. Attempt: {i}")
            self.check_title(url=url)
            time.sleep(30)
        self.driver.close()
        self.display.stop()
        print("Finished")

    def check_title(self, url):
        self.driver.get(url)
        print(self.driver.title)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main("https://icp.administracionelectronica.gob.es/icpplus/index.html")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
