# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

from xmpp import *
from random import *
from sys import maxint
from time import *
from pdb import *
import os, xmpp, time, sys, time, pdb, urllib, threading, types, random

BOT_VER1 = {'botver': {'name': 'zOeCher `şỉłэŋŧ.ђєļľ', 'ver': '4.17.85', 'os': 'S60'}}
New_Serverz = 'war/otake_serv.db'
fp = open(New_Serverz, 'r')
New_Serverz = eval(fp.read())
fp.close()
zoecher_text = 'codes/plugins/spamtext'
fp = open(zoecher_text, 'r')
zoecher_text = eval(fp.read())
fp.close()
spam_text = zoecher_text['text']
VIPE = {}
GS=[]
silent = 0
nz = ['fuck-2-','fuck-3-','fuck-4-','fuck-5-','fuck-6-','fuck-1-','oxigyene','rebomerx','ersmndax','dexicorbn','jardonedvx','piuxerix','teuroicx','rexmopid','surexve','evrixom','teckenzo','zoo_00','zee_00','zoo_01','zoo_02','zoo_03','zoo-00','zoo-01','zoo-02','zoo-03','nokia-502','nokia-501','jajejoa','madedee','daiked','iadenan','kaeload','sadlale','hadasloii','hadfek','arabicless','santaless','santaless-1','santaless-2','santaless-3','santaless-4','arabicless-1','arabicless-2','zoecher-1-bot','bading','activito','badgiq','{santa}storm','{santa}erl','{santa}pako}','{santa}freq','{santa}talis','{santa}isida']
servzz = ['jsmart.web.id','skyjabber.ru','mersaly.com','octro.net','jabbim.pl','syriasmile.org','syriatalks.org','syriaplus.org','arabstalk.org','syriatalk.co','freize.org','jabber.cz','matrixteam.org','jabbez.org','forat.org','jabber.se','jabster.info','skyjabber.ru','skyjabber.de','jabber.ru','xmpp.ru','jabbrik.ru','myjid.eu','syriastars.com','jabbec.ru','jabber.sy','xmppz.ru','jabbem.ru','jabber.sx','linux.pl','akl.lt','jabber.sk','syriatell.org','syriamoon.org','syriaworld.org','syriaa.ru','jabben.ru','aqq.eu','starstalk.net']#['xmpp.ru','jabber.ru']
nickzz = ['+','##','zoecher','Santa','hanger','Hello','iSiDa-BOt','SiLeNt.HeLL','MohtareF','aedmeral','RaCe','{!}StOrm','{SM}StOrm','iSida-bot','zinid','Matri{x}Team','NEW.By.Me!!','Lattakia','Syria','hamza','Matrix.DarK','I\'m Syrian','Viper','|Santa|BOt','Pako-bot','iCeDa',':-)',':(',':|','*HAHA*','bLaDe','dropbox','Just be happy','A.M.S', 's','z','viper-bot','01']
zoecherz = 'zoecher-'
names = ['zOeCher.Child','Fucker..BOT','_SiLeNt.HeLL_','96433X57X7','OXOXOX','the.xXx.LioN','zoo-57','zoo-75','the.lire.angel','sm-tm']
rezz = ['SyriaAsad 4 JaVa','SyriaTalK4-java','SyriaTalk4-Java-4.90.00','SantaTalK v3.1 http://jabbec.ru/Santa-IM.jar','jabber.web.id','SyriaBuzz4-java','Sham4-java','TalkNchaT Edition Java v2','Santa  IM-Edition_Symbian_fa84bd3d','SiLeNt 4 Ever','Fuck all','Santa  IM-Edition_Symbian_ae2d8e83','Santa  IM-Edition_Symbian_46363524','bot','&&Fuck YOU Mody&& :D:D:D:D:D:D','QIP','tkabber','Psi+']
zoecher_file = 'history/zoecher.txt'
ONVIPE = []
REP_ADV={'n':0,'err':0,'thr':0}
GET_NI=[]
GEN_NI=[]
silent = '1234567890'
zoecher = '~(-!^_^!-)~'

def adv_join(cl,groupchat):
  nick = '|SM|'+str(random.randrange(00, 999))
  GEN_NI.append(groupchat+'/'+nick)
  prs = xmpp.protocol.Presence(groupchat+'/'+nick)
  prs.setTag('x', namespace=xmpp.NS_MUC).addChild('history', {'maxchars':'0', 'maxstanzas':'0'})
  try:
    cl.send(prs)
  except:
    pass

def adv_leave(cl,groupchat,status=''):
  prs=xmpp.Presence(groupchat, 'unavailable')
  try:
    cl.send(prs)
  except:
    pass
	
def generate_adv(_len = None, sg = None):
  if sg == None:
    sg = '1234567890'
  if _len == None:
    _len = random.Random().randint(1, 100)
  s = ''
  l = len(sg)
  while _len > 0:
    s += sg[random.Random().randint(0, l - 1)]
    _len -= 1
  return s

def generate_zoecher(_len = None, sg = None):
  if sg == None:
    sg = '1234567890'
  if _len == None:
    _len = random.Random().randint(1, 100)
  s = ''
  l = len(sg)
  while _len > 0:
    s += sg[random.Random().randint(0, l - 1)]
    _len -= 1
  return s


def timer_adv(type,source,parameters):
  time.sleep(888)
  try:
    REP_ADV['n']=0
    REP_ADV['err']=0
    REP_ADV['thr']=0
  except:
    pass
  if '1' in ONVIPE:
    ONVIPE.remove('1')
    print 'Spam Off'

		      
def adv_start(type,source,parameters):
  body= parameters.split()
  if parameters:
    if not parameters.count(' ') or not parameters.count('@'):
      reply(type,source,u'I just can spam room!')
      return
    i=1
    number = body[1].lower()
    conf = body[0].lower()
    if parameters.count(' '):
      i = int(number)
    if i>1000:
      reply(type,source,u'Max num = 1000')
      return
    if not GS:
      reply(type,source,u'Servers file not found')
      return
    if '1' in ONVIPE:
      reply(type,source,u'I\'m spam another room now.')
      return
    ONVIPE.append('1')
    reply(type,source,u'Okay, Wait Me *HAHA*')
    threading.Thread(None, timer_adv, 'adv_timer'+str(random.randrange(0, 999)), (type,source,parameters)).start()
    REP_ADV['thr']=i
    for x in range(0, i):
      threading.Thread(None, adv_zoecher, 'adv_start'+str(random.randrange(0, 999)), (type,source,conf)).start()
    

def GoOn11(cl,psw):
  while ONVIPE:
    try:
      cl.Process(1)
    except:
      pass
           
def adv_zoecher(type,source,conf):
  if not '1' in ONVIPE:
    print 'break'
    return
  print 'ok'
  try:
    resouz = random.choice(rezz)
    gserv = random.choice(servzz)
    user = random.choice(names)
    name, domain, password, newBotJid, mainRes = user, gserv, 'zoecher', 0, resouz
    print u'START'
    node = unicode(name)
    lastnick = name
    jid = xmpp.protocol.JID(node=node, domain=domain, resource=mainRes)
    print u'bot jid: '+unicode(jid)
    psw = u''
    cl = xmpp.Client(jid.getDomain(), debug=[])
    con = cl.connect()
    if not con:
      threading.Thread(None, hot_spame, 'adv_start'+str(random.randrange(0, 999)), (type,source,conf)).start()
      if REP_ADV['err']!=1:
        print u'error to connect'+gserv
        REP_ADV['err']+=1
        return
    cl.Register('presence',adv_prs)
    cl.Register('iq',zoo_iq)
    cl.Register('message',adv_msg)
    print u'Connected'
    print u'New jid: '+unicode(jid.getNode())+'@'+unicode(domain)
    try:
      xmpp.features.register(cl, domain, {'username': node, 'password':password})
    except AttributeError:
      pass
    print u'Registered'
    au=cl.auth(jid.getNode(), password, jid.getResource())
    if not au:
      threading.Thread(None, hot_spame, 'adv_start'+str(random.randrange(0, 999)), (type,source,conf)).start()
      return
    REP_ADV['n']+=1
    if REP_ADV['n']==REP_ADV['thr']:
      reply(type,source,u'Registered '+unicode(REP_ADV['thr'])+u' Jid')
    print u'Autheticated'
    cl.sendInitPresence()
    threading.Thread(None, GoOn11, 'adv_process'+str(random.randrange(0, 999)), (cl,psw)).start()
    threading.Thread(None, adv_d, 'adv_d'+str(random.randrange(0, 999)), (cl,conf)).start()
  except:
    pass
def adv_prs(cl,mess):
  try:
    silent1 = spam_text
    fromjid = mess.getFrom()
    groupchat = fromjid.getStripped()
    nick = fromjid.getResource()
    ptype = mess.getType()
    if ptype == 'error':
      print 'BAN'
      if not '1' in globals['ONVIPE']:
        print 'STOP'
        try:
          cl.disconnect()
        except:
          pass
        return
      threading.Thread(None, adv_zoecher, 'adv_zoecher'+str(random.randrange(0, 999)), ('','',groupchat)).start()
      return
    cl.send(xmpp.Message(fromjid,spam_text,"chat"))
    for x in range(0, 1):
      if not '1' in globals['ONVIPE']:
        try:
          cl.disconnect()
        except:
          pass
      spisok = spam_text
      omsg = xmpp.protocol.Message(groupchat, spisok, 'chat')
      cl.send(omsg)
    if not groupchat+'/'+nick in globals['GEN_NI'] and not groupchat+'/'+nick in globals['GEN_NI']:
      globals['GEN_NI'].append(groupchat+'/'+nick)
    try:
      cl.disconnect()
    except:
      pass
  except:
    print 'error in adv Message'
    pass

def spame_stop_try(cl):
  try:
    cl.disconnect()
  except:
    pass

def adv_d(cl,conf):
  adv_join(cl,conf)
  time.sleep(0)
  try:
    for x in range(0, 1):
      spisok = spam_text
      omsg = xmpp.protocol.Message(conf, spisok, 'groupchat')
      cl.send(omsg)
  except:
    pass

def adv_msg(cl,msg):
  pass

def adv_stop(type,source,parameters):
  try:
    REP_OTAKE['n']=0
    REP_OTAKE['err']=0
    REP_OTAKE['thr']=0
  except:
    pass
  if '1' in ONVIPE:
    ONVIPE.remove('1')
    reply(type,source,u'Stopped! *SMOKE*')
  else:
    reply(type,source,u'Not Active *PARTY*')


def zoo_iq(cl,iq):
	fromjid = iq.getFrom()
	global BOT_VER1
	if not iq.getType() == 'error':
		if iq.getTags('query', {}, xmpp.NS_VERSION):
			if not BOT_VER1['botver']['os']:
				osver=''
				if os.name=='nt':
					osname=os.popen("ver")
					osver=osname.read().strip().decode('cp866')+'\n'
					osname.close()			
				else:
					osname=os.popen("uname -sr", 'r')
					osver=osname.read().strip()+'\n'
					osname.close()			
				pyver = 'Made By `şỉłэŋŧ.ђєļľ'
				BOT_VER1['botver']['os'] = pyver
			result = iq.buildReply('result')
			query = result.getTag('query')
			query.setTagData('name', BOT_VER1['botver']['name'])
			query.setTagData('version', BOT_VER1['botver']['ver'])
			query.setTagData('os', BOT_VER1['botver']['os'])
			try:
                          cl.send(result)
                        except:
                          pass
		      



def adv_load():
  if not GS:
    try:
      OTAKE = 'war/otake.db'
      fp2 = open(OTAKE, 'r')
      text = eval(fp2.read())
      fp2.close()
      for i in text:
        VIPE[i]=text[i]
      sss='war/otake_serv.db'
      tt=open(sss,'r')
      nxn=eval(tt.read())
      tt.close()
      for x in nxn:
        GS.append(x)
    except:
      print u'ERROR: Adv Plugin need Some Files not found'

def textadd(type, source, parameters):
	if parameters:
		zodata = parameters.strip().split()
		if len(zodata)<1:
			reply(type, source, u'Wrong Arguments!')
			return
		MACROS.add(pl[0], pl[1])
		write_file('war/spamtext.db', str(MACROS.gmacrolist))
		rep = u'Added: '+pl[1]
	reply(type, source, rep)


register_stage0(adv_load)
register(adv_start, Prefix+'spam', 9)
register(adv_stop, Prefix+'stop-spam', 9)
register(textadd, Prefix+'spam-add', 9)
