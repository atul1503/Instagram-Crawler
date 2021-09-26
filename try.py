from InstaProfileCrawler import InstaProfileCrawler


b=InstaProfileCrawler('sadhguru')
try:
    print(b.getName(),b.getAge())
except:
    b.browserHandle.close()