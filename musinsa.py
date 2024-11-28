from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# chrome_driver_path = '/Users/skeptical/chromedriver-mac-arm64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



url = 'https://www.musinsa.com/app/mujinjangsale/special'  # 크롤링하려는 웹사이트의 URL로 변경
driver.get(url)
flag = True
while(flag):
    try:
        # WebDriverWait 초기화 (최대 10초 대기)
        wait = WebDriverWait(driver, 3)
        
        # 클래스명이 'total_amount' 또는 'total_number'인 span 요소 찾기
        span_elements = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "span.total_amount")
        ))
        
        # 각 span 요소의 텍스트 출력
        for span in span_elements:
            print(f"클래스: {span.get_attribute('class')}, 텍스트: {span.text}")
            value = int(span.text.replace(",","")) 
            if value >173000000000:
                print("yes")
                flag = False
            else :
                print(value)
                time.sleep(5)
                
                

    except Exception as e:
        print(f"오류 발생: {e}")

driver.quit()
