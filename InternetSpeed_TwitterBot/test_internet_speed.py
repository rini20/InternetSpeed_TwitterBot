from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Set up Chrome options
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")


class TestSpeed:

    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_option)
        self.download = 0
        self.upload = 0

    def test_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        # Wait until the page is fully loaded
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        # Wait for the 'Go' button to become clickable
        go_icon = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.start-button a span.start-text'))
        )
        go_icon.click()

        # Click the 'Continue' button
        notification_continue_button = self.driver.find_element(By.CSS_SELECTOR, '.onetrust-banner-options button')
        notification_continue_button.click()

        # Selectors for download and upload speeds
        download_element_selector = (By.CSS_SELECTOR, "span.result-data-value.download-speed")
        upload_element_selector = (By.CSS_SELECTOR, "span.result-data-value.upload-speed")
        result_id_element = (By.CSS_SELECTOR, "div.result-data")

        # Wait until the speed calculation is complete and results are displayed

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(result_id_element))
        self.download = float(self.driver.find_element(*download_element_selector).text)
        print(f"Download Speed: {self.download}")
        self.upload = float(self.driver.find_element(*upload_element_selector).text)
        print(f"Upload Speed: {self.upload}")

        self.driver.quit()


