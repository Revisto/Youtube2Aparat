from _Lib_.Lib import *
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

Drive=SetUpDriver(False)

Drive.get("https://blog.feedspot.com/gaming_youtube_channels/")

Cases=Drive.find_elements_by_class_name("ext")
Videos=[]
for Case in Cases:
    a=(str(Case.get_attribute('href')))
    a=a.split("/")
    a=a[-2]
    Videos.append(a)
print (Videos)

