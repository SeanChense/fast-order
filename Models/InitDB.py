import Model
import names
import random

session = Model.session

# #clear tables
# tables = session.query(Model.TTable).all()
# for table in tables:
# 	session.delete(table)
# 	session.commit()
# 	print "delete table %s" % table

# #clear users
users	= session.query(Model.User).all()
for user in users:
	session.delete(user)
	session.commit()
	print "delete user %s" % user

# init user resource
	# id 		= Column(Integer, primary_key=True)
	# name 	= Column(String(100))
	# age 	= Column(Integer)
	# gender	= Column(Integer) # 0 for boy, 1 for girl, 2 for others
	# password= Column(String(100))
	# avatar	= Column(String(100))
avatars = \
("http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_7926ec20-dd34-11e5-bfb9-cfe874d78ed7/banner_img_1459825668511.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_-KCIu2C8d0VKakRE0WS2/banner_img_1459826335108.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_11191720-ecde-11e5-be0c-736255f75a6a/banner_img_1459826315532.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_-KDMAcL0eOHqveMxdZ5Z/banner_img_1463520112187.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_0a870340-f96d-11e5-995c-1f7a52dfd439/banner_img_1459668323686.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_1ca204f0-f99d-11e5-9596-f1927f4bd785/banner_img_1459763801650.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_470418e0-fc8c-11e5-9952-253f4304608b/banner_img_1460036239140.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_0720b1e0-0130-11e6-b9ce-ffaedafbed0a/banner_img_1460525692417.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_90d5e690-0562-11e6-91ae-416a68add056/banner_img_1460983583593.jpg",
"http://xiaobandeng-production.img-cn-hangzhou.aliyuncs.com/talks/talk_b9bf8c40-0dec-11e6-96d3-9b6ed08c86ad/banner_img_1461924473392.jpg")
# def __init__(self, name, age, gender, password, avatar):
for url in avatars:
	user = Model.User(names.get_full_name(), 
					  random.randint(20, 50),
					  random.randint(0, 2),
					  names.get_full_name(),
					  url)
	session.add(user)
	print "add user %s" % user

session.commit()



# init table resource
# for x in xrange(1,50):
# 	table = Model.TTable(1, 2)
# 	User.session.add(table)
# 	User.session.commit()