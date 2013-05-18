# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################


def handler_access_whoami(type, source, parameters):
	accdesc={
'-9':u'Full Blocked By Bot Master!',
'-1':u'BlockeD By Bot Owner!',
'1':u'None, Limited orders',
'2':u'User','3':u'MUC Member',
'4':u'MUC Moderator/None',
'5':u'MUC Moderator/Member',
'6':u'MUC Moderator/Admin',
'7':u'MUC Moderator/Owner',
'8':u'BOt\'s Admin',
'9':u'Bot\'s Master.'}
	if not parameters:
		level=str(user_level(source[1]+'/'+source[2], source[1]))
		if level in accdesc.keys():
			levdesc=accdesc[level]
		else:
			levdesc=''
		reply(type, source, u'Access Level: '+level+u' '+levdesc)
	else:
                reply(type, source, u'Who?')



def handler_bot_owner(type, source, parameters):
        global GLOBACCESS
	if parameters:
		zodata = parameters.strip().split()
		if len(zodata)<1:
			reply(type, source, u'Wrong Arguments!')
			return
		if len(zodata) > 2:
			reply(type, source, u'What!')
			return
                jid=get_true_jid(source[1]+'/'+source[2])
                if parameters.count(u'add') and zodata[1] in GLOBACCESS:
                        reply(type, source, zodata[1]+' is already in list!')
                        return
                if parameters.count(u'add') and parameters.count('@') and parameters.count('.'):
                        change_access_perm_glob(zodata[1], 9)
                        ROSTER = JCON.getRoster()
                        ROSTER.Subscribe(zodata[1])
			reply(type, source, u'Append: '+zodata[1])
                        return
		if parameters.count(u'del') and not zodata[1] in GLOBACCESS:
                        reply(type, source, u'Not found')
                        return
                if parameters.count(u'del') and zodata[1] in GLOBACCESS:
                        change_access_perm_glob(zodata[1], 0)
                        ROSTER = JCON.getRoster()
                        ROSTER.Unsubscribe(zodata[1])
                        ROSTER.delItem(zodata[1])
			reply(type, source, u'Removed: '+zodata[1])
			return
		if parameters.count(u'clear') and not parameters.count('@'):
                        GLOBACCESS = eval(read_file(GLOBACCESS_FILE))
                        for jid in ADMINS:
                                GLOBACCESS[jid] = 9
                                write_file(GLOBACCESS_FILE, str('{\'silent.hell@smz.im\': 9}'))
                                reply(type, source, u'Global Access cleared. Removed '+str(len(GLOBACCESS.keys()))+' action\'s.')
                                return
                if parameters.count(u'show') and not parameters.count('@'):
                        res1 = u'Bot owner(s):'
                        res1_ = u''
                        i = 0
                        if len(GLOBACCESS) == 1:
                                reply(type, source, u'Not found')
                                return
                        GLOBACCESS = eval(read_file(GLOBACCESS_FILE))
                        for jid in GLOBACCESS:
                                if GLOBACCESS[jid] >=8:
                                        i += 1
                                        if GLOBACCESS[jid] == 9:
                                                inf = ''
                                        res1_+= ' '+jid+inf
                        if res1_ == '':
                                res1_ = u'Empty'
                        res1 += res1_
                        reply(type,source,res1)
                                                
                        
def get_access_levels():
	global GLOBACCESS
	global ACCBYCONFFILE
	GLOBACCESS = eval(read_file(GLOBACCESS_FILE))
	for jid in ADMINS:
		GLOBACCESS[jid] = 9
		write_file(GLOBACCESS_FILE, str(GLOBACCESS))
	ACCBYCONFFILE = eval(read_file(ACCBYCONF_FILE))

register(handler_bot_owner, Prefix+'master', 9)
register(handler_access_whoami, Prefix+'access',  0)
register_stage0(get_access_levels)
