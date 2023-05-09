import cgi
form = cgi.FieldStorage()
name = form.getvalue("user")
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user'  in form:
    print('<h1>Who are you?</h1>')
else:
    #print(f"<h1>Hello <i>{form.getvalue(form['user'].value)}</i>!</h1>")
    #print('<h1>Hello <i>%s</i>!</h1>' % form.escape(form['user'].value))
    #print("<h1>Hello, {}!</h1>".format(name))
    print(f"<h1>Hello <i>{name}</i>!</h1>")
    
    
