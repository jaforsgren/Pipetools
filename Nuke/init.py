# If Write dir does not exist, create it
def createWriteDir(): 
    file = nuke.filename(nuke.thisNode()) 
    dir = os.path.dirname( file ) 
    osdir = nuke.callbacks.filenameFilter( dir ) 
    try: 
        os.makedirs( osdir ) 
        return 
    except: 
        return

# Activate the createWriteDir function
nuke.addBeforeRender( createWriteDir )


# Make Write node default to sRGB color space
nuke.knobDefault('Write.mov.colorspace', 'sRGB')




# Formats
nuke.addFormat( '1024 576 PAL Widescreen' )
nuke.addFormat( '1280 720 HD 720p' )


"""
bra att kolla
https://github.com/fredrikaverpil/nuke/blob/master/init.pyhttps://github.com/fredrikaverpil/nuke/blob/master/init.py
https://github.com/throb/vfxpipe/blob/master/nuke/init.py

# Make these favorites show up in Nuke
nuke.addFavoriteDir('File server', volProjects + '/Projects/')
nuke.addFavoriteDir('Assets', volAssets)
nuke.addFavoriteDir('R&D', volProjects + '/RnD/')

# Set plugin/gizmo sub-folders
nuke.pluginAppendPath(volAssets + '/include/nuke/gizmos')
nuke.pluginAppendPath(volAssets + '/include/nuke/plugins')
nuke.pluginAppendPath(volAssets + '/include/nuke/scripts')
nuke.pluginAppendPath(volAssets + '/include/nuke/icons')

"""