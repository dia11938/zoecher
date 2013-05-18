# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def known(type, jid, nick, text):
	merge_age()
	text = text.strip()
	if text == '': text = nick
	mdb = sqlite3.connect(agestatbase)
	cu = mdb.cursor()
	real_jid = cu.execute('select jid from age where room=? and (nick=? or jid=?)',(jid,text,text.lower())).fetchone()
	if real_jid:
		nicks = cu.execute('select nick from age where room=? and jid=?',(jid,real_jid[0])).fetchall()
		if text == nick: msg = u': '
		else: msg = u' '+text+u'  '
		for tmp in nicks:
			msg += tmp[0] + u', '
		msg = msg[:-2]
	else: msg = u''
	send_msg(type, jid, nick, msg)

global execute

register(known,'known', 2)
