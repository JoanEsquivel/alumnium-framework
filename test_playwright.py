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
        self.al.do("add 'buy some milk' to the todo list")
        self.al.do("add 'buy some bread' to the todo list")
        self.al.do("mark all tasks complete using 'Toggle All' button")
        self.al.check("task 'buy some milk' is completed")
        self.al.check("task 'buy some bread' is completed")
        
        assert self.al.get("number of completed todos in the list") == 2