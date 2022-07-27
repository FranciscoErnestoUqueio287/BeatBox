#https://painel.dizu.com.br/login
#/html/body/div[1]/section/form/div[1]/div/input
#/html/body/div[1]/section/form/div[2]/div/input
#/html/body/div[1]/section/form/div[5]/button | Return
#/html/body/div[1]/div/div[2]/div[6]/div/div[3]/div[2]/div/a
#/html/body/div[1]/div/div[2]/div[2]/div/ul/li[2]/a
#/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div/select
#/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div/div[3]/label
#/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[2]/button
from selenium import webdriver
import os,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = Options()
options.add_experimental_option("w3c", True)
global r
options.add_argument("start-maximized")
options.add_argument("--profile-directory=Default")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--incognito")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--incognito")
options.binary_location = os.environ.get("GOOGLE_CHROME_BINARY")
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('no-sandbox')
r = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=options,desired_capabilities=options.to_capabilities())
stealth(r,languages=['pt-PT','en'],vendor='Google Inc.',platform='win32',webgl_vendor='Intel Inc.',renderer='Intel Iris OpenGL Engine',fix_hairline=True)


def find_element(by,el,time=0):
    try:
        if time < 4: time.sleep(3);return r.find_element(by,el)
    except Exception as e: return find_element(by,el,time+1)
def loging(r):
    if "login" in r.title.lower() or "instagram" in r.title.lower():
        print("In, About to login")
        time.sleep(5)
        try:
            us = r.find_element(By.NAME,"username")
            pa = r.find_element(By.NAME,"password")
        except Exception as ex:
            print(ex,"Not even logged")
            us = r.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/input")
            pa = r.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input")
        time.sleep(2)
        print("Logged on Instagram")
        us.send_keys("+258842150009")
        pa.send_keys("novapasse")
        pa.send_keys(Keys.RETURN)
        time.sleep(5)
        if "/onetap/" in r.current_url:
            print("Saved Session")
            b = r.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div/section/div/button")
            b.click()
            time.sleep(2)
            try:
                print("Turned ON")
                q = r.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]");q.click()
            except: pass
def start(r):
    try: t = r.get("https://painel.dizu.com.br/login"); print("GOING to Dizu")
    except: start(r)
def on_dizu(r):
    try:
        time.sleep(8)
        print("About to log on dizu")
        us = r.find_element(By.XPATH,"/html/body/div[1]/section/form/div[1]/div/input")
        pa = r.find_element(By.XPATH,"/html/body/div[1]/section/form/div[2]/div/input")
        us.send_keys("acllasacllas@gmail.com")
        pa.send_keys("incorrect")
        print("Sended to log in dizu")
        time.sleep(5)
        pa.send_keys(Keys.RETURN)
        time.sleep(5)
        print("Logged on Dizu")
        r.get("https://painel.dizu.com.br/painel/conectar")
        print("Going to connect")
        #us = r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[6]/div/div[3]/div[2]/div/a")
        #us.send_keys(Keys.RETURN)
        time.sleep(7)
        us = r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/ul/li[2]/a")
        us.send_keys(Keys.RETURN)
        time.sleep(7)
        us = r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div/select")
        ep = us.get_attribute("value")
        us.send_keys(Keys.DOWN)
        print("Choosing my account")
        while us.get_attribute("value") == ep:
            r.refresh()
            time.sleep(10)
            us.send_keys(Keys.DOWN)
        print("Choosed")
        time.sleep(5)
        try:
            r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div/div[2]/label").click()
            print("Label 1")
        except: pass
        try:
            r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[1]/div/div[3]/label").click()
            print("Label 2")
        except: pass
        us = r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[2]/button")
        print("Loading Tasks")
        us.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e: print(e);r.get("https://painel.dizu.com.br/login");on_dizu(r);print("Starting on dizu because",e)
def liking(r):
    main = r.current_window_handle
    b = r.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/form/div[2]/button")
    while True:
        
        try:
            
            time.sleep(3)
            print("About to find Ver link")
            rt = "followed"
            us = r.find_element(By.XPATH,"//*[contains(text(),'Ver link')]")
            print("Found on page")
            us.click()
            print("Ver link clicado")
            r.switch_to.window(r.window_handles[len(r.window_handles)-1])
            print("Switched")
            time.sleep(40)           #bot.follow("".join(urlparse(r.current_url).path.split("/")))
            print("Time out")
            actions = ActionChains(r)
            actions.send_keys(Keys.TAB)
            actions.perform()
            p1 = r.execute_script("return document.activeElement")
            if p1.text == '':
                actions.send_keys(Keys.TAB)
                actions.perform()
            p1 = r.execute_script("return document.activeElement") 
            if p1.text in ['Follow','Follow Back']:
                actions.send_keys(Keys.RETURN)
                actions.perform()
            print("Sent Return")
            actions.perform()
            #exec(input("Codigo: "))
            print("perfomed")
            time.sleep(2)
            if r.current_window_handle != main: r.close();r.switch_to.window(main)
            us = r.find_element(By.XPATH,"//*[contains(text(),'confirmar')]")
            us.click()
            print("Confirmed")
            time.sleep(3)
        except Exception as e: r.switch_to.window(main);b.click();print(e)
while True:
    try:
        r.get("https://instagram.com")
        print("Sending Request")
        loging(r)
        start(r)
        on_dizu(r)
        liking(r)
    except: pass
#737670
def tik(r):
    l = "https://www.tiktok.com/login/phone-or-email/phone-password"
    r.get(l)
    time.sleep(5)
    us1 = find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/form/div[3]/div/div[2]/input")
    us = find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/form/div[3]/div/div[1]/div[2]/div[2]/ul/div[13]/li/span")
    us.click()
    us1.send_keys("841236144")
    us = find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/form/div[4]/div/input")
    us.send_keys("Incorrect677716@")
    
    

