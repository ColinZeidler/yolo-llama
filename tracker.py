import sys, requests
import urllib, json

url = "https://magorcorp.atlassian.net/rest/api/2/search"
user = "auto.verification"
passw = "video123"

case = sys.argv[1]
plan = sys.argv[2]

complete = sys.argv[3]
inprog = sys.argv[4]
fail = sys.argv[5]
sPass = sys.argv[6]

fromdate = sys.argv[7]
todate = sys.argv[8]

startAt = sys.argv[9]


query = "project=Verification AND created>=\"-{}d\" AND created<=\"-{}d\"".format(fromdate, todate)

if case == 'true':
    if plan == 'true':
        query = query + " AND (type=\"Test Case\" OR type=\"Test Plan\")"
    else:
        query = query + " AND type=\"Test Case\""
elif plan == 'true':
    query = query + " AND type=\"Test Plan\""


counter = 0
if complete == 'true':
    query = query + " AND ("
    query = query + "status=\"Test Run: Complete\""
    counter += 1

if inprog == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + " AND ("

    query = query + "status=\"In Progress\""
    counter += 1

if fail == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + " AND ("

    query = query + "status=\"Test Failed\""
    counter += 1

if sPass == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + " AND ("

    query = query + "status=\"Test: Passed\""
    counter += 1
if counter > 0:
    query = query + ")"

query = query + " order by updated"
print query
print "<br>"

print startAt
data = {"jql": query, "startAt" : startAt}
header = {"content-type": "application/json"}
r = requests.post("{}".format(url), auth = (user, passw), headers = header, data = json.dumps(data))

counter = 0
for issue in r.json()['issues']:
    counter += 1
    if issue['fields']['issuetype']['name'] == 'Test Case':
        print "<div class=testCase>"

    elif issue['fields']['issuetype']['name'] == 'Test Plan':
        print "<div class=testPlan>"

    print "<h1>", issue['fields']['issuetype']['name'], issue['key'], "</h1>"
    print "<h2>", issue['fields']['status']['name'], "</h2>"
#customfield_10228 = build number (for test cases, and test plans)
    try:
        print "Build:", issue['fields']['customfield_10228'][0]
    except:
        print "build not set"
    print "<br>"
    print "<div class=time>"
    date = issue['fields']['created'][:-12].split("T")
    print "Created", date[1] + ", " +  date[0], "<br>"
    update = issue['fields']['updated'][:-12].split("T")
    print "Updated", update[1] + ", " +  update[0], "<br>"
    print "</div>"
    print "</div>"
