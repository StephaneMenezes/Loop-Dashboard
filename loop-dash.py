from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

class BrowserHandler:
    def __init__(self, dashboard_url):
        self.dashboard_url = dashboard_url

    def start_browser(self, kiosk=True):
        chrome_options = Options()
        if kiosk:
            chrome_options.add_argument("--kiosk")
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_dashboard(self):
        self.driver.get(self.dashboard_url)

    def loop_refresh(self, update_every, how_long_to_stay):
        while True:
            self.driver.refresh()
            time.sleep(update_every)
            self.driver.refresh()
            time.sleep(how_long_to_stay)

# Exemplo de uso
dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiNDc5NTRhMWMtOWY5Yy00YjhhLWE5MTQtZTM1NjljYTU5NzQwIiwidCI6ImI1OTFhZTU0LTMzYzItNDU4OS1iZTY2LTkwMjFhNDE5NmM3YyJ9"
update_every = 180  # Atualizar a cada 180 segundos (3 minutos)
how_long_to_stay = 60  # Permanecer no dashboard por 60 segundos

browser_handler = BrowserHandler(dashboard_url)
browser_handler.start_browser()
browser_handler.open_dashboard()
browser_handler.loop_refresh(update_every, how_long_to_stay)

