# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################



import sqlite3 as db
import time, os, threading

TIMER_ID = {}

def check_jid(jid):
	parse_jid = jid.split('@')
	
	if len(parse_jid) == 2:
		if parse_jid[0] and parse_jid[1]:
			if parse_jid[1].count('.') >= 1 and parse_jid[1].count('.') <= 3:
				return True
			else:
				return False	
		else:
			return False
	else:
		return False

def queryinfo(dbpath,query):
	cursor,connection = None, None
	try:
		connection=db.connect(dbpath)
		cursor=connection.cursor()
		cursor.execute(query)
		result=cursor.fetchall()
		connection.commit()
		cursor.close()
		connection.close()
		return result
	except:
		if cursor:
			cursor.close()
		if connection:
			connection.commit()
			connection.close()
		return ''

def get_jids(gch, affiliation):
	iq=xmpp.Iq('get')
	ID = 'bot' + str(random.randrange(1000, 9999))
	iq.setID(ID)
	iq.setTo(gch)
	iq.setAttr('xml:encoding','utf-8')
	query = xmpp.Node('query') 
	query.setNamespace(xmpp.NS_MUC_ADMIN) 
	query.addChild('item', {'affiliation': affiliation}) 
	iq.addChild(node=query)
	
	response = JCON.SendAndWaitForResponse(iq, 10)
	
	ptype = response.getType()
	
	if ptype == 'result' and response.getID() == ID:
		return response

	
	
def admins(type, source, parameters):
	groupchat = source[1]
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'This command can be used only in the conference!')
		return

	resp = get_jids(groupchat, 'admin')
	njids = []
	
	if resp:
		njids = parse_stanza(resp)
	
	if type == 'public':
		reply(type, source, u'Look in PM!')
		
	if njids:
		rep = u'Admin List [Total: ' + str(len(njids))+ ']:\n' + '\n'.join(njids)
	else:
		rep = u'List admins empty!'
		
	reply('private', source, rep)
	
def owners(type, source, parameters):
	groupchat = source[1]
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'This command can be used only in the conference!')
		return

	resp = get_jids(groupchat, 'owner')
	njids = []
	
	if resp:
		njids = parse_stanza(resp)
	
	if type == 'public':
		reply(type, source, u'Look in PM!')
		
	reply('private', source, u'Owner List, [Total: ' + str(len(njids))+ ']:\n' + '\n'.join(njids))
	

	
def seen(type, source, parameters):
	groupchat = source[1]
	nick_jid = parameters.strip()
	curr_time = time.time()
	
	if not parameters:
		reply(type, source, u'Who?')
		return
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'This command can be used only in the conference!')
		return
	
	jid = ''
	nick = ''
	
	if check_jid(nick_jid):
		jid = nick_jid
	else:
		nick = nick_jid
	
	qnick = nick.replace('"','&quot;')
	
	if jid:
		qres = []
		
		for I in GROUPCHATS[groupchat]:
			rjid = GROUPCHATS[groupchat][I]['jid'].split('/')[0]
			
			if jid == rjid:
				if GROUPCHATS[groupchat][I]['ishere'] == 1:
					nick = I
					check_sql = 'SELECT nick,ujoin,uleave FROM users WHERE nick="%s"' % (qnick)
					qres = queryinfo('history/'+groupchat+'/users.db',check_sql)
					break
						
		if not qres:
			check_sql = 'SELECT nick,ujoin,uleave FROM users WHERE jid="%s" ORDER BY uleave' % (jid)
			qres = queryinfo('history/'+groupchat+'/users.db',check_sql)

		
		if qres:
			qres = list(qres[-1])
			gnick = qres[0].replace('&quot;','"')
			join_time = float(qres[1])
			leave_time = float(qres[2])
			
			if not GROUPCHATS[groupchat].has_key(gnick):
				seen_time = curr_time - leave_time
				here_time = leave_time - join_time
				rep = u'User '+ gnick + u' was here %s ago and stay in the conference about %s.' % (timeElapsed(seen_time), timeElapsed(here_time))
				reply(type, source, rep)
				return
			elif GROUPCHATS[groupchat].has_key(gnick):
				gjid = GROUPCHATS[groupchat][gnick]['jid'].split('/')[0]
				
				if GROUPCHATS[groupchat][gnick]['ishere'] == 0 and gjid == jid:
					seen_time = curr_time - leave_time
					here_time = leave_time - join_time
					rep = u'User '+ gnick + u' was here %s ago and stay in the conference about %s.' % (timeElapsed(seen_time), timeElapsed(here_time))
					reply(type, source, rep)
					return
				else:
					rep = u'Who?'
					reply(type, source, rep)
					return
					
			else:
				rep = u'User %s never been in this conference!' % (jid)
				reply(type, source, rep)
				return
		else:
			rep = u'User %s never been in this conference!' % (jid)
			reply(type, source, rep)	
	elif nick:
		check_sql = 'SELECT nick,ujoin,uleave,jid FROM users WHERE nick="%s"' % (qnick)
		qres = queryinfo('history/'+groupchat+'/users.db',check_sql)
		
		if qres:
			jid = list(qres[0])[3]
		
		gnick = ''
		
		for I in GROUPCHATS[groupchat]:
			rjid = GROUPCHATS[groupchat][I]['jid'].split('/')[0]
			
			if jid == rjid:
				if GROUPCHATS[groupchat][I]['ishere'] == 1:
					gnick = I
					break
	
		check_sql = 'SELECT nick,ujoin,uleave,jid FROM users WHERE jid="%s" ORDER BY uleave' % (jid)
		qres = queryinfo('history/'+groupchat+'/users.db',check_sql)
	
		if qres:
			qres = list(qres[-1])
			
			if not gnick:
				gnick = qres[0].replace('&quot;','"')
			
			join_time = float(qres[1])
			leave_time = float(qres[2])
			
			if not GROUPCHATS[groupchat].has_key(gnick):
				seen_time = curr_time - leave_time
				here_time = leave_time - join_time
				rep = u'User '+ nick + u' was here %s ago and stay in the conference about %s.' % (timeElapsed(seen_time), timeElapsed(here_time))
				reply(type, source, rep)
				return
			elif GROUPCHATS[groupchat].has_key(gnick):
				if GROUPCHATS[groupchat][gnick]['ishere'] == 0:
					seen_time = curr_time - leave_time
					here_time = leave_time - join_time
					rep = u'User '+ nick + u' was here %s ago and stay in the conference about %s.' % (timeElapsed(seen_time), timeElapsed(here_time))
					reply(type, source, rep)
					return
				else:
					rep = u'Who?'
					reply(type, source, rep)
					return
		else:
			rep = u'Users %s never been in this conference!' % (nick)
			reply(type, source, rep)
			
		
def getrealjid(type, source, parameters):
	groupchat=source[1]
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'This command can be used only in the conference!')
		return
	
	if not parameters:
		reply(type, source, u'And, who?')
		return
	
	nick = parameters.strip()
	
	sql = 'SELECT jid FROM users WHERE nick="%s";' % (nick.replace('"','&quot;'))
	qres = queryinfo('history/'+groupchat+'/users.db',sql)
	
	if not qres:
		reply(type,source,u'I don\'t know '+nick)
		return
	else:
		truejid=qres[0][0]
		
		if type == 'public':
			reply(type, source, u'Look in PM!')
			
	reply('private', source, u'Real JID '+nick+u': '+truejid)
		
		
def bot_uptime(type, source, parameters):
	if INFO['start']:
		uptime=int(time.time() - INFO['start'])
		rep,mem = u'- Uptime: '+timeElapsed(uptime),''
		if os.name=='posix':
			try:
				pr = os.popen('ps -o rss -p %s' % os.getpid())
				pr.readline()
				mem = pr.readline().strip()
				pr.close()
			except:
				pass
			if mem: rep += u'- Used Memory: %s Kb\n ' % mem
		(user, system,qqq,www,eee,) = os.times()
		rep += u'- CPU: * Spent %.2f Second\'s\n* System Wide Time: %.2f Second\'s\n* System Time and Eventually: %.2f Second\'s\n' % (user, system, user + system)
		rep += u'- Total Used Threads: %s\nActive Threads: %s' % (INFO['thr'], threading.activeCount())
	else:
		rep = u'Molding...'
	reply(type, source, rep)


register(getrealjid, Prefix+'realjid', 7, [''])
register(bot_uptime, Prefix+'botup', 3, [''])
register(seen, Prefix+'seen', 7, [''])
register(admins, Prefix+'admins', 7, [''])
register(owners, Prefix+'owners', 7, [''])
