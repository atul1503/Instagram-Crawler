from InstaProfileCrawler import InstaProfileCrawler
from Post  import Post

b=InstaProfileCrawler('cristiano')
print(b.getName())
print(b.getAge())
print(b.get_total_Followers())
print(b.get_total_posts())
p=b.getPosts()
print(b.getYoutube())
pk=Post(p[0],b.browserHandle)
print(pk.getHashtags())
