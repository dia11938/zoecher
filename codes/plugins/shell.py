# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def shell(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('sh -c "%s" 2>&1' % (parameters.encode('utf8')))
		return_value = pipe.read()
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
	pipe.close
	reply(type, source, return_value)

def free_ram(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('sh -c "free -%s" 2>&1' % (parameters.encode('utf8')))
		return_value = pipe.read()
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
	pipe.close
	reply(type, source, return_value)

def net_ping(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('ping -c3 "%s" 2>&1' % (parameters.encode('utf8')))
		return_value = pipe.read()
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
	pipe.close
	reply(type, source, return_value)

def sh_silent(type, source, parameters):
	return_value='Ok'
	if os.name=='posix':
		pipe = os.popen('sh -c "%s" 2>&1' % (parameters.encode('utf8')))
		return_value = pipe.read()
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
	pipe.close
	reply(type, source, 'Ok')
	
register(sh_silent, Prefix+'sh_silent', 9)
register(net_ping, Prefix+'net_ping', 6)	
register(free_ram, Prefix+'free', 9)
register(shell, Prefix+'sh', 9)
