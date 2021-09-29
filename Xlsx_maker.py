import xlsxwriter as xl

class writer:
    
    
    def __init__(self,profileObj,postObjArray,workbook_name):
        self.profileObj=profileObj
        self.postObjArray=postObjArray
        self.sheet_name=sheet_name
        self.workbook= xl.Workbook(workbook_name)
        self.sheet=self.workbook.add_worksheet()
        self.write_profile()
        self.write_posts()
        
    def write_profile(self):
        sheet.write(0,0,'Name')
        sheet.write(0,1,'Username')
        sheet.write(0,2,'Age')
        sheet.write(0,3,'Total Posts')
        sheet.write(0,4,'Total Followers')
        sheet.write(0,5,'Total Posts')
        sheet.write(0,6,'Youtube Channel Link')
        
        sheet.write(1,0,self.profileObj.Name)
        sheet.write(1,1,self.profileObj.username)
        sheet.write(1,2,self.profileObj.age)
        sheet.write(1,3,self.profileObj.totalposts)
        sheet.write(1,4,self.profileObj.totalfollowers)
        sheet.write(1,5,len(self.profileObj.posts))
        
    def write_posts():
        sheet.write(5,0,'Url')
        sheet.write(5,1,'Likes')
        sheet.write(5,2,'Hashtags')
        sheet.write(5,3,'No. of Comments')
        sheet.write(5,4,'Caption')
        sheet.write(5,5,'Post Link')
        
        self.url=None
        self.likes=None
        self.hashtags=None
        self.comments=None
        self.captions=None
        self.postlink=postlink
        for i in range(len(self.postObjArray)):
            sheet.write(6+i,0,self.postObjArray[i].url)
            sheet.write(6+i,1,self.postObjArray[i].likes)
            sheet.write(6+i,2,self.postObjArray[i].hashtags)
            sheet.write(6+i,3,self.postObjArray[i].comments)
            sheet.write(6+i,4,self.postObjArray[i].captions)
            sheet.write(6+i,5,self.postObjArray[i].postlink)
        
        self.workbook.close()