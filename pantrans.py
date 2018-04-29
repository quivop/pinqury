# script to transform markdown into html

import pypandoc

# grab markdown~
md_file = open('md/pan_hallo.md', 'r')
md_string = md_file.read()
md_file.close()

# grab header and footer~
header = open('templates/header.html', 'r')
footer = open('templates/footer.html', 'r')

# convert markdown body~
body = pypandoc.convert_text(md_string, 'html', format='md')

# stick it all together in a new file~

ht_file = open('ht/pan_hello.html', 'w')

ht_file.write(header.read() + body + footer.read())
ht_file.close()