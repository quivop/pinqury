# script to transform markdown into html

import CommonMark

# grab markdown~
md_file = open('md/hallo.md', 'r')
md_string = md_file.read()
md_file.close()

# grab header and footer~
header = open('templates/header.html', 'r')
footer = open('templates/footer.html', 'r')

# convert markdown body~
body = CommonMark.commonmark(md_string)

# stick it all together in a new file~

ht_file = open('ht/hallo.html', 'w')

ht_file.write(header.read() + body + footer.read())
ht_file.close()
