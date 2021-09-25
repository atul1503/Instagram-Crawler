from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class InstaProfileCrawler:
    NameCssSelector='#react-root > section > main > div > div.-vDIg > h1'
    origin='https://www.instagram.com/'
    def __init__(self,username):
        self.username=username()
        self.Name=''
        self.age=None
        self.posts=[]
        self.browserHandle=webdriver.Chrome()
    def getName(self):
        if self.Name:
            return self.Name
        self.browserHandle.get(origin+self.username)
        self.browserHandle.switch_to.window(driver.window_handles[1])
        self.Name=self.browserHandle.find_element_by_css_selector(NameCssSelector).text
        return self.Name
    def getAge(self):
        if self.Age:
            return self.age
        self.browserHandle.execute_script("window.open('');")
        self.browserHandle.get(self.Name+' age')
        source=self.browserHandle.page_source
        self.browserHandle.close()
        age_string=''
        for i in range(len(source)):
            if source[i:i+5] in ('years','Years'):
                j=i-2
                while source[j] in '0123456789':
                    age_string+=source[j]
                    j-=1
                break
        self.age=int(age_string)
        return self.age        
        
    