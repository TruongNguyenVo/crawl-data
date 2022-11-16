import json, sys, os, time,re,colorama,requests,time,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Khai báo browser
browser = webdriver.Chrome(executable_path= 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

#mở chrome profile 3- Profile Cần Thơ
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
options.add_argument('profile-directory=Profile 3')
options.add_argument('--mute-audio')
driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)


# mở trang facebook cần crawl

link_crawl = 'https://www.facebook.com/groups/ReviewAnUongCanTho/posts/1122612675107751/'
dr = driver.get(link_crawl)
time.sleep(5)

#========vào mục bình luận=========
#bấm vào mục phù hợp nhất hay bình luận liên quan nhất
try:
	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span').click()
except:
	driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span').click()
time.sleep(3)
#bấm vào mục tất cả bình luận
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/div[1]/span').click()
time.sleep(3)

#bấm vào mục xem thêm n bình luận nữa
end = True
while end == True:
	try:
		driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[8]/div/div[5]/div/div/div[2]/div[4]/div/div[2]/span/span').click()
		time.sleep(5)
		end = True 
	except:
		print('Đã tải hết bình luận')
		end = False

# print('Đã thoát khỏi vòng lặp')
#tìm tất cả comment và ghi ra màn hình

#in tất cả các link người comment
tags_link = '//a[@aria-hidden = "false"]'
link_list =driver.find_elements_by_xpath(tags_link)



#in tất cả các tên 
tags_name = '//span[@class = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u"]'
name_list = driver.find_elements_by_xpath(tags_name)
temp = 0
tep = open('link_thu_excel.csv',"a+",encoding='utf')

#đọc hết tep link_thu
dong = tep.readline().strip()
while dong != '':
	dong = tep.readline().strip()

#ghi vào tệp
for i in link_list:

	link = i.get_attribute('href')
	name = name_list[temp].text
	text = str(name)+","+str(link)+'\n'
	tep.write(text)
	print("name facebook: " +str(name)+","+"link facebook: "+str(link)+'\n')
	temp = temp +1


# #cấu trúc tags "//tên_thẻ[@tên_loại_thẻ = 'tên thuộc tính đó']" ==> 
# tags = "//div[@class = 'x1n2onr6']"

# comment_list = driver.find_elements_by_xpath(tags)
# # print(comment_list)

# #in từng comment ra màn hình

# for comment in comment_list:
# 	#hiển thị tên người và nội dung cách nhau dấu :
# 	#người post
# 	tag_poster = '//div[@class = "x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1pi30zi"]'
# 	link_facebook = driver.find_element_by_xpath(tag_poster).get_attribute('href')
# 	print("link facebook: " +str(link_facebook))

# 	# class_tags_name = '//span[@class = "x3nfvp2"]'
# 	# name_poster = driver.find_element_by_xpath(class_tags_name)
# 	# print("name poster: "+str(name_poster.text))

# 	# tags_content = '//div[@class = "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"]'
# 	# content_poster = driver.find_element_by_xpath(tags_content)
# 	# print("content: "+ str(content_poster.text))

# 	# print(content_poster.text)


#=======================================lấy link facebook========
# # #cấu trúc tags "//tên_thẻ[@tên_loại_thẻ = 'tên thuộc tính đó']" ==> 



#================================


print('Done')
time.sleep(10)




# xt0psk2
# xt0psk2					

# x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz
# xqcrz7y x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x1w0mnb xr9ek0c x1n2onr6
# xt0psk2

# x1n2onr6 x4uap5 x18d9i69 x1swvt13 x1iorvi4 x78zum5 x1q0g3np x1a2a7pz
# xqcrz7y x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x1w0mnb xr9ek0c x1n2onr6
# xt0psk2

# x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz
# xqcrz7y x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x1w0mnb xr9ek0c x1n2onr6
# xt0psk2

# x1n2onr6 x1iorvi4 x4uap5 x18d9i69 x1swvt13 x78zum5 x1q0g3np x1a2a7pz
# xqcrz7y x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x1w0mnb xr9ek0c x1n2onr6
# xt0psk2

#mở chrome profile 3
# options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=D:\\a tool\\profile_tds\\User Data')
# options.add_argument('profile-directory=Profile 3')
# options.add_argument('--mute-audio')
# driver = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\Chrome\\Application\\chromedriver.exe', options=options)


# # mở trang facebook cần crawl
# link = 'https://www.tiktok.com/@sao.bongda/video/7025214955632856347'
# dr = driver.get(link)
# time.sleep(5)

# tags1 = '//div[@class = "tiktok-bylcfd-StyledUserLinkName e1g2efjf4"]'
# link_list =driver.find_elements_by_xpath(tags1)
# for i in link_list:
# 	tags_link1 = '//a[@class = "tiktok-bylcfd-StyledUserLinkName e1g2efjf4"]'
# 	temp = driver.find_element_by_xpath(tags_link1).get_attribute('href')
# 	print(temp)
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
# tiktok-bylcfd-StyledUserLinkName e1g2efjf4
