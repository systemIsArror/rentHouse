#coding:utf-8]
import os

#Application配置函数
settings = dict(
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		cookie_secret="M8QBeJGVT4OaBAVuobeJw1szoyFxb0dsr0O4Ml9bJgY=",
		xsrf_cookies=True,
		debug=True
	)

#数据库配置参数
mysql_options = dict(
		host="127.0.0.1",
		database="ihome",
		user="root",
		password="atguigu",
	)

#redis配置参数
redis_options = dict(
		host="127.0.0.1",
		port=6379
	)

#日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"

#密码加密密钥
passwd_hash_key = "kyBm33kPRGSKnpLhlHw98vqhslXnf0IErhNKAHMQ5qY="
