# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

invite_pending=[]

def invite(type, source, parameters):
	truejid,nick,reason='','',''
	if not parameters:
		reply(type,source,u'What?')
		return
	if not parameters.count('@'):
		nicks = GROUPCHATS[source[1]].keys()
		nick=parameters.split()[0]
		if not nick in nicks:
			reply(type,source,u'I don\'t know'+nick)
			return
		else:
			truejid=get_true_jid(source[1]+'/'+nick)
			reason=' '.join(parameters.split()[1:])
			reply(type,source,u'Invited!')
	else:
		truejid=parameters
	msg=xmpp.Message(to=source[1])
	id = 'inv'+str(random.randrange(1, 1000))
	globals()['invite_pending'].append(id)
	msg.setID(id)
	x=xmpp.Node('x')
	x.setNamespace('http://jabber.org/protocol/muc#user')
	inv=x.addChild('invite', {'to':truejid})
	if reason:
		inv.setTagData('reason', reason)
	else:
		inv.setTagData('reason', u'You have invited by '+source[2])
	msg.addChild(node=x)
	JCON.send(msg)
	reply(type,source,u'Invited!')

				
					
register(invite, Prefix+'invite', 8)
