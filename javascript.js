function update() {
 var testcase = document.getElementById('typecase');
 var testplan = document.getElementById('typeplan');
 var statuscomp = document.getElementById('statuscomplete');
 var statusinprog = document.getElementById('statusinprog');

 var fromdate = document.getElementById('from');
 var todate = document.getElementById('to');

 var http_r = new XMLHttpRequest();
 
 http_r.onreadystatechange = function() {
  if (http_r.readyState == 4) {
   document.getElementById('results').innerHTML = http_r.responseText;
  }
 }
 http_r.open('GET', 'tracker.php?case=' + testcase.checked + '&plan=' + testplan.checked + '&complete=' + statuscomp.checked + '&inprog=' + statusinprog.checked + '&fromdate=' + fromdate.value + '&todate=' + todate.value, true);
 http_r.send();

}
