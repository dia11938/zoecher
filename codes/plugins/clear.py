# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def cleaner(type, source, parameters):
    groupchat=source[1]
    if GROUPCHATS.has_key(groupchat):
      reply(type, source, u'Clean by 20 messages in 0 second\'s')
      cleans=xmpp.protocol.Presence(source[1]+'/'+get_bot_nick(source[1]))
      JCON.send(cleans)
      for x in range(20, 25):
        time.sleep(0.2)
        msg(groupchat, u'')
      reply(type, source, u'Cleaned!')
      done=xmpp.protocol.Presence(source[1]+'/'+get_bot_nick(source[1]))
      JCON.send(done)
    
register(cleaner, Prefix+'clear',  4)
register(cleaner, '0',  4)
