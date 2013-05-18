# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def info(type, source, parameters):
    accdesc={'blocked':u'Full Blocked By Bot Owner',
'ignore':u'BlockeD By Bot Owner!',
'1':u'None, Limited orders',
'2':u'User','3':u'MUC Member',
'4':u'MUC Moderator/None',
'5':u'MUC Moderator/Member',
'6':u'MUC Moderator/Admin',
'7':u'MUC Moderator/Owner',
'8':u'BOt\'s Admin',
'9':u'Bot\'s owner.'
}
    if not parameters:
	acc=str(user_level(source[1]+'/'+source[2], source[1]))
	if acc in accdesc.keys():
    	    levdesc=accdesc[acc]
        else:
	    levdesc=''
	reply(type,source,u'\n- Prefix: '+Prefix+'\n- Bot version: 5.'+zoo_ver+'\n- Your Access Level: '+acc+', '+levdesc+'\n- Total Error\'s: 0\n- Total Conference\'s: '+str(len(GROUPCHATS.keys()))+' for more information use "remote" command.\n- Server: conference.'+CONNECT_SERVER+' | BOt Nick: '+BotNick+'\n- Message size limit : 4096')

register(info, Prefix+'info', 2)
