import xlsxwriter as xl

class writer:
    
    
    def __init__(self,profileObj,postObjArray,workbook_name):
        self.profileObj=profileObj
        self.postObjArray=postObjArray
        self.workbook= xl.Workbook(workbook_name+'.xlsx')
        self.sheet=self.workbook.add_worksheet()
        self.write_profile()
        self.write_posts()
        
    def write_profile(self):
        self.sheet.write(0,0,'Name')
        self.sheet.write(0,1,'Username')
        self.sheet.write(0,2,'Age')
        self.sheet.write(0,3,'Total Posts')
        self.sheet.write(0,4,'Total Followers')
        self.sheet.write(0,5,'Total Posts')
        self.sheet.write(0,6,'Youtube Channel Link')
        
        self.sheet.write(1,0,self.profileObj.Name)
        self.sheet.write(1,1,self.profileObj.username)
        self.sheet.write(1,2,self.profileObj.age)
        self.sheet.write(1,3,self.profileObj.totalposts)
        self.sheet.write(1,4,self.profileObj.totalfollowers)
        self.sheet.write(1,5,len(self.profileObj.posts))
        self.sheet.write(1,6,self.profileObj.youtube)
        
    def write_posts(self):
        self.sheet.write(5,1,'Likes')
        self.sheet.write(5,2,'Hashtags')
        self.sheet.write(5,4,'Caption')
        self.sheet.write(5,5,'Post Link')
        

        for i in range(len(self.postObjArray)):
            self.sheet.write(6+i,1,self.postObjArray[i].likes)
            self.sheet.write(6+i,2,self.postObjArray[i].hashtags)
            self.sheet.write(6+i,4,self.postObjArray[i].captions)
            self.sheet.write(6+i,5,self.postObjArray[i].postlink)
        
        self.workbook.close()