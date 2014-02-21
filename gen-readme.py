#!/usr/bin/env python2

from glob import glob
from urllib import quote
import re

'''
Everything in the header string will be written out to the top of the README file
Github or Bitbucket support Markdown so you can format links, headers, bulleted lists
etc... within this string and it will be rendered on Github
'''

header = '''
JITcode-MechE
=============

JIT modules to learn computing in a problem-based context within Mechanical Engineering

###Notebooks'''

format_item = '* [{name}]({url})'.format
#Creates a hyperlink using markdown syntax with displayed text "name" and links to "url"

bb_url = 'github.com/barbagroup/JITcode-MechE/blob/master/{}'.format
#base url of repo where notebooks are stored

def notebooks():
    '''
    get list of all ipython notebook files in lessons subdir
    '''
    return glob('lessons/*.ipynb')

def lesson_id(filename):
    '''
    used to sort notebook display order based on prefixed number
    at beginning of filename
    '''
    return int(re.search('[0-9]+', filename).group())

def lesson_name(filename):
    '''
    Given a filename of format 00_Lesson00_Name_Of_Lesson.ipynb
    returns the Name_Of_Lesson with underscores replaced with whitespace

    Actual process: Grab the starting and ending string indices of LessonXX, 
    use that to slice the string from just after the LessonXX ending indice, then split
    the remaining string at the '.' to drop the .ipynb and then replace all remaining 
    underscores with spaces
    '''
    [ind.end(0) for ind in re.finditer('Lesson[0-9]+',filename)]
    return filename[ind.end(0)+1:].split('.')[0].replace('_',' ')


def nb_url(filename):
    '''This isn't really useful anymore, but if your file name has 
    any whitespace or other non-URL compliant characters this formats
    the appropriate unicode.  Note that nbviewer has periodically changed
    how it handles various unicode addresses, so we generally avoid all
    whitespace in filenames.
    '''
    raw_url = bb_url(quote(quote(filename))) 
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)

def write_readme(nblist, fo):
    '''
    for each notebook in nblist, write out the formatted nbviewer links
    to the file specified by fo (README.md) and prepend the header string
    specified above
    '''
    fo.write('{}\n'.format(header)) 
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
