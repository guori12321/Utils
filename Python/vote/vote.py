#coding=utf-8
import sys,re,os
import gevent
import gevent.monkey;gevent.monkey.patch_all();
import gevent.queue
import requests
from pyquery import PyQuery

ip_Q = gevent.queue.Queue()

PORT = ['8080','80','43','3128','43']

def get_proxy():
	try:
		while True:
			url = url_Q.get(timeout=1)
			r = requests.get(url)#plz set timeout
			r.encoding='gb2312'
			d = PyQuery(r.text)
			for item in d("#proxylisttb table tr td"):
				ip = item.text
				if ip and re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip):
					ip_Q.put(ip)
					print ip
	except gevent.queue.Empty:
		print 'get_proxy quit!'

def vote():
	pass #do as your wish
	
def vote_

if __name__ == '__main__':
	get_proxy("http://www.cnproxy.com/proxy1.html")
