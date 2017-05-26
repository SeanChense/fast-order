#!/usr/bin/python
#coding:utf-8
import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import *
from Model.ErrorCode import *
from Qiniu.image_uploader import *
import json
import datetime, random

mod = Blueprint('image_helper', __name__, url_prefix='/image')

@mod.route("/upload", methods = ['POST'])
@superadmin_required
def upload_image(admin):
	image = request.files['image']
	image_name = get_image_name()
	image_path = '/tmp/' + image_name
	with file(image_path, 'wb') as f:
		f.write(image.read())
	upload_img(image_name, image_path)
	key = "http://oofm3g268.bkt.clouddn.com/" + image_name
	return jsonify({
		"status":0,
		"data": key
		})

def get_image_name():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + (str(random.randrange(100,999))) + '.jpeg'
