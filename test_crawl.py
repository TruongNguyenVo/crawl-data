# from bs4 import BeautifulSoup
# import requests

# page = requests.get('https://www.facebook.com/motchutyeeuthuong/posts/pfbid0iyEXvVryzNt3spsMaKq1SRde4qFUU5YjALiPRKFunBJEphwYFuFGVsN5wZjxBpWZl')

# soup = BeautifulSoup(page.content,'lxml')
# # # print(soup.text)
# lists = soup.find_all('script')
# # # print(type(lists[3])) # type in bs4

# lists1 = str(lists[3])
# # print(lists1) #string

# #print all comment
# list_all_comment = []
# # all_comment = '<script nonce="tpTbSsb4" type="application/ld+json">{"\u0040context":"https:\/\/schema.org","\u0040type":"SocialMediaPosting","dateCreated":"2022-03-06T04:32:49-0800","dateModified":"2022-04-14T13:15:18-0700","identifier":"100075960804277;134439932431366;;9","articleBody":"B\u1ea3o b\u1ed1i bu\u1ed3n qu\u00e1 m\u00e0 b\u1ea3o b\u1ed1i khum n\u00f3i \ud83d\ude25\ud83d\ude25\ud83d\ude25","url":"https:\/\/www.facebook.com\/motchutyeeuthuong\/posts\/pfbid02npgF7AnoqgRybmfsGw741eYKt4EnW446x1vtfUgzzx5pYDPd8oK7ZLZL6icawpT6l","isPartOf":"https:\/\/www.facebook.com\/motchutyeeuthuong","headline":"B\u1ea3o b\u1ed1i bu\u1ed3n qu\u00e1 m\u00e0 b\u1ea3o b\u1ed1i khum n\u00f3i \ud83d\ude25\ud83d\ude25\ud83d\ude25 - M\u1ed9t Ch\u00fat Y\u00eau Th\u01b0\u01a1ng","interactionStatistic":[{"\u0040type":"InteractionCounter","interactionType":"https:\/\/schema.org\/CommentAction","userInteractionCount":16},{"\u0040type":"InteractionCounter","interactionType":"http:\/\/schema.org\/LikeAction","userInteractionCount":1068},{"\u0040type":"InteractionCounter","interactionType":"http:\/\/schema.org\/ShareAction","userInteractionCount":86},{"\u0040type":"InteractionCounter","interactionType":"http:\/\/schema.org\/FollowAction","userInteractionCount":8316}],"commentCount":16,"comment":[{"\u0040type":"Comment","identifier":"134930672382292","dateCreated":"2022-03-08T04:04:45-0800","text":"Ng\u01b0\u1eddi ta to x\u00e1c nh\u01b0ng t\u00e2m h\u1ed3n \u00edu \u0111u\u1ed1i l\u1eafm","mentions":null,"author":{"\u0040type":"Person","name":"L\u00e2m Thi\u00ean Ho\u00e0ng H\u1ea3i","url":"https:\/\/www.facebook.com\/haicon66666","identifier":"100067562083388"}},{"\u0040type":"Comment","identifier":"134928042382555","dateCreated":"2022-03-08T03:57:37-0800","text":"B\u1ea3o b\u1ed1i b\u1ecb t\u1ed5n th\u01b0\u01a1ng \ud83d\ude22\ud83d\ude22","mentions":null,"author":{"\u0040type":"Person","name":"Pham Vu Vo","url":"https:\/\/www.facebook.com\/people\/Pham-Vu-Vo\/100072037608760\/","identifier":"100072037608760"}},{"\u0040type":"Comment","identifier":"134930655715627","dateCreated":"2022-03-08T04:04:37-0800","text":"\ud83d\ude25\ud83d\ude25\ud83d\ude25","mentions":null,"author":{"\u0040type":"Person","name":"Nhung Trang","url":"https:\/\/www.facebook.com\/people\/Nhung-Trang\/100078904759218\/","identifier":"100078904759218"}},{"\u0040type":"Comment","identifier":"134929765715716","dateCreated":"2022-03-08T04:01:44-0800","text":"Ch\u01a1i g\u00ec m\u00e0 k\u00ec v\u1eady","mentions":null,"author":{"\u0040type":"Person","name":"S\u1ef9 Thanh","url":null,"identifier":"100003238234584"}},{"\u0040type":"Comment","identifier":"135446278997398","dateCreated":"2022-03-10T04:25:30-0800","text":"choi gi ki cuc vay","mentions":null,"author":{"\u0040type":"Person","name":"M\u00f9a Tam Thong","url":"https:\/\/www.facebook.com\/people\/M\u0025C3\u0025B9a-Tam-Thong\/100075700271336\/","identifier":"100075700271336"}}],"author":{"\u0040type":"Person","name":"M\u1ed9t Ch\u00fat Y\u00eau Th\u01b0\u01a1ng","identifier":100075960804277,"url":"https:\/\/www.facebook.com\/motchutyeeuthuong","image":null,"sameAs":"","address":null},"keywords":"b\u1ed1i,b\u1ea3o,bu\u1ed3n,qu\u00e1,khum,m\u00e0"}</script>'
# # arr2 = all_comment.split(",")
# # for i in arr2:
# # 	print(i)
# # 	print('========================')
# arr1 = lists1.split(',')
# for i in arr1:
# 	# print(i)
# 	list_all_comment.append(i)
# #xóa vị trí đầu và cuối chuỗi
# del list_all_comment[0]
# del list_all_comment[-1]

# dicts = {}
# print(list_all_comment)
# # for i in list_all_comment:
# # 	print(i)
# # 	print('======================')





from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.facebook.com/RioXbutnotmusicpage/posts/pfbid02YqMaFYs6yywBYvhZjDY6shqs1cNYzGRk4aLSqXVQ9tPRWrmqU1cfXVUhkaaR8YCBl')

soup = BeautifulSoup(page.content,'lxml')

print(soup.find_all('div'))
exit()
comment = soup.find('div',class_="xv55zj0 x1vvkbs x1rg5ohu xxymvpz")
# print(comment)