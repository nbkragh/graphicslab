import numpy as np
import sys, os, bpy, math

# image files
destination = "C:/Users/NBK/Documents/BlenderOuput/img"
num_files_pre = len(os.listdir(destination))
bpy.context.scene.render.image_settings.file_format = 'PNG'


# rotate klods
klods = bpy.data.objects['klods']
klodsrotation = klods.rotation_euler
klods.rotation_euler= (klodsrotation.x+11,klodsrotation.y+12, klodsrotation.z+13)

# start start and stop simulation, then render
end_at_frame = 20
bpy.context.scene.frame_end = end_at_frame
for i in range(1):
    num_files_pre = num_files_pre+1
    bpy.context.scene.frame_current = 0
    bpy.ops.screen.animation_play()



#bpy.context.scene.frame_current = 0
#bpy.ops.screen.animation_play()
def stop_animation_handler(scene):
    
    if bpy.context.scene.frame_current == end_at_frame:
        
        bpy.context.scene.render.filepath = os.path.join(destination, 'sim_render'+str(num_files_pre)+'.png')
        bpy.ops.render.render(write_still = True, use_viewport=True)
        bpy.ops.screen.animation_cancel(restore_frame=False)
for i in range( len(bpy.app.handlers.frame_change_pre) ):
    bpy.app.handlers.frame_change_pre.pop()

bpy.app.handlers.frame_change_pre.append(stop_animation_handler)

# render image
#    num_files_pre = num_files_pre+1
#    bpy.context.scene.render.filepath = os.path.join('C:/Users/NBK/Documents/BlenderOuput/img', 'sim_render'+str(num_files_pre)+'.png')
#    bpy.ops.render.render(write_still = True, use_viewport=True)

