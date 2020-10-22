from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


driver = webdriver.Chrome()
driver.get("https://www.google.co.jp/imghp?hl=ko&tab=wi&authuser=0&ogbl") #Open browser
elem = driver.find_element_by_name("q")
elem.send_keys("동영배")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        #break if an error occurs
        try:
            driver.find_element_by_css_selector(".mye4qd").click() #Press "show mere results"
        except:
            break
    last_height = new_height


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try: #Pass if an error occurs
        image.click()
        time.sleep(2)
        imgurl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")#イメージurlを取る
        urllib.request.urlretrieve(imgurl, str(count) + ".jpg") #image download
        count = count + 1
    except:
        pass
driver.close()