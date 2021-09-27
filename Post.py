from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time


class Post:
    def __init__(self):
        self.url=None
        self.likes=None
        self.hashtags=None
        self.comments=None