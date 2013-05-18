# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def commands(type, source, parameters):
        access_level=str(user_level(source[1]+'/'+source[2], source[1]))
        res = u'Total commands: '+str(len(COMMANDS.keys()))+'\nPrefix: '+Prefix+' | Your access level: '+access_level+' | Available commands: \n- ... Users/Members: ver, ping, info, regjid, commands, help, dns, time\n- 6 ... iq, clear, drjabber, net_ping\n- 7 ... banlist [clear, copy], memberlist [clear, copy], owners, admins\n- 8 ... free [m, g, k], setnick, loadpl, glob_status, glob_member, glob_ban\n- 9 ... master [add, del, show, clear], enter, esc, remote, reboot, halt, clear-rooms, roster [add, del, show]\n- ... WAR Commands\n( For Roomz )\nspam, stop-spam, spam-add, zoech, stop_zoech, start, stop, start2, stop2\n( For JID\'s ) \n spamjid, stop_spamjid, spamjid2, stop_spamjid2'
        reply(type, source, res) 

register(commands, Prefix+'commands', 0)
