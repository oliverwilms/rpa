from selenium import webdriver
import yaml

conf = yaml.safe_load(open('loginDetails.yaml'))
myMkEmail = conf['mk_user']['email']
myMkPassw = conf['mk_user']['password']
portal = "https://mycw123.ecwcloud.com/portal16977/jsp/100mp/login_otp.jsp"

driver = webdriver.Chrome()

def login(url,userId, username, passId, password, clickId):
    driver.get(url)
    driver.find_element(By.NAME, value=userId).send_keys(username)
    driver.find_element(By.NAME, value=passId).send_keys(password)
    driver.find_element(By.NAME, value=clickId).click()

login(portal, "loginUser", myMkEmail, "enterPwd", myMkPassw, "loginSubmit")