from _Lib_.Lib import *
#-D-A-T-A-------------------------------------------------------------
import _DataStuff_.DailyMemory
import _DataStuff_.Targets
import _DataStuff_.PostsLinks
import string

class Telegram:
    
    def __init__(self):
        self.Bot_Token='1306882752:AAFqLGTOAtkRhWBvmfZkHg_0nOOXfLXBSP4'
        self.Chat_Id='-1001278142168'
    
    def SendNakedMessage(self,Message):
        bot_token = self.Bot_Token
        bot_chatID = self.Chat_Id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + Message
        try:
            response = requests.get(send_text)
        except Exception as e: print('Could not send Telegram Message >>> '+str(e))
    def SendPhoto(self,Path):
        token = self.Bot_Token
        chat_id = self.Chat_Id
        file = Path
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        files = {}
        files["photo"] = open(file, "rb")
        requests.get(url, params={"chat_id": chat_id}, files=files)


class Notification:
    
    def Bar(self, Sec:int , Message="Processing"):        
        with ChargingBar(Message, max=Sec*100) as bar:
            for i in range(Sec*100):
                sleep(1/100)
                bar.next()
    
        return True

    def Loading(self,Message="Downloading"):
        with Spinner(str(Message)+"  ") as bar:
            while True:
                #lobal STOP_THREADs
                try:
                    if STOP_THREADs==True:
                        return True
                except: pass
                sleep(0.1)
                bar.next()
                
    def KillLoading(self):
        global STOP_THREADs
        STOP_THREADs = True
        print (" ")
        print('Loading Thread Killed') 
        del STOP_THREADs
        
    def StartLoading(self):
        T=threading.Thread(target=Notification().Loading,args=())
        T.start()


class Aparat:
    
    def __init__(self,SetDriver=True,HeadLess=True):
        def SetUpDriver(HeadLess=True):
            options = webdriver.ChromeOptions()
            if HeadLess:
                options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36')
            Drive = webdriver.Chrome(chrome_options=options)
            return Drive
        if SetDriver:
            self.Drive=SetUpDriver(HeadLess)
    
    def LogIn(self,UserName,Password):
        self.Drive.get("https://www.aparat.com/login")
        sleep(1)
        UsernameElements=self.Drive.find_element_by_class_name("cIoHFe")
        UsernameElements.send_keys(str(UserName))
        sleep(5)
        Click=self.Drive.find_element_by_class_name("margin-right5")
        Click.click()
        
        sleep(1)
        PasswordElements=self.Drive.find_element_by_class_name("iQlHkq")
        PasswordElements.send_keys(str(Password))
        sleep(5)
        Click=self.Drive.find_element_by_class_name("margin-right5")
        Click.click()
        sleep(10)  

    def CloseDriver(self):
        self.Drive.close()

    def SaveCookie(self,UserName):
        CN=UserName+"_Cookies.pkl"
        pickle.dump(self.Drive.get_cookies() , open(CN,"wb"))

    def LogInInstagramByCookie(self,UserName):
        CN=UserName+"_Cookies.pkl"
        CN="/Cookies/"+CN
        CN=DataStuff().Pwd()+CN
        self.Drive.get('https://www.aparat.com/')
        for cookie in pickle.load(open((CN), "rb")):
            if 'expiry' in cookie:
                del cookie['expiry']
            self.Drive.add_cookie(cookie)
        print ("DONE Logging In")
         
    def Upload(self,Link,Title,Description,Sticks):
        if len(Description)<30  or  type(Sticks)!=list  or  len(Sticks)>5  or  len(Sticks)<3:
            return False
        
        self.Drive.get("https://www.aparat.com/uploadnew")
        sleep(3)
        Input=self.Drive.find_element_by_class_name("react-fine-uploader-file-input")

        Input.send_keys(Link)
        
        Title_=self.Drive.find_element_by_class_name("sc-caSCKo")
        Title_.send_keys(Title)
        Description_=self.Drive.find_element_by_class_name("fmqcAi")
        Description_.send_keys(Description)
        Sticks_=self.Drive.find_element_by_xpath('//*[@id="video--detail-form"]/div[1]/div[3]/div[1]/div/div[1]/input')
        Sticks_.click()
        sleep(2)
        
        for Stick in Sticks:

            Sticks_.send_keys(Stick)
            sleep(1)
            Sticks_.send_keys(Keys.ENTER)
            sleep(1)
        
        sleep(5)
        
        self.Drive.save_screenshot("__.png")
        
        sleep(2)
        
        (self.Drive.find_elements_by_class_name("sc-bwCtUz"))[0].click()
        
        while True:
            try: self.Drive.find_element_by_class_name("bpoWCR") ; break
            except: sleep(3)
        
        print ("---Uploaded---")
        return True


                  
class YouTube:
        
    def __init__(self,SetDriver=True,HeadLess=True):
    
        def SetUpDriver(HeadLess=True):
            options = webdriver.ChromeOptions()
            if HeadLess:
                options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument('--disable-dev-shm-usage')
            #options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36')
            Drive = webdriver.Chrome(chrome_options=options)
            return Drive

        if SetDriver:
            self.Drive=SetUpDriver(HeadLess)
     
    def CloseDriver(self):
        self.Drive.close()

    def GoToVideoPage(self,UserName):
        self.Drive.get("https://www.youtube.com/channel/"+UserName+"/videos")
        print ("Currntly We Are In >> "+str(UserName))
        sleep(2)
        self.Drive.save_screenshot("Account.png")
        
    def MineLinks_WhenInVideoPage(self,HowMany="All"):
        RawLinks = self.Drive.find_elements_by_id("video-title")
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

        def Download(self,Link,Name):
            doc = requests.get(Link)
        #with open(Data().PWD()+"/Audios/Talks/"+'Talk.mp3', 'wb') as f:
        try: os.mkdir("Videos")
        except: pass
        with open('Videos/{}.mp4'.format(Name) , 'wb') as f:
            f.write(doc.content)
    
    def Download(self,Link,Name):
        doc = requests.get(Link)
        #with open(Data().PWD()+"/Audios/Talks/"+'Talk.mp3', 'wb') as f:
        try: os.mkdir("Videos")
        except: pass
        #Notification().StartLoading()
        with open('Videos/{}.mp4'.format(Name) , 'wb') as f:
            f.write(doc.content)
        #STOP_THREADs = True
        #sleep(5)
        #STOP_THREADs = False
        

     
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
      
    def DescriptionGenerator(self, ChannelName , Title,UserName):
        Space="""
                                                
"""
        PoweredBy="برگرفته از کانال های یوتیوب"
        
        Text=Title+(Space)+PoweredBy+(Space)+"لایک و سابسکرایب یادتون نره!!!"
        if len(Text)<30:
            Text+=Space+"تهیه شده توسط کانال "+'https://YouTube.com/channel/'+UserName
        return Text

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
    
    def SticksGenerator(self):
        Sticks=['گیم',  'گیم پلی' , 'گیمر', 'فورت نایت' ,'بازی']
        Selected=[]
        for _ in range (5):
            RandomChoice=random.choice(Sticks)
            Sticks.remove(RandomChoice)
            Selected.append(RandomChoice)    
        return Selected

    def Translate(self,text,Dest="fa"):
        translator= Translator(to_lang=Dest)
        translation = translator.translate(str(text))
        return translation

class Full_Programs:
    
    def UploadVideo(self):
        Revistube=YouTube()
        while True:
            RandomListOfContents=(DataStuff().ContentTarget())
            Telegram().SendNakedMessage("Start Mining to find a post")
            for Content in RandomListOfContents:
                Revistube.GoToVideoPage(Content)
                Links = (Revistube.MineLinks_WhenInVideoPage())
                Links = Links[0:5]
                print (Links)
                PostedLinks=DataStuff().ReturnPostsLinks()
                for SingeLink in Links:
                    if SingeLink not in PostedLinks:
                        try:
                            DetailsYoutubeVideo=Revistube.VideoDetails(SingeLink)
                            Duration=DetailsYoutubeVideo['Duration']
                            Duration=Duration.split(":")
                            print (Duration)
                        except:
                            Duration='99:99:99'
                        if int(Duration[0])==0 and int(Duration[1])<=20:
                            Telegram().SendNakedMessage("Found a Post")
                            Telegram().SendNakedMessage("Duratios is  "+str(Duration))
                            print ('Found One')
                            DownloadLink=Revistube.LinkDownload(SingeLink)
                            Revistube.Download(DownloadLink,"_Video_")
                            Telegram().SendNakedMessage("Downloaded")
                            Title=DetailsYoutubeVideo['Title']
                            Telegram().SendNakedMessage("Title is "+str(Title))
                            Aparatube=Aparat()
                            Aparatube.LogInInstagramByCookie("Revistube")
                            Telegram().SendNakedMessage("Channel : "+str(Content))
                            Description=DataStuff().DescriptionGenerator(Content,Title,"Revistube")
                            Sticks=DataStuff().SticksGenerator()
                            #TranslatedTitle=DataStuff().Translate(Title)
                            #MixTitle=Title+" "+TranslatedTitle
                            #if len(MixTitle)<=80:
                            #    Title=MixTitle
                            #if len(Title)>80:
                            #    Title=Title[:80]
                            Aparatube.Upload((DataStuff().Pwd())+"/Videos/_Video_.mp4",Title,Description,Sticks)
                            DataStuff().AddPostsLinks(SingeLink)
                            Telegram().SendNakedMessage("Uploaded  --  "+str(SingeLink))
                            Revistube.CloseDriver()
                            Aparatube.CloseDriver()
                            
                            return True
    
    def AutoVideoUpload(self):
        
        while True:
            
            try:
                
                Full_Programs().UploadVideo()
                
                Telegram().SendNakedMessage("---Fine---")
                
                Notification().Bar(30*60)

            except Exception as e:Telegram().SendNakedMessage("An Error  =  "+str(e))
            
            




