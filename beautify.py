# beautify your new html file~
from bs4 import BeautifulSoup
import re


# make a better prettifier~
def my_prettifier(soup, indent_width=4, single_lines=True):
    if single_lines:
        for tag in soup():
            tag.attrs = {
                attr: [" ".join(attr_value.replace(
                    "\n", " ").split()) for attr_value in value]
                if isinstance(value, list)
                else " ".join(value.replace("\n", " ").split())
                for attr, value in tag.attrs.items()}

    r = re.compile(r'^(\s*)', re.MULTILINE)
    return r.sub(r'\1' * indent_width, soup.prettify())


# grab the html~
ugly_html = open('ht/hallo.html', 'r')
html_string = ugly_html.read()
ugly_html.close()

# run it through a beautiful soup parser~
parsed_html = BeautifulSoup(html_string, 'html.parser')

# now stick it in a new file~
pretty_html = open('htp/hallo2.html', 'w')

pretty_html.write(my_prettifier(parsed_html))
pretty_html.close()
