import sys, requests

url = "https://magorcorp.atlassian.net/rest/api/2/search"
user = "auto.verification"
passw = "video123"

case = sys.argv[1]
plan = sys.argv[2]

complete = sys.argv[3]
inprog = sys.argv[4]

fromdate = sys.argv[5]
todate = sys.argv[6]

query = "project=Verification&created>=\"-{}d\"&created<=\"-{}d\"".format(fromdate, todate)

if case == 'true':
    if plan == 'true':
        query = query + "&(type=\"Test Case\"+OR+type=\"Test Plan\")"
    else:
        query = query + "&type=\"Test Case\""
elif plan == 'true':
    query = query + "&type=\"Test Plan\""

if inprog == 'true':
    if complete == 'false':
        query = query + "&status=\"In Progress\""
elif complete == 'true':
    query = query + "&status!=\"In Progress\""

query = query + "+order+by+created"
print query

r = requests.get("{}?jql={}".format(url, query), auth = (user, passw))

print r

for issue in r.json()['issues']:
    print issue['key']
