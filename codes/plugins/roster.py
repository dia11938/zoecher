# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def roster(type,source,parameters):
        if parameters:
                jiddata = parameters.strip().split()
                if len(jiddata) > 2:
                        reply(type, source, u'What?')
                        return
        if parameters.count(u'del') and parameters.count('@') and parameters.count('.'):
                ROSTER = JCON.getRoster()
                ROSTER = JCON.getRoster()
                ROSTER.delItem(jiddata[1])
                reply(type,source,u'Ok!')
                return
        if parameters.count(u'add') and parameters.count('@') and parameters.count('.'):
                ROSTER = JCON.getRoster()
                ROSTER.Subscribe(jiddata[1])
                reply(type,source,u'Ok!')
                return
        if parameters.count(u'show'):
                ROSTER = JCON.getRoster()
                list, col = '', 0
                rep = ROSTER.getItems()
                for jid in rep:
                        if not jid.count('@conf'):
                                col = col + 1
                                list += '\n'+str(col)+'. '+jid
                if col != 0:
                        reply(type, source, (u'\nTotal: %s Contacts in My Roster:' % str(col))+list)
                else:
                        reply(type, source, u'Not found')

		
register(roster, Prefix+'roster', 8)
