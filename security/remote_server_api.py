"""
this file should be the api of your remote server
for example, your login service from your company
e.g. provide email and password, send this information to your remote server
waiting for the response from remote server. If remote server authorized this email and password
then it will be ok to login this user.
"""

import hashlib

import requests

import logging
logger = logging.getLogger(__name__)

def md5(str):
	# 创建md5对象
	hl = hashlib.md5()

	# Tips
	# 此处必须声明encode
	# 否则报错为：hl.update(str)  Unicode-objects must be encoded before hashing
	hl.update(str.encode(encoding='utf-8'))

	print('MD5加密前为 ：' + str)
	print('MD5加密后为 ：' + hl.hexdigest())
	return hl.hexdigest()

def authenticate(username, password):
	"""

	:param username:
	:param password:
	:return:
	"""
	md5Pwd = md5(password)

	# server_url = "https://yourloginservice.com"
	# auth_url = '%s/auth' % server_url
	server_url = "http://192.168.101.130"
	auth_url = '%s/rpc/system/api/user/checklogin?username=%s&password=%s' % (server_url, username, md5Pwd)

	# param_dict = dict(login=username, password=password)
	# param_dict = dict(username=username, password=md5Pwd)
	headers = ""

	# this is an example of real world case
	auth_result = requests.post(
	    auth_url, json=None, headers=headers, verify=False)
	if auth_result.status_code != 200:
	    logger.warn("failed to auth user: %s, status: %s, response: %s " %
	                (username, auth_result.status_code, auth_result.text))
	    return None
	result_dict = auth_result.json()
	logger.info("auth user: %s, status: %s, response: %s, result_dict: %s " % (username, auth_result.status_code, auth_result.text, result_dict))
	if result_dict['code'] != 200:
		logger.warn("failed to auth user: %s, status: %s, response: %s " %
					(username, auth_result.status_code, auth_result.text))
		return None
	userinfo = dict(
	    username=username)
	return userinfo

	""" 
	# mock the server response here
	if username == 'Admin@example.com':
		userinfo = dict(username=username)
		return userinfo
	else:
		return None
	"""