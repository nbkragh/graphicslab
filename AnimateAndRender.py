import numpy as np
import os, bpy

destination = "C:/Users/NBK/Desktop/projektklodser/BlenderOuput/img"
num_files_pre = len(os.listdir(destination))
bpy.context.scene.render.image_settings.file_format = 'PNG'

print("bpy.context.area.type = "+bpy.context.area.type)
klods = bpy.data.objects['PD10003660 K-ROOF TILE 2X2 45 INV']
klodsrotation = klods.rotation_euler
for i in range(1):
	klods.rotation_euler= (klodsrotation.x+11,klodsrotation.y+12, klodsrotation.z+13)
	bpy.ops.ptcache.bake({"point_cache": bpy.context.scene.rigidbody_world.point_cache}, bake=True)
	num_files_pre = num_files_pre+1
	bpy.context.scene.render.filepath = os.path.join(destination, 'sim_render'+str(num_files_pre)+'.png')
	bpy.context.scene.frame_current = 200
	bpy.ops.render.render(write_still = True, use_viewport=True)
	bpy.ops.ptcache.free_bake({"point_cache": bpy.context.scene.rigidbody_world.point_cache})
