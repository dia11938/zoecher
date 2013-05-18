# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

spk_pending=[]
spisok_pending=[]

def spisok_iq(type, source, parameters):
        if not parameters:
                reply(type,source,u'Invalid Order\nAvailable: - '+Prefix+'list owner\n - '+Prefix+'list admin\n- '+Prefix+'list member\n '+Prefix+'list outcast')
                return
        body=parameters.lower()
	nick = source[2]
	groupchat=source[1]
	afl=''
	if body.count(u'owner')>0:
                afl='owner'
        elif body.count(u'admin')>0:
                afl='admin'
        elif body.count(u'member')>0:
                afl='member'
        elif body.count(u'outcast')>0:
                afl='outcast'
        if afl=='':
                return
	iq = xmpp.Iq('get')
	id='item'+str(random.randrange(1000, 9999))
	globals()['spisok_pending'].append(id)
	iq.setTo(groupchat)
	iq.setID(id)
	globals()['spisok_pending'].append(id)
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'affiliation':afl})
	iq.addChild(node=query)
	JCON.SendAndCallForResponse(iq, sp_answ, {'type': type, 'source': source})


def sp_answ(coze, res, type, source):
	id=res.getID()
	if id in globals()['spisok_pending']:
		globals()['spisok_pending'].remove(id)
	else:
		print u'id does not match'
		return
	rep =''
	if res:
		if res.getType() == 'result':
                        print 'yahoo!'
			props = res.getChildren()[0].getChildren()
			sp='\n'
			n =0
			b=''
			c=''
			for p in props:
                                if p!='None':
                                        n+=1
                                        y = p.getAttrs()['jid']
                                        try:
                                                b=p.getTag('reason')
                                                c=b.getData()
                                        except:
                                                pass
                                        sp+= unicode(n)+') '+y+' '+c+'\n'
                        if sp=='\n':
                                reply(type,source,u'Empty')
                                return
                else:
                        reply(type,source,u'bummer (')
                        return
        else:
                reply(type,source,u'bummer (')
                return
        if type == 'public':
                reply(type,source,u'Sent to PM!')
	reply('private', source, sp)
	
register(spisok_iq, Prefix+'list', 7)


def hnd_getold_list(type,source):
        if check_file(source[1],'banlist.db'):
                file='history/'+source[1]+'/banlist.db'
                fp=open(file,'r')
                txt=eval(fp.read())
                fp.close()
                n=0
                if txt:
                        for x in txt:
                                n+=1
                                old_ban(source[1], x, source[2])
                        reply(type,source,u'Banlist reduced '+unicode(n))

def any_copy_banl(type,source,parameters):
        if len(parameters)>50:
                return
        if not parameters.count(' '):
                reply(type,source,u'what?')
                return
        chat=parameters.split()[1]
        try:
                file='history/'+chat+'/banlist.db'
                fp=open(file,'r')
                txt=eval(fp.read())
                fp.close()
        except:
                reply(type,source,u'I Can\'t find base of: '+chat)
                return
        if not txt:
                reply(type,source,u'Empty!')
                return
        n=0
        for x in txt:
                n+=1
                old_ban(source, x, source[2])
        reply(type,source,u'Copied '+unicode(n))
                                
def hnd_banl(type, source, parameters):
        if source[1] not in GROUPCHATS:
                return
        body=parameters.lower()
	nick = source[2]
	groupchat=source[1]
        if body.count(u'back'):
                hnd_getold_list(type,source)
                return
        if body.count(u'copy'):
                any_copy_banl(type,source,parameters)
                return
	afl='outcast'
	iq = xmpp.Iq('get')
	id='item'+str(random.randrange(1000, 9999))
	globals()['spk_pending'].append(id)
	iq.setTo(groupchat)
	iq.setID(id)
	globals()['spk_pending'].append(id)
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'affiliation':afl})
	iq.addChild(node=query)
	JCON.SendAndCallForResponse(iq, banlist_answ, {'type': type, 'source': source, 'parameters': parameters})
	return


def banlist_answ(coze, res, type, source, parameters):
	id=res.getID()
	if id in globals()['spk_pending']:
		globals()['spk_pending'].remove(id)
	else:
		print u'id does not match'
		return
	rep =''
	if res:
		if res.getType() == 'result':
                        #print 'yahoo!'
			props = res.getChildren()[0].getChildren()
			listserv=''
			listjid=''
			serv = 0
			jid = 0
			for p in props:
                                if p!='None':
                                        y = p.getAttrs()['jid']
                                        if y.count(u'@'):
                                                jid+=1
                                                listjid+=y+' '
                                        else:
                                                serv+=1
                                                listserv+=y+' '
                        if listserv=='' and listjid=='':
                                reply(type,source,u'Empty')
                                return
                        all=serv+jid
                        listall=listjid+listserv
                        if check_file(source[1],'banlist.db'):
                                file='history/'+source[1]+'/banlist.db'
                                fp=open(file,'r')
                                txt=eval(fp.read())
                                fp.close()
                                if parameters.count(u'serv'):
                                        if serv>0:
                                                txt=listserv.split()
                                                write_file(file, str(txt))
                                                reply(type,source,u'keeping a server '+unicode(serv))
                                                return
                                        else:
                                                reply(type,source,u'serv no found')
                                                return
                                elif parameters.count(u'clear'):
                                        if jid==0 and serv==0:
                                                return
                                        else:
                                                UNBAN=[]
                                                UNBAN.extend(listall.split())
                                                for x in UNBAN:
                                                        hnd_now_unban(source[1], x)
                                                reply(type,source,u'The Operation was successful.')
                                                return
                                else:
                                        if jid==0 and serv==0:
                                                return
                                        txt=listall.split()
                                        write_file(file, str(txt))
                                        reply(type,source,u'Stored')
                                        return

                        
                        
                else:
                        reply(type,source,u'bummer (')
                        return
        else:
                reply(type,source,u'bummer (')
                return
        
def old_ban(groupchat, jid, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'jid':jid, 'affiliation':'outcast'})
	ban.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)

def hnd_now_unban(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':'none'})
	iq.addChild(node=query)
	JCON.send(iq)

	
register(hnd_banl, Prefix+'banlist', 7)
