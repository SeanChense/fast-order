#!/usr/bin/python
#coding:utf-8
import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import *
from Models.ErrorCode import *
from Qiniu.image_uploader import *
import json

mod = Blueprint('image_helper', __name__, url_prefix='/image')

@mod.route("/upload", methods = ['POST'])
@superadmin_required
def upload_image(admin):
	image = request.files['image']
	print 'look'
	print image
	with file('temp.jpeg', 'wb') as f:
		f.write(image.read())
	upload_img('test', 'temp.jpeg')
	return "ok"