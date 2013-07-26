<?php
$case = $_GET['case'];
$plan = $_GET['plan'];
$complete = $_GET['complete'];
$inprog = $_GET['inprog'];
$fail = $_GET['fail'];
$pass = $_GET['pass'];
$fromdate = $_GET['fromdate'];
$todate = $_GET['todate'];
$startAt = $_GET['startAt'];

#echo "$case $plan $complete $inprog $fail $fromdate $todate<br>";
echo `/home/videowall/python2.7-env/bin/python2.7 tracker.py $case $plan $complete $inprog $fail $pass $fromdate $todate $startAt`;
?>
