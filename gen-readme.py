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

format_module = '####{name}'.format
#Format string for module headers

def notebooks():
    '''
    get list of all ipython notebook files in lessons subdir
    '''
    return glob('module*/*.ipynb')

def lesson_id(filename):
    '''
    used to sort notebook display order based on prefixed number
    at beginning of filename
    '''

    return int(re.search('/([0-9]+)_', filename).group(1))

def module_id(filename):
    '''
    used to sort notebook order based on which module directory
    the file is found in
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

def module_name(filename):
    print filename
    return re.search('module[0-9]+_([a-zA-Z_]+)',filename).group(1).replace("_"," ");

def sort_by_module(filenames):
    '''
    Takes all of the filenames found and organizes them based on which module
    they are from
    '''
    module_dict = {}
    for i in filenames:
        name = module_name(i)
	if name in module_dict:
	    module_dict[name].append(i)
	else:
	    module_dict[name] = [i]
    return module_dict

def sort_module_list(modules):
     '''
     Takes a dictionary of modules and sorts all of the lessons within it 
     by their order
     '''
     sorted_modules = {}
     for i in modules:
         sorted_modules[i] = sorted(modules[i], key=lesson_id)

     return sorted_modules


def nb_url(filename):
    '''This isn't really useful anymore, but if your file name has 
    any whitespace or other non-URL compliant characters this formats
    the appropriate unicode.  Note that nbviewer has periodically changed
    how it handles various unicode addresses, so we generally avoid all
    whitespace in filenames.
    '''
    raw_url = bb_url(quote(quote(filename))) 
    return 'http://nbviewer.ipython.org/urls/{}'.format(raw_url)

def write_readme(modules, fo):
    '''
    for each notebook in nblist, write out the formatted nbviewer links
    to the file specified by fo (README.md) and prepend the header string
    specified above
    '''
    fo.write('{}\n'.format(header)) 
    for mod in modules:
        fo.write('{}\n'.format(format_module(name=mod)))
	for nb in modules[mod]:
        	name = lesson_name(nb)
        	url = nb_url(nb)
        	fo.write('{}\n'.format(format_item(name=name, url=url)))

def main():
    nblist = sorted(notebooks(), key=lesson_id) #get list of notebooks sorted by leading number
    modules = sort_module_list(sort_by_module(notebooks()))
    with open('README.md', 'w') as fo:
        write_readme(modules, fo)

if __name__ == '__main__':
    main()
