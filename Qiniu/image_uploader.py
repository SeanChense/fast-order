# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

import sys 
sys.path.append('..') 
import secret_config

#需要填写你的 Access Key 和 Secret Key
access_key = secret_config.qiniu_ak
secret_key = secret_config.qiniu_sk

#构建鉴权对象
q = Auth(access_key, secret_key)

print q

#要上传的空间
bucket_name = 'fastorder'

#上传到七牛后保存的文件名
key = 'my-python-logo.png';

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = '../test.png'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
