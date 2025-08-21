import os
from dotenv import load_dotenv
from alumnium import Alumni
from selenium.webdriver import Chrome

load_dotenv()

driver = Chrome()
driver.get("https://www.joanmedia.dev/")

al = Alumni(driver)
al.do("click on 'conferences'")
al.check("conference list contain PyCon US 2025 - Automated E2E testing with Playwright and Python")
conferences = al.get('list of conferences')
print(conferences)
