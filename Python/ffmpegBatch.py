import os, optparse, logging, subprocess, re
"""
=======================================================================
ffmpeg batch utility
stolen from https://github.com/throb

===========================================================
"""

def searchDir(pathName, ext):

    foundFiles = []
    for root, dirs, files in os.walk(pathName):
        for curFile in files:
            if ext in os.path.splitext(curFile)[1] : foundFiles.append(os.path.normpath(os.path.join(root, curFile)))
    return foundFiles

def processFiles(fileList, ext):

    ffmpegPath = '//shared-fs1/package/Softwarepeg/ffmpeg'

    for curFile in fileList:
        if os.path.exists(os.path.dirname(curFile.replace(ext,'m4v'))) == False:
            os.makedirs(os.path.dirname(curFile.replace(ext,'m4v'))) 

        ffOpts = ' -y -i %s -vcodec libx264 -b:v 2000k -threads 0 -an %s' % (curFile, curFile.replace(ext,'m4v'))
        subprocess.call(ffmpegPath + ffOpts)        
        print ffmpegPath + ffOpts + '\n'   


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    usageStr = '%s [arguments] ' % (__file__)
    parser = optparse.OptionParser(usage = usageStr)
    
    #options    
    parser.add_option('-i','--input',action = 'store', dest = 'inputPath', help = 'Input Path (full path)', default = None)
    parser.add_option('-e','--ext',action = 'store', dest = 'extension', help = 'Extension to search for', default = 'mov')
    options, args = parser.parse_args()    
       
    # Option Checking
    if options.inputPath == None:
        parser.error('Please enter a path')
    if os.path.isdir(options.inputPath) == False:
        parser.error('Please enter a valid directory\n%s is not valid' % (options.inputPath))
  
    

    fileList = searchDir(options.inputPath, options.extension)
    processFiles(fileList, options.extension)
    print 'Processed %d files' % (len(fileList))
    