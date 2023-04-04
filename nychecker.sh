#!/bin/sh
m=$(cd /home && ./nystatechecker.py 2>&1)
curl -fsS -m 10 --retry 5 --data-raw "$m" $HC_PING_URL/$?
echo $m