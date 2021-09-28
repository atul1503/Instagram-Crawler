from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time


class Post:
    likes_selector='#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div.eo2As > section.EDfFK.ygqzn > div > div > a > span'
    caption_selector='#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span'
    
    
    def __init__(self,postlink,browserHandle):
        self.url=None
        self.likes=None
        self.hashtags=None
        self.comments=None
        self.captions=None
        self.postlink=postlink
        self.browserHandle=browserHandle
    
    def go_to_post(self):
        if self.browserHandle.current_url==self.postlink:
            return
        self.browserHandle.get(self.postlink)
            
    def getLikes(self):
        if self.likes:
            return self.likes
        self.likes=self.browserHandle.find_element_by_css_selector(likes_selector).text
        return self.likes
        
        
    def getHashtags(self):
        if self.hashtags:
            return self.hashtags
        captions=self.browserHandle.find_element_by_css_selector(caption_selector).text
        i=0
        hashtags=''
        while i<len(captions):
            if captions[i]=='#':
                j=i
                while j<len(caption) and caption[j]!=' ':
                    hashtags+=caption[j]
                    j+=1
                hashtags+=' '
                i=j
            i+=1
        self.captions=captions
        return self.hashtags
        
        
    def getCaption(self):
        if self.captions:
            return self.captions
        captions=self.browserHandle.find_element_by_css_selector(caption_selector).text
        return captions