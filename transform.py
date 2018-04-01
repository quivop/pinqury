# script to transform markdown into html

import CommonMark

md_file = open('md/hallo.md', 'r')
md_string = md_file.read()

ht_file = open('ht/hallo.html', 'w')
ht_file.write(CommonMark.commonmark(md_string))
ht_file.close()
