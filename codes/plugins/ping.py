# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

ping_pending=[]
def handler_ping(type, source, parameters):
	nick=parameters
	groupchat=source[1]
	iq = xmpp.Iq('get')
	id = 'p'+str(random.randrange(1, 1000))
	globals()['ping_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'jabber:iq:version');
	if parameters:
		if GROUPCHATS.has_key(source[1]):
			nicks = GROUPCHATS[source[1]].keys()
			param = parameters.strip()
			if not nick in nicks:
				iq.setTo(param)
			else:
				if GROUPCHATS[groupchat][nick]['ishere']==0:
					reply(type, source, u'was he here? :-O')
					return
				param=nick
				jid=groupchat+'/'+nick
				iq.setTo(jid)
	else:
		jid=groupchat+'/'+source[2]
		iq.setTo(jid)
		param=''
	t0 = time.time()
	JCON.SendAndCallForResponse(iq, handler_ping_answ,{'t0': t0, 'mtype': type, 'source': source, 'param': param})
	return

def handler_ping_answ(coze, res, t0, mtype, source, param):
	id = res.getID()
	if id in globals()['ping_pending']:
		globals()['ping_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	if res:
		if res.getType() == 'result':
			t = time.time()
			rep = u'Pong from '
			if param:
				rep += param
			else:
				rep += u'you'
			rep+=u' '+str(round(t-t0, 1))+u' Second\'s'
		else:
			rep = u'Error! No pong, no version...'
	reply(mtype, source, rep)
	
register(handler_ping, Prefix+'ping', 0)
