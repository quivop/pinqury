# beautify your new html file~
from bs4 import BeautifulSoup


# grab the html~
ugly_html = open('ht/hallo.html', 'r')
html_string = ugly_html.read()
ugly_html.close()

# run it through a beautiful soup parser~
parsed_html = BeautifulSoup(html_string, 'html.parser')

# now stick it in a new file~
pretty_html = open('htp/hallo.html', 'w')

pretty_html.write(parsed_html.prettify())
pretty_html.close()