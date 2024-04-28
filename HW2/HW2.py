# 導入必要的库
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 設置 Chrome 驅動程式的路徑和啟動 WebDriver
service = Service("C:/Users/user/anaconda3/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 打開目標網頁
driver.get("https://store.steampowered.com/search/?filter=topsellers")

# 等待網頁加載，確保所需元素已經存在於網頁中
# wait = WebDriverWait(driver, 10)
# books = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "table-td")))

# 獲取網頁源碼
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# 遊戲元素的定位
games = soup.find_all('a', class_='search_result_row')

# 解析網頁並抓取資料
data = []
index = 1

for game in games:
    try:
        # 提取遊戲名稱
        name = game.find('span', class_='title').text
        # 提取發行日期
        release_date = game.find('div', class_='col search_released responsive_secondrow').text.strip()
        # 提取圖片網址
        image_url = game.find('img')['src']
        # 提取價格
        price = game.find('div', class_='discount_final_price').text.strip()
        
        # 將解析的資料存儲到字典中，然後添加到列表
        temp_data = {
            "Name": name,
            "Release Date": release_date,
            "Price": price,
            # "ImageURL" : image_url
        }
        data.append(temp_data)
        
        index += 1
    except:
        continue

# 將抓取的資料轉換為 DataFrame，並保存為 CSV 檔案
df = pd.DataFrame(data)
df.to_csv("game.csv", encoding='utf_8_sig', index=False)

# 關閉瀏覽器
driver.quit()