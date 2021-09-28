from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
from Post import Post
from selenium.webdriver.common.proxy import Proxy,ProxyType


class InstaProfileCrawler:
    NameXpathSelector='//*[@id="react-root"]/section/main/div/div[1]/h1'
    origin='https://www.instagram.com/'
    
    def instaLogin(self):
        usernameInputXpath='//*[@id="loginForm"]/div/div[1]/div/label/input'
        passwordInputXpath='//*[@id="loginForm"]/div/div[2]/div/label/input'
        loginXpath='//*[@id="react-root"]/section/main/div/div[4]/article/div[1]/div//a'
        tester_insta_username='tripathi8341'
        tester_insta_password='pinkidi'
        self.browserHandle.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        usernameInput=self.browserHandle.find_element_by_xpath(usernameInputXpath)
        passwordInput=self.browserHandle.find_element_by_xpath(passwordInputXpath)
        usernameInput.send_keys(tester_insta_username)
        passwordInput.send_keys(tester_insta_password)
        self.browserHandle.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
        self.browserHandle.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div').click()
        if self.browserHandle.find_element_by_css_selector('#slfErrorAlert'):
            self.browserHandle.close()
            print('CONGRATULATIONS INSTAGRAM BLOCKED YOU. WAIT FOR ETERNITY NOW'.center())
    
    def __init__(self,username):
        self.username=username
        self.Name=None
        self.age=None
        self.totalposts=None
        self.totalfollowers=None
        self.posts=None
        self.isVerified=None
        self.browserHandle=webdriver.Chrome()
        #self.browserHandle.implicitly_wait(8)
        #self.instaLogin()
        
        
    def go_to_profile(self):
        if not self.isProfilePage():
            self.instaLogin()
            self.browserHandle.get(InstaProfileCrawler.origin+self.username)
    
    def getName(self):
        if self.Name:
            return self.Name
        self.go_to_profile()
        self.Name=self.browserHandle.find_element_by_xpath(InstaProfileCrawler.NameXpathSelector).text
        self.Name=self.browserHandle.find_element_by_class_name('rhpdm').text
        return self.Name
    
    def getAge(self):
        if self.age:
            return self.age
        self.go_to_profile()
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
    
    def isProfilePage(self):
        if InstaProfileCrawler.origin+self.username in self.browserHandle.current_url:
            return True
        else:
            return False
    
    def get_total_Followers(self):
        if self.totalfollowers:
            return self.totalfollowers
        self.go_to_profile()
        self.totalfollowers=self.browserHandle.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span').get_attribute('title')
        return self.totalfollowers
    
    def get_total_posts(self):
        if self.totalposts:
            return self.totalposts
        self.go_to_profile()
        self.totalposts=self.browserHandle.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a').find_element_by_tag_name('span').text
    
    def getVerificationStatus(self):
        if self.isVerified:
            return self.isVerified
        self.go_to_profile()
        if self.browserHandle.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span').text=='Verified':
            self.isVerified='Yes'
        else:
            self.isVerified='No'
        return self.isVerified
        
    def getPosts(self):
        if self.posts:
            return self.posts
        self.go_to_profile()
        postlinks=self.browserHandle.find_elements_by_tag_name('a')
        i=len(postlinks)-1
        while i>-1:
            if '/p/' not in postlinks[i].get_attribute('href'):
                postlinks.pop(i)
            i-=1
        for i in range(len(postlinks)):
            postlinks[i]=postlinks[i].get_attribute('href')
        return postlinks
    
    def getYoutube(self):
        
