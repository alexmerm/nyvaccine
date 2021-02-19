#!/bin/sh
m=$(cd /home && ./nystatechecker.py 2>&1)
curl -fsS -m 10 --retry 5 --data-raw "$m" https://hc-ping.com/***REMOVED***/$?
echo $m