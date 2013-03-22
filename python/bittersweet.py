#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import time

import tweepy

from daemon import Daemon
from data import voices
import config

class BittersweetDaemon(Daemon):
	def run(self):
		auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
		auth.set_access_token(config.access_key, config.access_secret)
		api = tweepy.API(auth)

		while True:
			try:
				api.update_status(random.choice(voices))
			except:
				continue
				
			time.sleep(1800)

if __name__ == "__main__":
	import sys

	daemon = BittersweetDaemon('/tmp/lalasweetbot.pid')

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)