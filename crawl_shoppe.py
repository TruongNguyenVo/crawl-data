import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver # thêm thư viện webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #thêm thư viện keys cho máy
from datetime import datetime # thêm thư viện datetime để lấy thời gian thực
def rundelay(k):
  while (k>0):
    print('                                        ', end='\r')
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')
    time.sleep(1)
    k=k-1
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')


# link_crawl = input('nhap link can crawl: ')




# #Khai báo browser
# browser = webdriver.Chrome(executable_path= 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

# #mở chrome profile 3- Profile Cần Thơ
options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
# options.add_argument('profile-directory=Profile 3')
# options.add_argument('--mute-audio')
# driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)
# # driver.maximize_window() #khong set full man hinh
# driver.set_window_size(700,1000)
# options.headless = True # chạy ngầm

# mở chrome lên
driver = webdriver.Chrome(options=options,executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.set_window_size(700,1000)
driver.maximize_window()

# #mở trang web shoppe
dr = driver.get('https://shopee.vn/')
time.sleep(10)
###########################################
# user = driver.find_element_by_id("email") #tìm kiểu của tài khoản(sau chữ id)
# user.send_keys(tk)#điền tài khoản

# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")


##########################################################
#nhập món cần crawl vào mục tìm kiếm
items_crawl = 'áo polo nam'
driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div[2]/div/div[1]/div[1]/div/form/input").send_keys(items_crawl)
rundelay(3)

#tắt poster quảng cáo và nhấn nút enter
while(True):
	print('TURN OFF THE POSTER SHOPPE IF THIS APPEAR!!')
	rundelay(5)
	try:
		driver.find_element(By.XPATH,'//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/button').click()

		break
	except:

		pass
rundelay(10)
#nhấn vào mục giá
# driver.find_element(By.CLASS_NAME, "shopee-svg-icon icon-arrow-down-small").click()
# rundelay(2)
# #nhấn vào mục giá từ thấp đến cao
# driver.find_element(By.CLASS_NAME,"select-with-status__dropdown-item select-with-status__dropdown-item--with-tick").click()
# rundelay(2)

link_price_toptodown = str(driver.current_url)
page = 1 #crawling page 1
driver.get(link_price_toptodown + '&order=asc&page='+str(page)+'&sortBy=price')
#cuộn 4 lần mỗi lần 2650
driver.execute_script("window.scrollTo(0,2650)")
rundelay(3)
for i in range(0,5):
	driver.execute_script("window.scrollTo(0, window.scrollY + 1200)")
	rundelay(3)



rundelay(5)
#tìm tất cả link sản phẩm
link = '//a[@data-sqe = "link"]'
link_item_list =driver.find_elements_by_xpath(link)

#tìm tất cả các tên các sản phẩm
name_items = '//div[@class = "ie3A+n bM+7UW Cve6sh"]'
name_item_list = driver.find_elements(By.XPATH, name_items)

#tìm tất cả các max_giá các sản phẩm
price_items = '//span[@class = "ZEgDH9"]'
price_items_list = driver.find_elements(By.XPATH, price_items)

#tìm tất cả các mục đã bán bao nhiêu sản phẩm
sold_item = '//div[@class = "r6HknA uEPGHT"]' #các sản phẩm đã bán
sold_item_list = driver.find_elements(By.XPATH, sold_item)

#mở tệp
tep = open('D:\\a tool\\DATACT\\data_shoppe.csv',"w+",encoding='utf')
tieude = "Name,Price,Sold,Date_Crawl,Link_Item"+'\n'
tep.write(tieude)
#đọc hết tệp
dong = tep.readline().strip()
while dong != '':
	dong = tep.readline().strip()

temp1 = 0
for i in link_item_list:
	if temp1 == 0:
		temp1 = temp1 +1
		pass

	else:
		try:
			link = i.get_attribute('href')
			name = name_item_list[temp1-1].text
			price = price_items_list[temp1-1].text
			sold = sold_item_list[temp1-1].text

			print('===========================================')
			print('link'+ str(temp1)+':\t' + str(link))

			print('===========================================')
			print('tên'+ str(temp1)+':\t' + str(name))

			print('===========================================')
			print('giá'+ str(temp1)+':\t' + str(price))

			print('===========================================')
			print('đã bán'+ str(temp1)+':\t' + str(sold))

			print('===========================================')
			# #in ra ngày tháng năm, giờ phút giây
			# date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
			#in ra ngày tháng năm
			date = datetime.today().strftime('%Y-%m-%d')
			print('ngày lấy dữ liêu: '+':\t' + date)

			#xử lý dữ liệu trước khi ghi vào tệp
			text = str(name)+","+str(price)+","+str(sold)+","+str(date)+","+str(link)+'\n'

			#ghi dữ liệu vào tệp
			tep.write(text)
			temp1 = temp1+1
		except IndexError:
			pass
		except:
			print('Lỗi rồi')
			exit()





driver.quit()


# time.sleep(10000)


# VTjd7p whIxGK
# VTjd7p whIxGK