from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time



class InstaProfileCrawler:
    NameXpathSelector='//*[@id="react-root"]/section/main/div/div[1]/h1'
    origin='https://www.instagram.com/'
    def instaLogin(self):
        usernameInputXpath='//*[@id="loginForm"]/div/div[1]/div/label/input'
        passwordInputXpath='//*[@id="loginForm"]/div/div[2]/div/label/input'
        loginXpath='//*[@id="loginForm"]/div/div[3]/button'
        username='tripathi8341'
        password='pinkidi'
        self.browserHandle.get('https://www.instagram.com/accounts/login/')
        usernameInput=self.browserHandle.find_element_by_xpath(usernameInputXpath)
        passwordInput=self.browserHandle.find_element_by_xpath(passwordInputXpath)
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.browserHandle.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
        self.browserHandle.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        
    def __init__(self,username):
        self.username=username
        self.Name=''
        self.age=None
        self.posts=[]
        self.browserHandle=webdriver.Chrome()
        self.browserHandle.implicitly_wait(8)
        self.instaLogin()
    def getName(self):
        if self.Name:
            return self.Name
        self.browserHandle.get(InstaProfileCrawler.origin+self.username)
        #self.Name=self.browserHandle.find_element_by_xpath(InstaProfileCrawler.NameXpathSelector).text
        self.Name=self.browserHandle.find_element_by_class_name('rhpdm').text
        return self.Name
    def getAge(self):
        if self.age:
            return self.age
        googleBaseUrl='https://www.google.com/search?q='
        self.browserHandle.execute_script("window.open('');")
        self.browserHandle.switch_to.window(self.browserHandle.window_handles[1])
        self.getName()
        self.browserHandle.get(googleBaseUrl+self.Name+' age')
        source=self.browserHandle.page_source
        self.browserHandle.close()
        age_string=''
        for i in range(len(source)):
            if source[i:i+5] in ('years','Years'):
                j=i-2
                while source[j] not in '0123456789':
                    j-=1
                while source[j] in '0123456789':
                    age_string+=source[j]
                    j-=1
                break
        self.age=int(age_string[::-1])
        return self.age        
        
    