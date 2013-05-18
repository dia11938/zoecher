# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def clear_rooms(type,source,parameters):
    reply(type,source,u'The process has started, I\'ll leave '+str(len(GROUPCHATS.keys()))+' conference\'s.')
    if check_file(file='conferences.db'):
        killrooms = eval(read_file(GROUPCHAT_CACHE_FILE))
    for groupchat in killrooms:
	leave_groupchat(groupchat, u'Left by clear rooms order from my Master')
    else:
	print 'Error! Plugin (clear_rooms)'
    rooms_file = 'history/conferences.db'
    start2 = open(rooms_file, 'r')
    txt2 = eval(start2.read())
    write_file(rooms_file,str('{u\'santa@conference.smz.im\': {\'nick\': \'zOeCher\'}}'))
    reply(type, source, u'The operation was successful.')
register(clear_rooms, Prefix+'clear-rooms',  9)   
