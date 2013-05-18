# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################


def stats_get(type, source, parameters):
		groupchat = source[1]
		iq = xmpp.Iq('get')
		iq.setQueryNS('http://jabber.org/protocol/stats')
		if parameters!='':
			iq.setTo(parameters.strip())
		else:
			iq.setTo(CONNECT_SERVER)
			parameters=CONNECT_SERVER
		JCON.SendAndCallForResponse(iq,first_stats,{'parameters':parameters,'type':type,'source':source})

def first_stats(coze,res,parameters,type,source):
	qu=res.getQueryChildren()
	if res.getType()=='error':
		reply(type,source,u'Error! Remote server not found!')
		pass
	elif res.getType()=='result':
		iq = xmpp.Iq('get')
		iq.setQueryNS('http://jabber.org/protocol/stats')
		iq.setQueryPayload(qu)
		iq.setTo(parameters)
		JCON.SendAndCallForResponse(iq,second_stats,{'parameters':parameters,'type':type,'source':source})
	else:
		reply(type,source,u'Timed out!')

def second_stats(coze,stats,parameters,type,source):
	pay=stats.getQueryPayload()
	if stats.getType()=='result':
		result=u'Server Statics ' + parameters + ':\n'
		for stat in pay:
			result=result+stat.getAttrs()['name']+': '+stat.getAttrs()['value'] + ' '+stat.getAttrs()['units'] + '\n'
			
		reply(type,source,result.strip())

register(stats_get, Prefix+'stats', 3)
