from _Lib_.Lib import *
#-D-A-T-A-------------------------------------------------------------
import _DataStuff_.DailyMemory
import _DataStuff_.Targets
import _DataStuff_.PostsLinks


class Aparat:
    def __init__(self,UserName,Password):
        self.username=UserName
        self.password=Password
        

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
        
