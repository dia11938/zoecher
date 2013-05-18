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

LAST_REG_JID={}
JID_REG_TIME={}

def generate_reg(_len = None, sg = None):
  if sg == None:
    sg = 'aoeuizxcvbnmsdfghjklqwrtyp1234567890-.*!%~+'
  if _len == None:
    _len = random.Random().randint(1, 100)
  s = ''
  l = len(sg)
  while _len > 0:
    s += sg[random.Random().randint(0, l - 1)]
    _len -= 1
  return s

  
def hnd_gonew_jid(type,source,parameters):
  l = parameters.lower()
  s= parameters.split()
  jid=get_true_jid(source[1]+'/'+source[2])
  if jid in JID_REG_TIME:
    if time.time() - JID_REG_TIME[jid]['time']<10:
      reply(type,source,u'Wait 10 Seconds to Register another JID')
      return
    else:
      JID_REG_TIME[jid]['time']=time.time()
  if not jid in JID_REG_TIME:
    JID_REG_TIME[jid]={'time':time.time()}
  if not parameters:
    reply(type,source,u'and?')
    return
  if len(parameters)>50:
    reply(type,source,u'???')
    return
  if not l.count(u'@')>0:
    reply(type,source,u'Wrong Order!')
    return
  if not l.count(u'.')>0:
    reply(type,source,u'Wrong Order!')
    return
  aka=l.split('@')
  dom=aka[1].split()[0]
  reply(type,source,'Ok')
  LAST_REG_JID[source[1]+'/'+source[2]]={}
  pas = generate_reg(random.Random().randint(1,10))
  if l.count(' ')>0:
    pas = s[1]
  name, domain, password, newBotJid, mainRes = aka[0], dom, pas, 0,'zOeCher-bot'
  print u'START'
  node = name
  jid = xmpp.JID(node=node, domain=domain, resource=mainRes)
  cl = xmpp.Client(jid.getDomain(), debug=[])
  con = cl.connect()
  if not con:
    reply(type,source,u'Can\'t connect to '+s[0])
    return
  cl.RegisterHandler('message', hnd_newreg_Hnd)
  try:
    xmpp.features.register(cl, domain, {'username': node, 'password':password})
    print u'Registered'
  except:
    reply(type,source,u'Registered: '+unicode(JCON.lastErr)+', '+unicode(JCON.lastErrCode))
  try:
    au=cl.auth(jid.getNode(), password, jid.getResource())
    if not au:
      reply(type,source,u'This JID registered or exceeded the time limit')
      return
  except UnicodeEncodeError:
    reply(type,source,u'Error Encoding. [Must be in UTF8]')
    return
  cl.sendInitPresence()
  reply(type,source,u'Registered:\nJID: '+node+'@'+domain+u'\nPassword: '+password)
  threading.Thread(None, hnd_regs_timer, 'at'+str(random.randrange(0, 999)), (type, source)).start()
  while LAST_REG_JID:
    cl.Process(1)
  print 'unavibile'
  try:
    cl.disconnect()
  except:
    pass

def hnd_regs_timer(cl):
  time.sleep(10)
  try:
    cl.disconnect()
  except:
    pass
  
    
def hnd_newreg_Hnd(cl,mess):
  print '1 mess!'
  try:
    body=mess.getBody()
    if LAST_REG_JID:
      for x in LAST_REG_JID:
        msg(x,body[:450])
        del LAST_REG_JID[x]
  except (RuntimeError,IOError,AttributeError):
    pass
        
    
  
register(hnd_gonew_jid, Prefix+'regjid', 5)
