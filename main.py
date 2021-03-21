from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import *

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys("samsung phone")
driver.find_element(By.XPATH, "//*[@id='nav-search-bar-form']/div[3]/div").click()
driver.find_element(By.XPATH, "//*[@id='p_89/Samsung']/span/a/span").click()
driver.implicitly_wait(10)
phones = driver.find_elements(By.XPATH, "//span[contains(@class,' a-color-base a-text-normal')]")
phones_prices = driver.find_elements(By.XPATH, "//span[contains(@class,'a-price-whole')]")

mobilePhone = []
mobilePrices = []
for mobiles in phones:
    print(mobiles.text)
    mobilePhone.append(mobiles.text)

for prices in phones_prices:
    print(prices.text)
    mobilePrices.append(prices.text)

no_of_phones = len(phones)
no_of_prices = len(phones_prices)

final = zip(mobilePhone, mobilePrices)

# for data in list(final):
#   print(data)

wb = Workbook()
wb["Sheet"].title = 'samsung data'
sh1 = wb.active

sh1.append(["LIST OF MOBILES", "PRICES"])
for x in list(final):
    sh1.append(x)

wb.save("samsungList.xlsx")

print("the total no of phones is equal to :" + str(no_of_phones))
print("the total no of prices :" + str(no_of_prices))

driver.quit()
