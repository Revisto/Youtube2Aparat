from _Lib_.Lib import *
#-D-A-T-A-------------------------------------------------------------
import _DataStuff_.DailyMemory
import _DataStuff_.Targets
import _DataStuff_.PostsLinks


class Aparat:
    def __init__(self,UserName,Password):
        self.username=UserName
        self.password=Password
        
class YouTube:
        
    def SetUpDriver(self,HeadLess=True):
        options = webdriver.ChromeOptions()
        if HeadLess:
            options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        #options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        Drive = webdriver.Chrome(options=options)
        self.Driver=Drive
        
    def CloseDriver(self):
        self.Driver.close()

    def GoToVideoPage(self,UserName):
        self.Driver.get("https://www.youtube.com/c/"+UserName+"/videos")
        print ("Currntly We Are In >> "+str(UserName))
        
    def MineLinks_WhenInVideoPage(self,HowMany="All"):
        RawLinks = self.Driver.find_elements_by_id("video-title")
        Links=[]
        for x in RawLinks:
            Links.append(str(x.get_attribute("href")))
        if HowMany=="All":
            HowMany=len(Links)
        return Links[0:HowMany]

    def LinkDownload(self,Link):
        Video = pafy.new(Link)
        Best = Video.getbest()
        #Resolution=Best.resolution
        DownloadLink = Best.url
        return DownloadLink
    
    def VideoDetails(self,Link):
        Video = pafy.new(Link)
        Details={ 
        "Title" : Video.title ,
        "Rate" : Video.rating ,
        "Views" : Video.viewcount ,
        "Duration" : Video.duration ,
        "Author" : Video.author     
        }
        
        return Details

class DataStuff:

    def ActionLimits(self,TheKey):
        Limits={
            'Posts':45 , #min
            'PostsPerDay':30 ,  #times
        }
        
        try:
            return Limits[TheKey]
        except:
            return False
    
    def ReturnWhatCanWeDoNow(self):
        if not(DataStuff().IsDailyMemoryForToday()):
            DataStuff().ReplaceFile()
            print ("Memory Updated")
        
        Dict=DataStuff().GetDailyMemory()
        Actions=[]
        for Key in Dict:
            if not( len(Dict[Key]) >= DataStuff().ActionLimits(str(Key)+"PerDay") ):
                ListOfActions=Dict[Key]
                if ListOfActions==[]:
                    Actions.append([1,str(Key)])
                else:
                    ListOfActions.sort()
                    LastActionTime=ListOfActions[-1]
                    MinLastAction=LastActionTime[0]*60+LastActionTime[1]
                    TimeNow=DataStuff().Time()
                    MinTimeNow=TimeNow[0]*60+TimeNow[1]
                    if MinTimeNow<MinLastAction:
                        MinTimeNow=24*60
                    Space=MinTimeNow-MinLastAction
                    if Space>DataStuff().ActionLimits(Key):
                        Actions.append([1/(Space-DataStuff().ActionLimits(Key)),Key])
                    elif Space==DataStuff().ActionLimits(Key):
                        Actions.append([1,Key])

        if Actions==[]:
            return False

        Actions.sort()
        BestAction=Actions[0]
        SimilarBestActions=[]
        for Action in Actions:
            if Action[0]==BestAction[0]:
                SimilarBestActions.append(Action)
            else:
                break
        RandomBestAction=(random.choice(SimilarBestActions))
        KeyOfBestAction=RandomBestAction[1]
        #return KeyOfBestAction,Actions
        Actions.remove(RandomBestAction)
        KeyActions=[]
        for Action in Actions:
            KeyActions.append(Action[1])
        return {'BestAction':KeyOfBestAction , 'AllActionsExceptBestAction':KeyActions}     
        
    def IsDailyMemoryForToday(self):
        Dict=DataStuff().GetDailyMemory() 
        if Dict["Date"] == DataStuff().Date():
            return True
        else:
            return False
    
    def AutoAddValue(self,TheKey):
        if TheKey=="Date":
            return False
        
        Dict=DataStuff().GetDailyMemory() 
        try:
            Dict[TheKey].append(DataStuff().Time())
        except:
            return False
        DataStuff().ReplaceFile(Dict)
        
        print (">>>SuccessFully Updated<<<")
        return True
    
    def ReplaceFile(self,FileData="None",NameFile="DailyMemory.py",NameData="DailyReport"):
        if FileData=="None":
            FileData=DataStuff().RawDictionaryOfData()
        DataStuff().DeleteFile(NameFile)
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+NameFile
        with open (NameFile,"w") as f:
            f.write(str(str(NameData)+"=")+str(FileData))
            f.close()
        print (">>> "+str(NameData)+" SuccussFully Replaced <<<")
        
    def GetDailyMemory(self):
        DailyMemory_ = reload(_DataStuff_.DailyMemory)
        DailyMemory_ = _DataStuff_.DailyMemory.DailyReport
        return DailyMemory_
    
    def GetTargets(self):
        AllTargets_ = reload(_DataStuff_.Targets)
        AllTargets_ = _DataStuff_.Targets.AllTargets
        return AllTargets_
    
    def RawDictionaryOfData(self):
        Dict={
            "Date" : DataStuff().Date(),
            
            "Posts" : [],
            
        }
    
        return Dict

    def Date(self):
        Raw=str(datetime.datetime.now())
        Raw=Raw.split(" ")
        Raw=Raw[0]
        Raw=Raw.split("-")
        for i in range (len(Raw)):
            Raw[i]=int(Raw[i])
        
        return Raw
       
    def Time(self):
        Raw=str(datetime.datetime.now())
        Raw=Raw.split(" ")
        Raw=Raw[1]
        Raw=Raw.split(":")
        for i in range (len(Raw)):
            Raw[i]=float(Raw[i])
        for i in range (len(Raw)):
            Raw[i]=int(Raw[i])
        
        return Raw[0:2]
      
    def CaptionGenerator(self):
        
        Text="""
        تست کپشن
        """
        return Text+(" ".join(HashTags))

    def ContentTarget(self):
        List=DataStuff().GetTargets()
        List_=[]
        while len(List)!=0:
            RandomChoice=random.choice(List)
            List.remove(RandomChoice)
            List_.append(RandomChoice)
        return List_
        #return ["nsworld.ir"]
        
    def ReturnPostsLinks(self):
        NewLinks = reload(_DataStuff_.PostsLinks)
        NewLinks = NewLinks.LinksPosted
        return NewLinks
    
    def AddPostsLinks(self,Link):
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+'PostsLinks.py'
        with open(NameFile , 'a+') as f:
            f.write('"'+str(Link)+'"'+",")
            f.close()

    def DeleteFile(self,Path):
        try:
            os.remove(Path)
            print ("Successfully Removed")
            return True
        except:
            try:
                Pwd=DataStuff().Pwd()
                NameFile=Pwd+'/_DataStuff_/'+Path
                os.remove(NameFile)
                print ("Successfully Removed")
                return True
            except:
                print ("No Such File to Be Removed")
                return False
         
    def Pwd(self):
        return str(os.getcwd())
        



print (YouTube().VideoDetails("https://www.youtube.com/watch?v=217WsOwSVS8"))
a.SetUpDriver()
a.GoToVideoPage("Samsung")
Links= (a.MineLinks_WhenInVideoPage())
print (a.LinkDownload(Links[0]))
print (a.VideoDetails(Links[0]))





# Behind The Scene
#Dont Look : )
#Maybe a code is Naked
'''a=YouTube()
a.SetUpDriver()
a.GoToVideoPage("Samsung")
Links= (a.MineLinks_WhenInVideoPage())'''
'''from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=VN7Osrd3DF8').streams.get_highest_resolution().download()
'''
'''import pafy
url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)
print (video.title)
print (video.rating)
print (video.viewcount)
print (video.duration)
print (video.description)
'''
'''import pafy
url = "https://www.youtube.com/watch?v=FCRmIoX6PTA"
video = pafy.new(url)
best = video.getbest()
print (best.resolution, best.extension)
streams = video.streams
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)
'''