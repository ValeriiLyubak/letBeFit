from selenium import webdriver


class BrowserFactory:
    def __init__(self, browser_name):
        self.browser_name = browser_name.lower()

    def get_driver(self):
        if self.browser_name == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
            chrome_options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(options=chrome_options)

        elif self.browser_name == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference("geo.enabled", False)
            driver = webdriver.Firefox(options=firefox_options)

        elif self.browser_name == "edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--disable-notifications")
            driver = webdriver.Edge(options=edge_options)

        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

        driver.maximize_window()
        return driver

