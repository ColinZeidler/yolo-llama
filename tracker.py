import sys, requests
import urllib

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


query = "project=Verification&created>=\"-{}d\"&created<=\"-{}d\"".format(fromdate, todate)

if case == 'true':
    if plan == 'true':
        query = query + "&(type=\"Test Case\" OR type=\"Test Plan\")"
    else:
        query = query + "&type=\"Test Case\""
elif plan == 'true':
    query = query + "&type=\"Test Plan\""


counter = 0
if complete == 'true':
    query = query + "&("
    query = query + "status=\"Test Run: Complete\""
    counter += 1

if inprog == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + "&("

    query = query + "status=\"In Progress\""
    counter += 1

if fail == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + "&("

    query = query + "status=\"Test Failed\""
    counter += 1

if sPass == 'true':
    if counter > 0:
        query = query + " OR "
    if counter == 0:
        query = query + "&("

    query = query + "status=\"Test: Passed\""
    counter += 1
if counter > 0:
    query = query + ")"

query = query + " order by created"
print query
print "<br>"

query = urllib.quote_plus(query)

r = requests.get("{}?jql={}".format(url, query), auth = (user, passw))

counter = 0
for issue in r.json()['issues']:
    counter += 1
    print issue['key'], counter
    print "<br>"
    print issue['fields'].keys()
    print "<br>"
