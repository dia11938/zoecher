#!/bin/bash

zoecher=./zoecher.py

PIDPATH=./settings
PIDFILE=$PIDPATH/zoecher.pid

case "$1" in
  start)
	echo -n "Starting zOeCher Bot: "
	if ([[ -w $PIDFILE ]])
	then 
		echo "ERROR: zOeCher BOt already running!"
		exit 1
	fi
	$NEUTRON --pid=$PIDFILE >/dev/null &
	echo "Done"
    ;;
  stop)
	echo -n "Stopping zOeCher BOt: "
	if !([[ -w $PIDFILE ]])
	then 
		echo "ERROR: zOeCher Bot is not running!"
		exit 1
	fi
	kill `cat $PIDFILE`
	rm $PIDFILE
	echo "done"
    ;;
  *)
    echo "Usage: $0 [start|stop]" >&2
    exit 1
    ;;
esac

exit 0
