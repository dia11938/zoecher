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
def version(type, source, parameters):
	nick=source[2]
	groupchat=source[1]
	me =groupchat+'/'+nick
	jid_domain=parameters.strip()
	nick_room=groupchat+'/'+parameters.strip()
	iq = xmpp.Iq('get')
	id='vers'+str(random.randrange(1000, 9999))
	globals()['version_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'jabber:iq:version');
	if parameters:
                if GROUPCHATS.has_key(source[1]):
                        nicks = GROUPCHATS[source[1]].keys()
                        nick = parameters.strip()
                        if not nick in nicks:
                                iq.setTo(nick)
                        else:
                                if GROUPCHATS[source[1]][nick]['ishere']==0:
                                        reply(type, source, u'Not found')
                                        return				
                                jid=groupchat+'/'+nick
                                iq.setTo(jid)
	else:
		jid=source[1]+'/'+source[2]
		iq.setTo(jid)
		nick=''
        JCON.SendAndCallForResponse(iq, version_answ, {'type': type, 'source': source, 'nick': nick})
        return

               
def version_answ(coze, res, type, source, nick):
	id = res.getID()
	if id in globals()['version_pending']:
		globals()['version_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	rep =''
	if res:
		if res.getType()=='error':
			if not nick:
				reply(type,source,u'Error!')
				return
			else:
				reply(type,source,u'Error! Service unavailable!')
				return
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
                                if not nick:
                                        rep = ''+name
                                else:
                                        rep = ''+name
                        if not version=='':
                                rep += ' '+ version
                        if not os=='':
                                rep += ' // '+ os
		else:
			rep = u'Error! Something not found!'
	else:
		rep = u'there is not such thing'
	reply(type, source, rep)
	
register(version, Prefix+'ver', 0)
