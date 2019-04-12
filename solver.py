from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import ssl
from pathlib import Path

datafolder = Path('captcha/')
filename= "captcha"
fileext = ".bmp"

driver = webdriver.Chrome() #uses chromium 

driver.get("https://academicscc.vit.ac.in/student/stud_login.asp")
image = driver.find_element_by_id("imgCaptcha")

ssl._create_default_https_context = ssl._create_unverified_context #ignores ssl error not good code

for i in range(1,11):
    fileloc = datafolder/(filename + str(i) + fileext)
    ele = driver.find_element_by_link_text('Change Verification Code')
    ele.click() #creates new verification code
    urllib.request.urlretrieve(image.get_attribute('src'), fileloc) #stores captha as bmp

driver.close() 

#eliminate pixels that have no surrounding pixel in the up and down direction
#eliminate pixels that have no surrounding pixels in the left and right
#each letter size 14 and 13?
#find starting and ending to optimize left and right- (20-110)? top and bottom-(4-22)?