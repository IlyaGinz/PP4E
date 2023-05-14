import cgi
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'username' in form:
    print('<h1>Who are you?</h1>')
else:
    #print(f"<h1>Hello <i>{form.getvalue(form['user'].value)}</i>!</h1>")
    #print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))
    #print("<h1>Hello, {}!</h1>".format(name))
    print(f"<h1>Hello <i>{username}</i>!</h1>")
    print(f"<h2>Is this your password: <i>{password}</i>?</h2>")
    
print(f'<p>this is the form: \n {form}</p>')
print(f'<p>this is the username: \n {form["username"]}</p>')
# print(f'<p>this is the password: \n {form}</p>')
    
