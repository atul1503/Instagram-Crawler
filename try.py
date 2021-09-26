from InstaProfileCrawler import InstaProfileCrawler


b=InstaProfileCrawler('sadhguru')
try:
    print(b.getAge())
except:
    b.browserHandle.close()