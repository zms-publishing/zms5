#!/bin/bash

instance_dir="/home/zope/venv/instance/zms5"
venv_bin_dir="/home/zope/venv/bin"

nohup  $venv_bin_dir/runzeo --configure $instance_dir/etc/zeo.conf 1>/dev/null 2>/dev/null &
echo "ZEO started"
nohup  $venv_bin_dir/runwsgi --debug --verbose $instance_dir/etc/zope.ini debug-mode=on http_port=8085 1>/dev/null 2>/dev/null &
echo "ZOPE 8085 started"
# nohup $venv_bin_dir/runwsgi --debug --verbose $instance_dir/etc/zope.ini debug-mode=on http_port=8086 1>/dev/null 2>/dev/null &
# echo "ZOPE 8086 started"
echo "ZOPE 8086 is starting"
$venv_bin_dir/runwsgi --debug --verbose $instance_dir/etc/zope.ini debug-mode=on http_port=8086