# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def ban_everywhere(type, source, jid):
	gch=source[1]
	for gch in GROUPCHATS.keys():
	    order_banjid(gch, jid, u'by zOeCher!')
	    reply(type, source, u'Jid '+jid+' has been banned in '+str(len(GROUPCHATS.keys()))+' conference\'s.')
	    return


def member_everywhere(type, source, jid):
	gch=source[1]
	for gch in GROUPCHATS.keys():
	    order_member(gch, jid, u'by zOeCher!')
	    reply(type, source, u'Jid '+jid+' has been set to affiliation Member in '+str(len(GROUPCHATS.keys()))+' conference\'s.')
	    return



def order_unban(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':'none'})
	iq.addChild(node=query)
	JCON.send(iq)

def order_banjid(groupchat, jid, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('ban'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'jid':jid, 'affiliation':'outcast'})
	ban.setTagData('reason', u'by zOeCher!')
	iq.addChild(node=query)
	JCON.send(iq)

def order_member(groupchat, jid, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID(str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'jid':jid, 'affiliation':'member'})
	ban.setTagData('reason', u'by zOeCher!')
	iq.addChild(node=query)
	JCON.send(iq)

def order_unmember(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID(str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':"none"})
	iq.addChild(node=query)
	JCON.send(iq)


register(member_everywhere, Prefix+'glob_member', 8)
register(ban_everywhere, Prefix+'glob_ban', 8)
