import pandas as pd
import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
s = requests.Session()
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
options.add_argument('profile-directory=Profile 3')
options.add_argument('--mute-audio')
driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)
driver.maximize_window()
# from selenium import webdriver # thêm thư viện webdriver
# from selenium.webdriver.common.keys import Keys #thêm thư viện keys cho máy

# tk ="vohoangduy0596@gmail.com"
# mk ="08nguyen16396742"

# # mở chrome lên
# driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
# driver.maximize_window()

# #mở trang web
# driver.get("https://www.facebook.com")

# #điền tài khoản

# user = driver.find_element_by_id("email") #tìm kiểu của tài khoản(sau chữ id)
# user.send_keys(tk)#điền tài khoản
# time.sleep(5)
# #điền mật khẩu
# password = driver.find_element_by_id("pass") #tìm kiểu của mật khẩu(sau chữ id)
# password.send_keys(mk) #điền mật khẩu
# time.sleep(5)
# #nhấn enter
# password.send_keys(Keys.ENTER)
# time.sleep(5)

df = pd.read_csv('data_cantho.csv')
tep_ghigoikb = open('D:\\a tool\\DATACT\\data_cantho_dagoikb.txt','a',encoding='utf')
# print(df)
saved_column = df['Link'] #you can also use df['column_name']
# print(type(saved_column))
def ktra_ketban(link):
	tepktra = open('data_cantho_dagoikb.txt')
	tep_link = tepktra.read()
	# print(y)
	link_list = tep_link.split(',')
	for link_ktra in link_list:
		# print(link_ktra)
		# print(link)
		if link == link_ktra:
			return True
	return False

def rundelay(k):
  while (k>0):
    print('                                        ', end='\r')
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')
    time.sleep(1)
    k=k-1
    print(' \033[1;31m=> \033[1;32m Đang Đợi Delay Khoảng:   '  +str(k), end='\r')

#convert to list
link_list = saved_column.tolist()
for link in link_list:
	# dr = driver.get(link)
	# time.sleep(100)
	# tep_ghigoikb.write(link + ',')
#	link1 = 'https://www.facebook.com/groups/220729368629424/user/100015509047388/?__cft__[0]=AZVFuqjdv6FSnDFQ4Gk4Nj8L0KfFnkZn-YmkRROzhyos_CrHpcDkpJOwqYVO7XXALB1QVlcJkJKoEIq-fFl8GvgYSnMFzKuMx-iK8vSlsU_7lz-liCMVrw5FXyCDQdM0i6sh6WGWMHpASiSIXGWxckEd&__tn__=R]-R'

	ktra = ktra_ketban(link)
	# print(ktra)
	# exit()
	if ktra == False:
		dr = driver.get(link)
		time.sleep(3)
		try:
			#nếu nút kết bạn nằm ở ô 1 thì sài lệnh này
#			driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div[2]/span/span').click()
			#nếu nút kết bạn nằm ở ô 2 thì sài lệnh này
			driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span').click()
			tep_ghigoikb.write(str(link) + ',')
			print('đã qua dòng ghi')
			print('Requests: ',link)
		except:
			tep_ghigoikb.write(str(link) + ',')
			print('đã qua dòng ghi')
			print('Error: ',link)
		rd_delay = random.randint(10,60)
		rundelay(rd_delay)

	




