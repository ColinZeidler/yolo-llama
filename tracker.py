import sys, requests

url = "https://magorcorp.atlassian.net/rest/api/2/search"
user = "auto.verification"
passw = "video123"

case = sys.argv[0]
plan = sys.argv[1]

complete = sys.argv[2]
inprog = sys.argv[3]

fromdate = sys.argv[4]
todate = sys.argv[5]


