#!/usr/bin/env python2

from glob import glob
from urllib import quote
import re

#Everything in the header string will be written out to the top of the README file
#Github or Bitbucket support Markdown 

header = '''
JITcode-MechE
=============

JIT modules to learn computing in a problem-based context within Mechanical Engineering

###Notebooks'''

format_item = '* [{name}]({url})'.format #Creates a hyperlink using markdown syntax with displayed text "name" and links to "url"

bb_url = 'github.com/barbagroup/JITcode-MechE/blob/master/{}'.format #base url of repo where notebooks are stored

def notebooks():
    ##get list of all ipython notebook files in lessons subdir
    return glob('lessons/*.ipynb')

def lesson_id(filename):
    ##used to sort notebook display order based on prefixed number 
    return int(re.search('[0-9]+', filename).group())

def lesson_name(filename):
    return filename.split('/')[1].split('.')[0].split('_')[2]

def nb_url(filename):
    ##This isn't really useful anymore, but if your file name has any whitespace or other non-URL compliant characters this formats the appropriate unicode
    raw_url = bb_url(quote(quote(filename))) 
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)

def write_readme(nblist, fo):
    fo.write('{}\n'.format(header)) #write the header specified above
    #write out each link to invidual notebooks in order
    for nb in nblist:
        name = lesson_name(nb)
        url = nb_url(nb)
        fo.write('{}\n'.format(format_item(name=name, url=url)))

def main():
    nblist = sorted(notebooks(), key=lesson_id) #get list of notebooks sorted by leading number
    with open('README.md', 'w') as fo:
        write_readme(nblist, fo)

if __name__ == '__main__':
    main()
