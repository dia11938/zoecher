# zoecher 6.x plugin
# -*- coding: utf-8 -*-
#####################################################################
# This file is part of zOeCher 6.x
# Plugin 4 zOeCher Jabber Bot
# Coded By Silent.Hell (admin@smz.im)
# Official site: http://smz.im
# All Rights Reserved, Copyright © 2o13
#####################################################################
import socket

def dns_query(query):
    try:
	int(query[-1])
    except ValueError:
	try:
	    (hostname, aliaslist, ipaddrlist) = socket.gethostbyname_ex(query)
	    return '  '.join(ipaddrlist)
	except socket.gaierror:
	    return u'I can\'t resolve it.'
    else:
	try:
	    (hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(query)
	except socket.herror:
	    return u'I can\'t resolve it'
	return hostname + ' ' + string.join(aliaslist) + ' ' + string.join(aliaslist)
def dns_dns(type, source, parameters):
    if parameters.strip():
        result = dns_query(parameters)
        reply(type, source, u'IP/Hostname Address: '+result)
    else:
        reply(type, source, u'What?')
register(dns_dns, Prefix+'dns', 1)
