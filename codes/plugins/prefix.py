# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def prefix(type, source, parameters):
	if not parameters:
		reply(type, source, u'Command Prefix: '+Prefix)
		return
	else:
		add_gch(source[1], DEFAULT_NICK, parameters)
		#join_groupchat(source[1], parameters)
	reply(type, source, u'Command Prefix: '+Prefix)
register(prefix, Prefix+'prefix', 0)
