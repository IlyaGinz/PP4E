import cgi, shelve, sys, os

form = cgi.FieldStorage()
print('Content-type: text/html')

replyhtml = """
<html>
<title>Reply Page</title>
<body>
</body>
</html>
"""
print(replyhtml)

