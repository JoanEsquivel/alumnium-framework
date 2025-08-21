import unittest
from playwright.sync_api import sync_playwright
from alumnium import Alumni
from dotenv import load_dotenv

load_dotenv()


# Run with:
# python -m unittest test_playwright.py

class TestSearch(unittest.TestCase):

    def setUp(self):
        page = sync_playwright().start().chromium.launch(headless=False).new_page()
        page.goto("https://todomvc.com/examples/vue/dist/#/")
        self.al = Alumni(page)

    def test_complete_all_todos(self):
        self.al.do("type 'buy some milk' into the input field, then press 'Enter'")
        self.al.do("type 'buy some bread' into the input field, then press 'Enter'")
        self.al.do("mark all tasks complete")
        self.al.check("buy some milk' title font style is strikethrough", vision=True)
        self.al.check("buy some bread' title font style is strikethrough", vision=True)