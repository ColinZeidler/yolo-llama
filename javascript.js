 var testcase;
 var testplan;
 var statuscomp;
 var statusinprog;
 var statusfail;
 var statuspass;
 var fromdate;
 var todate;
 var orderBy;

 var phpURL;
 var counter = 50;
function load() {
 testcase = document.getElementById('typecase');
 testplan = document.getElementById('typeplan');
 statuscomp = document.getElementById('statuscomplete');
 statusinprog = document.getElementById('statusinprog');
 statusfail = document.getElementById('statusfail');
 statuspass = document.getElementById('statuspass');
 fromdate = document.getElementById('from');
 todate = document.getElementById('to');
 orderBy = document.getElementById('orderby');
}
function update() {
 var http_r = new XMLHttpRequest();
 genURL();
 http_r.onreadystatechange = function() {
  if (http_r.readyState == 4) {
   counter = 50;
   var resultsdiv = document.getElementById('results');
   resultsdiv.innerHTML = http_r.responseText;
   resultsdiv.innerHTML = resultsdiv.innerHTML + "<div id=loadmore onclick='loadMore(this)'><h1>Load More</h1></div>";
   document.getElementById('loading').innerHTML = '';
  }
 }
 http_r.open('GET', phpURL, true);
 http_r.send();
 document.getElementById('loading').innerHTML = "<img src=\"images/loading_spin.gif\" height=64px />";
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

function loadMore(obj) {
 console.info(obj);
 var http_r = new XMLHttpRequest();
 genURL(counter);
 http_r.onreadystatechange = function() {
  if (http_r.readyState == 4) {
   var adder = document.getElementById('loadmore');
   var results = document.getElementById('results');
   adder.parentNode.removeChild(adder);
   results.innerHTML = results.innerHTML + http_r.responseText;
   results.appendChild(adder);
   adder.innerHTML = "<h1>Load More</h1>";
   counter += 50;
  }
 }
 http_r.open('GET', phpURL, true);
 http_r.send();
 document.getElementById('loadmore').innerHTML = "<h1>Loading...</h1>";
}

function genURL(start) {
 start = start || 0;
 console.info(start)
 phpURL = 'tracker.php?case=' + testcase.checked + '&plan=' + testplan.checked + '&complete=' + statuscomp.checked + '&inprog=' + statusinprog.checked + '&fail=' + statusfail.checked + '&fromdate=' + fromdate.value + '&todate=' + todate.value + "&pass=" + statuspass.checked + "&startAt=" + start + "&order=" + orderBy.options[orderBy.selectedIndex].value;
}
