import cgi

# Set the content type to HTML
print("Content-type: text/html\n\n")

# Get the form data
form = cgi.FieldStorage()
name = form.getvalue("name")

# If the form was submitted with a name, render a greeting
if name:
    print("<h1>Hello, {}!</h1>".format(name))
else:
    # Otherwise, show the form
    print("""
    <form method="post">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
    """)