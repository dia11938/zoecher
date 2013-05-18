# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################


version_pending=[]
def version2(type, source, parameters):
	nick = parameters
	groupchat=source[1]
	iq = xmpp.Iq('get')
	id='vers'+str(random.randrange(1000, 9999))
	globals()['version_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'jabber:iq:version');
	if parameters:
		jid=parameters.strip()
		iq.setTo(jid)
	JCON.SendAndCallForResponse(iq, version_answ2, {'type': type, 'source': source})
	return

               
def version_answ2(coze, res, type, source):
	id = res.getID()
	if id in globals()['version_pending']:
		globals()['version_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	rep =''
	if res:
		if res.getType() == 'result':
			name = 'None'
			version = 'None'
			os = 'None'
			props = res.getQueryChildren()
			for p in props:
				if p.getName() == 'name':
					name = p.getData()
				elif p.getName() == 'version':
					version = p.getData()
				elif p.getName() == 'os':
					os = p.getData()
			if name:
                                rep = name
                        if version:
                                rep += ' '+ version
                        if os:
                                rep += ' // '+ os
		else:
			rep = u'Error! Something not found!'
	else:
		rep = u'there is not such thing'
	reply(type, source, rep)
	
register(version2, Prefix+'ver2', 0)
