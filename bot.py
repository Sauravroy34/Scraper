from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import bs4
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=Options())


folder = input("please enter name of your folder")
name = input("enter name ")
url=  f"https://www.google.com/search?sca_esv=8c1933b810334ae6&sxsrf=ACQVn0-PqT1f4rpdlMjEhuJBKMXqrmFjqA:1713776373545&q={name}&uds=AMwkrPtPoxXqS2m_DIc-uP6TtTVfxNvZApPtMZugHjMhnyWj_7LDZwmfQWP52Z6DF1aoIasK4CysKdE5rz1AGYcmno4V0j4Pr4b97J0GA_j6kGNBwUjfU_yHn3dM2I-oGnhC9Jj89X3-WiqxKZmt37MuysqiQrGWNFi1gNedzN9vHQdAkRdjGTdfAEZMPjLNJTqM-Xyqi4pWoJM1Sm83A6Y6b6IqZSwi5HoIJM3mLTAv6dLpyP6ASo52EPM687tR1NVcM2n4H840ru5f_kYHIv3psdZQpqi3Cg&udm=2&prmd=isvnmbtz&sa=X&ved=2ahUKEwjFueC_utWFAxW7g2MGHeZLA8oQtKgLegQIDhAB"
driver.get(url)
# target_div =driver.find_element(By.ID,"res")
# list_img = driver.find_elements(By.TAG_NAME,"img")
no_of_times = int(input("enter a number"))
soup = bs4.BeautifulSoup(driver.page_source,"html.parser")
x = 0
j = 0
while x!= no_of_times:


    # target_div = soup.find(id="rcnt")
    # req = requests.get(driver.page_source,"lxml")

    list_img = soup.find_all("img",src = True)
    print(list_img)
    for i in list_img:

        try:
            if ".gif" not in i["src"] or "google.com" not in i["src"]:
                img = requests.get(i["src"])
                j = j +1
                with open(f"images/{name} {j}.png" ,"wb") as f:
                    f.write(img.content)
                    x = x+1
                    if x == no_of_times:
                        break
        except:
            pass
    driver.execute_script("window.scrollBy(0,300)")
    time.sleep(5)

