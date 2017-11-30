from flask import Flask


# definition
def say_hello(username = "World"):
    return '<p>Hello %s</p>\n' % username

# Page layout .. replaced with bootstrap stuff later
header_text = '''
    <html>\n<head><title>BeerWell</title></head>\n<body>'''
greetings = '''
    <p>Hai</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


# EB initialization
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + greetings + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# Run the app!
if __name__ == "__main__":
    application.debug = True
    application.run()
