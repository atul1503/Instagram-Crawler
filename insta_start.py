from InstaProfileCrawler import InstaProfileCrawler
from Post  import Post
from Xlsx_maker import writer


def getUsernames():
    return ['cristiano','sadhguru']
    
def everything_starts_here():
    usernames=getUsernames()
    flag=False
    for id in usernames:
        if flag:
            profile=InstaProfileCrawler(id,profile.browserHandle)
        else:
            profile=InstaProfileCrawler(id)
        flag=True    
        profile.getName()
        profile.getAge()
        profile.get_total_Followers()
        profile.get_total_posts()
        profile.getVerificationStatus()
        profile.getPosts()
        profile.getYoutube()
        
        postArr=[]
        for plink in profile.getPosts():
            post=Post(plink,profile.browserHandle)
            post.getLikes()
            post.getHashtags()
            post.getCaption()
            postArr.append(post)
    
        writer(profile,postArr,profile.getName())
    
everything_starts_here()