import fnmatch
import os

PATH = '/../../../..'
ext = '*.mb'

def get_file_names(filepath, ext):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames, ext):                
                matches.append(os.path.join(filename)) 
        if matches:
            print "Found {} files:".format(len(matches))
            output_files(matches)
        else:
            print "No files found."
    else:
        print "Sorry that path does not exist. Try again."


def output_files(list_of_files):
    for filename in list_of_files:
        print filename

files = get_file_names(PATH, ext)