<?php
$case = $_GET['case'];
$plan = $_GET['plan'];
$complete = $_GET['complete'];
$inprog = $_GET['inprog'];
$fromdate = $_GET['fromdate'];
$todate = $_GET['todate'];

echo `/home/videowall/python2.7-env/bin/python2.7 tracker.py $case $plan $complete $inprog $fromedate $todate`
?>
