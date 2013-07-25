 var testcase;
 var testplan;
 var statuscomp;
 var statusinprog;
 var statusfail;
 var statuspass;
function load() {
 testcase = document.getElementById('typecase');
 testplan = document.getElementById('typeplan');
 statuscomp = document.getElementById('statuscomplete');
 statusinprog = document.getElementById('statusinprog');
 statusfail = document.getElementById('statusfail');
 statuspass = document.getElementById('statuspass');
}
function update() {
 var fromdate = document.getElementById('from');
 var todate = document.getElementById('to');

 var http_r = new XMLHttpRequest();
 
 http_r.onreadystatechange = function() {
  if (http_r.readyState == 4) {
   document.getElementById('results').innerHTML = http_r.responseText;
  }
 }
 http_r.open('GET', 'tracker.php?case=' + testcase.checked + '&plan=' + testplan.checked + '&complete=' + statuscomp.checked + '&inprog=' + statusinprog.checked + '&fail=' + statusfail.checked + '&fromdate=' + fromdate.value + '&todate=' + todate.value + "&pass=" + statuspass.checked, true);
 http_r.send();

}

function updateType() {
 if (testcase.checked) {
  statusfail.disabled = false;
  statuspass.disabled = false;
 } else {
  statusfail.disabled = true;
  statusfail.checked = false;
  statuspass.disabled = true;
  statuspass.checked = false;
 }

 if (testplan.checked) {
  statuscomp.disabled = false;
 } else {
  statuscomp.disabled = true;
  statuscomp.checked = false;
 }
}
