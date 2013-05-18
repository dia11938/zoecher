# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################
  


def ch_st(type, source, parameters):
	if parameters:
		args,show,status=parameters.split(' ',1),'',''
		if args[0] in ['away','xa','dnd','online']:
			show=args[0]
		else:
			show=None
			status=parameters
		if not status:
			try:
				status=args[1]
			except:
				status=None
		change_bots_status(status,show)

def change_bots_status(status,show):
        rt = xmpp.Presence()
        if show:
                rt.setShow(show)
        if status:
                rt.setStatus(status)
        JCON.send(rt)
        for x in GROUPCHATS:
                try:
                        file='history/'+x+'/config.cfg'
                        fp=open(file,'r')
                        txt=eval(fp.read())
                        fp.close()
                        if 'status' in txt:
                                txt['status']['show']=show[:100]
                                txt['status']['status']=status[:100]
                                write_file(file,str(txt))
                except:
                        pass
                prs=xmpp.protocol.Presence(x+'/'+get_bot_nick(x))
                if status:
                        prs.setStatus(status)
                if show:
                        prs.setShow(show)
                JCON.send(prs)


register(ch_st, Prefix+'glob_status', 8)

