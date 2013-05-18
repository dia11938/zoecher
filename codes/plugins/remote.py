# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################

def remote(type, source, parameters):	
	groupchat = source[1]
	nick = source[2]
	
	groupchats = GROUPCHATS.keys()
	groupchats.sort()

	if parameters:
		spltdp = parameters.split(' ', 2)
		dest_gch = spltdp[0]
		
		if len(spltdp) >= 2:
			dest_comm = spltdp[1]
		else:
			reply(type, source, u'Wrong command!')
			return
		
		dest_params = ''
		
		if dest_gch.isdigit():
			if int(dest_gch) <= len(groupchats) and int(dest_gch) != 0:
				dest_gch = groupchats[int(dest_gch)-1]
			else:
				reply(type, source, u'The Conference does not exist!')
				return
		else:
			if not dest_gch in groupchats:
				reply(type, source, u'The Conference does not exist!')
				return
				
		if len(spltdp) >= 3:
			dest_params = spltdp[2]
		
		bot_nick = get_bot_nick(dest_gch)
		
		dest_source = [groupchat+'/'+nick,dest_gch,bot_nick]
		
		if COMMAND_HANDLERS.has_key(dest_comm.lower()):
			comm_hnd = COMMAND_HANDLERS[dest_comm.lower()]
		elif MACROS.macrolist[dest_gch].has_key(dest_comm.lower()):
			exp_alias = MACROS.expand(dest_comm.lower(), dest_source)
			
			spl_comm_par = exp_alias.split(' ',1)
			dest_comm = spl_comm_par[0]
			
			if len(spl_comm_par) >= 2:
				alias_par = spl_comm_par[1]
				dest_params = alias_par+' '+dest_params
				dest_params = dest_params.strip()
			
			if COMMAND_HANDLERS.has_key(dest_comm.lower()):
				comm_hnd = COMMAND_HANDLERS[dest_comm.lower()]
			else:
				reply(type, source, u'Unknown command!')
				return
		elif MACROS.gmacrolist.has_key(dest_comm.lower()):
			exp_alias = MACROS.expand(dest_comm.lower(), dest_source)
			
			spl_comm_par = exp_alias.split(' ',1)
			dest_comm = spl_comm_par[0]
			
			if len(spl_comm_par) >= 2:
				alias_par = spl_comm_par[1]
				dest_params = alias_par+' '+dest_params
				dest_params = dest_params.strip()
			
			if COMMAND_HANDLERS.has_key(dest_comm.lower()):
				comm_hnd = COMMAND_HANDLERS[dest_comm.lower()]
			else:
				reply(type, source, u'Unknown command!')
				return
		else:
			reply(type, source, u'Unknown command!')
			return
		
		if type == 'public':
			reply(type, source, u'Sent to PM!')
			
		comm_hnd('private',dest_source,dest_params)
	else:
		gchli = [u'%s) %s' % (groupchats.index(li)+1,li) for li in groupchats]
		
		if gchli:
			rep = u'Available Conferences:\n%s' % ('\n'.join(gchli))
		else:
			rep = u'No available conferences!'
			
		reply(type, source, rep)



register(remote, Prefix+'remote', 8)
