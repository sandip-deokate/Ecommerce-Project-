from importlib.metadata import metadata
from datetime import datetime

import pytest
import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.common.bidi.cdp import version
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException

download_dir = "C:\A11ty"
os.makedirs(download_dir, exist_ok=True)

@pytest.fixture()
def browser_setup(browser):
    if browser == 'edge':
        from selenium.webdriver.edge.service import Service as  EdgeServices
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        #from webdriver_manager.firefox import GeckoDriverManager
        ops = webdriver.EdgeOptions()
        preference = {"download.default_directory": download_dir,
                      "download.prompt_for_download": False,
                      "download.directory_upgrade": True,  # Allow directory upgrade
                      "safebrowsing.enabled": True,  # Enable safe browsing
                      "directory_upgrade": True,
                      "plugins.always_open_pdf_externally": True,
                      "browser.helperApps.neverAsk.saveToDisk": "application",
                      "profile.default_content_setting_values.notifications": 0,  # Block notifications
                      }
        ops.add_experimental_option("prefs", preference)
        # Arguments
        # ops.add_argument("--headless")
        ops.add_argument("--disable-features=DownloadBubble,DownloadBubbleV2")
        ops.add_argument("--safebrowsing-disable-download-protection")
        ops.add_argument("start-maximized")
        ops.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
        ops.add_argument("--disable-infobars")  # Disable infobars
        ops.add_argument("--start-maximized")  # Start maximized
        # ops.add_argument("--no-sandbox")  # Bypass OS security model
        ops.add_argument("--disable-dev-shm-usage")  #
        driver = webdriver.Edge(service=EdgeServices(EdgeChromiumDriverManager(version="129.0.2792.52").install()), options=ops)

    elif browser=='firefox':
        from selenium.webdriver.firefox.service import Service as GeckoService
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
        #Profile
        profile = FirefoxProfile()

        ops = Options()
        ops.profile = profile
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", "C:\A11ty")

        ops.binary_location = r'C:\Users\148350\AppData\Local\Mozilla Firefox\firefox.exe'

        ops.set_preference("pdfjs.disabled", True)
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()), options=ops)

    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        #extension_path = '/path/to/chrono_download_manager.crx'
        #Preferences
        ops = webdriver.ChromeOptions()
        preference= {"download.default_directory":download_dir,
                     "download.prompt_for_download": False,
                     "download.directory_upgrade": True,  # Allow directory upgrade
                     "safebrowsing.enabled": True,  # Enable safe browsing
                     "profile.default_content_setting_values.notifications": 0,
                     "plugins.always_open_pdf_externally":True# Block notifications
                      }
        ops.add_experimental_option("prefs",preference)
        #ops.add_extension(extension_path)
        #Arguments
        #ops.add_argument("--headless")
        ops.add_argument("--disable-features=DownloadBubble,DownloadBubbleV2")
        ops.add_argument("--safebrowsing-disable-download-protection")
        ops.add_argument("start-maximized")
        ops.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
        ops.add_argument("--disable-infobars")  # Disable infobars
        ops.add_argument("--start-maximized")  # Start maximized
        #ops.add_argument("--no-sandbox")  # Bypass OS security model
        ops.add_argument("--disable-dev-shm-usage")  #
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ops)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###############  HTML Reports ############

# It's hook for adding Environment info to HTML
def pytest_configure(config):
    config._metadata['Project Name']='Ecommerce'
    config._metadata['Module Name']='Account Registration'
    config._metadata['Tester']='sandip'

# It's optional hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVAHOME",None)
    metadata.pop("Plugin", None)

@pytest.hookimpl(tryfirst= True)
def pytest_configure(config):
    config.option.htmlpath =(os.path.abspath(os.curdir)+"\\reports\\"+
                             datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html")


#


