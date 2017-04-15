# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import uuid

import sys 
sys.path.append('..') 
import secret_config

#需要填写你的 Access Key 和 Secret Key
access_key = secret_config.qiniu_ak
secret_key = secret_config.qiniu_sk

#构建鉴权对象
q = Auth(access_key, secret_key)

def upload_img(key, localfile):
	#要上传的空间
	bucket_name = 'fastorder'
	#生成上传 Token，可以指定过期时间等
	token = q.upload_token(bucket_name, key, 3600)

	ret, info = put_file(token, key, localfile)
	print(info)
	print
	print ret



# key = uuid.uuid1()
# upload_img(key, "../test.png")
# print 'url is http://oofm3g268.bkt.clouddn.com/'+str(key)
