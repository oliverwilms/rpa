from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

import yaml

conf = yaml.safe_load(open('loginDetails.yaml'))
myMkEmail = conf['mk_user']['email']
myMkPassw = conf['mk_user']['password']
portal = "https://mycw123.ecwcloud.com/portal16977/jsp/100mp/login_otp.jsp"

service1= Service(executable_path="C:\\Users\\olive\\Documents\\website_login\\chromedriver.exe")
driver = webdriver.Chrome(service=service1)

def login(url,userId, username, passId, password, clickId):
    driver.get(url)
    element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME,userId)))
    driver.find_element(By.NAME, userId).send_keys(username)
    element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME,passId)))
    driver.find_element(By.NAME, passId).send_keys(password)
    element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME,clickId)))
    driver.find_element(By.NAME, clickId).click()

login(portal, "loginUser", myMkEmail, "enterPwd", myMkPassw, "loginSubmit")
element = wait(driver, 10).until(EC.presence_of_element_located((By.NAME,"test12345")))
#time.sleep(10)
