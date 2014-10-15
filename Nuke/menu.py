
""""
import nukeExternalControl.server
nukeExternalControl.server.nuke_command_server()
"""
# -------- My Toolbar --------

# Initialize the toolbar menu
toolbar = nuke.toolbar('Nodes')

# My tools
toolbar.addCommand('My Nodes/Bezier', "nuke.createNode('Bezier')")
toolbar.addCommand( "My Nodes/pgBokeh", "nuke.createNode('pgBokeh')")


# -------- My File Menu --------

nuke.menu( 'Nuke' ).addCommand( 'My file menu/Rendering/Send to RenderManager', "nuke.load(\"submitNukeToRenderManager\"), submitNukeToRenderManager()" )

"""

https://github.com/throb/vfxpipe/blob/master/nuke/menu.py

# add to main nuke menu
menubar = nuke.menu("Nuke");

# add Read/Write Panel to File Menu
menubar.addSeparator()
menubar.addCommand('File/Display Read-Write Nodes','fxpipenukescripts.showReadWrite()','shift-q')

# add shift-z for delete
menubar.addSeparator()
menubar.addCommand( 'Edit/Delete Node(s)', 'nukescripts.node_delete(popupOnError=True)', 'shift+z')
menubar.addCommand( 'Edit/Archive Script','fxpipenukescripts.archive.ai.interface()','')
menubar.addCommand( 'Edit/Open selected node in OS Browser','fxpipenukescripts.openInOSWindow()','ctrl+shift+e')

# add send to playback
#menubar.addCommand('Render/Send to Playback','fxpipenukescripts.sendToPlaybackRV()','')

# menu is...
m = menubar.addMenu("&Pipeline Tools")

# add pipeline menu items here
m.addCommand('Auto Write','fxpipenukescripts.createAutowrite()','alt+w')
m.addCommand('Viewer Input','nuke.createNode("VIEWER_INPUT")','')
m.addSeparator()


"""