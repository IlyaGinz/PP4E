import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print(f'<h1>Hello <i>{cgi.escape(form["user"].value)}</i>!</h1>')
    # print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))
