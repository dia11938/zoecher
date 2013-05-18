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


def get_old_list(type,source):
        if check_file(source[1],'memberlist.db'):
                file='history/'+source[1]+'/memberlist.db'
                fp=open(file,'r')
                txt=eval(fp.read())
                fp.close()
                n=0
                if txt:
                        for x in txt:
                                n+=1
                                old_member(source[1], x, source[2])
                        reply(type,source,u'Memberlist reduced '+unicode(n))

def cp_memberlist(type,source,parameters):
        if len(parameters)>50:
                return
        if not parameters.count(' '):
                reply(type,source,u'what?')
                return
        chat=parameters.split()[1]
        try:
                file='history/'+chat+'/memberlist.db'
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
                old_member(source, x, source[2])
        reply(type,source,u'Copied '+unicode(n))
                                
def hnd_memberlist(type, source, parameters):
        if source[1] not in GROUPCHATS:
                return
        body=parameters.lower()
	nick = source[2]
	groupchat=source[1]
        if body.count(u'back'):
                get_old_list(type,source)
                return
        if body.count(u'copy'):
                cp_memberlist(type,source,parameters)
                return
	afl='member'
	iq = xmpp.Iq('get')
	id='item'+str(random.randrange(1000, 9999))
	globals()['spk_pending'].append(id)
	iq.setTo(groupchat)
	iq.setID(id)
	globals()['spk_pending'].append(id)
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	member=query.addChild('item', {'affiliation':afl})
	iq.addChild(node=query)
	JCON.SendAndCallForResponse(iq, handler_memberlist_answ, {'type': type, 'source': source, 'parameters': parameters})
	return


def handler_memberlist_answ(coze, res, type, source, parameters):
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
                        if check_file(source[1],'memberlist.db'):
                                file='history/'+source[1]+'/memberlist.db'
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
                                                reply(type,source,u'server not found')
                                                return
                                elif parameters.count(u'clear'):
                                        if jid==0 and serv==0:
                                                return
                                        else:
                                                UNMEMBER=[]
                                                UNMEMBER.extend(listall.split())
                                                for x in UNMEMBER:
                                                        order_now_member(source[1], x)
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
	#reply(type, source, sp)
        
def old_member(groupchat, jid, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'jid':jid, 'affiliation':'member'})
	ban.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)

def order_now_member(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':'none'})
	iq.addChild(node=query)
	JCON.send(iq)

	
register(hnd_memberlist, Prefix+'memberlist', 7, [''])
