from time import sleep,strftime
import os
wakemeup = input('幾點起床啦(e.g. 0700):')
while True:
	if strftime('%H%M') == wakemeup:
		os.system('spafly "{0}"'.format('#spotify_url'))
		break
	sleep(0.5)
