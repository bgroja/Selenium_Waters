import re
import time
import webbrowser
import subprocess
from flask import Flask, render_template,request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
app = Flask(__name__)
url2='http://localhost:5000'
url="https://microapps.on-demand.waters.com/"

url="https://microapps.on-demand.waters.com/"
serv = Service("C:\Program Files\browsers\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv)


@app.route('/')
def run_tests():
    return render_template("home.html")

#function_list = [UrlAccess,login,CCSonDemand,ForEmpower,DirectCCSonDemand,register,DataConnect]
@app.route('/run-tests',methods=['POST'])
def watercorp():
   UrlAccessMessage = UrlAccess()
   loginMessage = login()
   CCSonDemandMessage = CCSonDemand()
   ForEmpowerMessage = ForEmpower()
   DirectCCSonDemandMessage = DirectCCSonDemand()
   registerMessage = register()
   DataConnectMessage = DataConnect()
   Home_ExecMessage = Home_Exec()
   scroll_homeMessage = scroll_home()
   Smart_LCMethodMessage = Smart_LCMethod()
   ReportFeedbackMessage = ReportFeedback()
   return  render_template('home.html', UrlAccessMessage = UrlAccessMessage, loginMessage = loginMessage,CCSonDemandMessage = CCSonDemandMessage,ForEmpowerMessage = ForEmpowerMessage,DirectCCSonDemandMessage = DirectCCSonDemandMessage,registerMessage = registerMessage,DataConnectMessage = DataConnectMessage,Home_ExecMessage = Home_ExecMessage, scroll_homeMessage = scroll_homeMessage,
                           Smart_LCMethodMessage = Smart_LCMethodMessage,ReportFeedbackMessage = ReportFeedbackMessage)

def UrlAccess():
   driver.get(url)
   if driver.title=='Waters Microapp Store':
       UrlAccessMessage = "Pass"
   else :
       UrlAccessmessage="Fail"
   return UrlAccessMessage

def ForEmpower():
    driver.get(url)
    driver.maximize_window()
    element = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/a[2]/div')
    element.click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[3]/div[2]/div/a[7]/div/div/div[1]')
    attribute_value = element.get_attribute('name')
    print(attribute_value)
    if element.get_attribute('name')=="cardTitle":
       ForEmpowerMessage = "Pass"
    else :
       ForEmpowerMessage = "Fail"
    #print(ForEmpowerMessage)
    return ForEmpowerMessage

def login():
   #data = request.json
   driver.get(url)
   element=driver.find_element(By.ID,"login")
   element.click()
   element = driver.find_element(By.ID, "emailField")
   element.send_keys('conajma@partner.waters.com')
   element = driver.find_element(By.ID, "passwordField")
   element.send_keys('RojuYaju@@1994')
   element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/button")
   element.click()
   driver.maximize_window()
   element=driver.find_element(By.ID,"welcomeUserName")
   print(element.get_attribute("id"))
   if element.get_attribute("id")=='welcomeUserName':
    loginMessage = "Pass"
   else:
    loginMessage="Fail"
   return loginMessage

def CCSonDemand():
    driver.get(url)
    element = driver.find_element(By.ID, "login")
    element.click()
    element = driver.find_element(By.ID, "emailField")
    element.send_keys('conajma@partner.waters.com')
    element = driver.find_element(By.ID, "passwordField")
    element.send_keys('RojuYaju@@1994')
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/button")
    element.click()
    driver.maximize_window()
    time.sleep(4)
    element=driver.find_element(By.NAME,'cardTitle')
    element.click()
    expected_url="https://microapps.on-demand.waters.com/home/showmarkdown/ccs-ondemand"
    time.sleep(4)
    actual_url=driver.current_url
    if expected_url==actual_url:
        CCSonDemandMessage = "Pass"
    else:
        CCSonDemandMessage = "Fail"
    return CCSonDemandMessage

def DirectCCSonDemand():
    driver.get('https://microapps.on-demand.waters.com/home/showmarkdown/ccs-ondemand')
    driver.maximize_window()
    time.sleep(4)
    driver.execute_script("document.getElementsByClassName('navbar')[0].style.display = 'none';")
    element = driver.find_element(By.XPATH, '/html/body/div[3]/div/p[5]/a[1]')
    location = element.location
    driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(element))
    element.click()
    time.sleep(10)
    #element.send_keys('conajma@partner.waters.com')
    #element = driver.find_element(By.ID, "passwordField")
    #element = driver.find_element(By.ID, "emailField")
    #element.send_keys('RojuYaju@@1994')
    #element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/div[3]/button")
    #element.click()
    #time.sleep(5)
    expected_url='https://ccs.on-demand.waters.com/#/'
    actual_url=driver.current_url
    print(actual_url)
    if expected_url==actual_url:
        DirectCCSonDemandMessage = "Pass"
    else:
        DirectCCSonDemandMessage = "Fail"

    return DirectCCSonDemandMessage

def register():
    time.sleep(5)
    driver.get('https://microapps.on-demand.waters.com/')
    element=driver.find_element(By.ID,"welcomeUserName")
    element.click()
    element=driver.find_element(By.CLASS_NAME,"dropdown-content")
    #drop_down=Select(element)
    #drop_down.select_by_visible_text("logout")
    element.click()
    element = driver.find_element(By.ID, "login")
    element.click()
    driver.maximize_window()
    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Register here!')
    element.click()
    element = driver.find_element(By.ID, "registeredFirstName")
    element.send_keys('Ajay')
    element = driver.find_element(By.ID, "registeredLastName")
    element.send_keys('Managaon')
    element = driver.find_element(By.ID, "registeredEmail")
    element.send_keys("ajaymanagaon@outlook.com")
    wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[placeholder='Password']")))
    element.send_keys("Yaju@@2024")
    wait = WebDriverWait(driver, 4)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"input[placeholder='Company']")))
    element.send_keys("waters")
    original_handle = driver.current_window_handle
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".underline")))
    element.click()
    for handle in driver.window_handles:
        if handle != original_handle:
            driver.switch_to.window(handle)
            break
    driver.switch_to.window(original_handle)
    wait = WebDriverWait(driver, 5)
    element = wait.until(
        (EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/form/div[8]/div/input"))))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    element = driver.find_element(By.ID, "registerUser")
    element.click()
    element=driver.find_element(By.ID,"modalCustomMessage")
    attribute=element.get_attribute("id")
    if attribute=='modalCustomMessage':
        registerMessage = "Pass"
    else:
        registerMessage = "Fail"
    return registerMessage

def DataConnect():
    driver.get('https://microapps.on-demand.waters.com/')
    element = driver.find_element(By.ID, 'search')
    element.click()
    element.send_keys("Dat")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, 'ui-id-2')))
    # element=driver.find_element(By.ID,'ui-id-2')
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[3]/div[2]/div/a[12]/div/div/div[1]')
    element.click()
    expected_url="https://microapps.on-demand.waters.com/home/showmarkdown/data-as-a-product"
    actual_url=driver.current_url
    if expected_url==actual_url:
       DataConnectMessage = "Pass"
    else:
       DataConnectMessage = "Fail"
    return DataConnectMessage

def Home_Exec():
    element = driver.find_element(By.XPATH,'/html/body/nav/a/img')
    element.click()
    #wait = WebDriverWait(driver, 5)
    #element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="showMsiAppsLaptop"]/div')))
    #element.click()
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="showMsiAppsLaptop"]/div')))
    element.click()
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="appStoreCards"]/a[14]/div/div/div[1]')))
    element.click()
    expected_url= 'https://microapps.on-demand.waters.com/home/showmarkdown/msi-quantify'
    actual_url=driver.current_url
    if expected_url==actual_url:
        Home_ExecMessage= "Pass"
    else:
        Home_ExecMessage = "Fail"
    return Home_ExecMessage

def scroll_home():
    wait = WebDriverWait(driver,5)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/nav/a/img")))
    element.click()
    element = driver.find_element(By.XPATH,"/html/body/div/div[3]/div[3]/div[2]/div/a[10]/div/div/div[1]")
    element.click()
    original_handle = driver.current_window_handle
    wait= WebDriverWait(driver,5)
    element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "License Agreement")))
    element.click()
    wait = WebDriverWait(driver,5)
    expected_url = 'https://proddocuments.on-demand.waters.com/LicenseAgreement/Microapps-EULA.pdf'
    actual_url = driver.current_url
    if actual_url == expected_url :
        scroll_homeMessage = "Pass"
    else:
        scroll_homeMessage = "fail"
    driver.get("https://microapps.on-demand.waters.com/home/showmarkdown/rrt-alignment")
    return scroll_homeMessage

def Smart_LCMethod():
    wait = WebDriverWait(driver,5)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/nav/a/img")))
    element.click()
    wait = WebDriverWait(driver,5)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/div[3]/div[2]/div/a[11]/div/div/div[2]")))
    element.click()
    expected_url = "https://microapps.on-demand.waters.com/home/showmarkdown/ma-ewa-slc-md"
    actual_url = driver.current_url
    if expected_url == actual_url:
        Smart_LCMethodMessage = "Pass"
    else:
        Smart_LCMethodMessage = "Fail"
    print(Smart_LCMethodMessage)
    return Smart_LCMethodMessage

def ReportFeedback():
    element = driver.find_element(By.ID,"lnkFeedback")
    element.click()
    element =driver.find_element(By.ID,"name")
    element.send_keys("Ajay")
    element= driver.find_element(By.ID,"email")
    element.send_keys("ajaymanagaon@waters.com")
    element=driver.find_element(By.ID,"feedback")
    element.send_keys("Good app")
    ReportFeedbackMessage = "Pass"
    return ReportFeedbackMessage

def launch_web_address(url2):
  webbrowser.open(url2)

if __name__ == '__main__':
    app.run()
    launch_web_address(url2)
    run_tests()
    watercorp()
    launch_web_address(url2)







