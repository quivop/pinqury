# beautify your new html file~
from tidylib import tidy_document


# grab the html~
ugly_html = open('ht/hallo.html', 'r')
html_string = ugly_html.read()
ugly_html.close()

# run it through a beautiful soup parser~
parsed_html, errors = tidy_document(html_string)

# now stick it in a new file~
pretty_html = open('htp/hallo3.html', 'w')

pretty_html.write(parsed_html)
pretty_html.close()

print(errors)
