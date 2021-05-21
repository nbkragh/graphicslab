import os, bpy
bpy.context.scene.render.image_settings.file_format = 'PNG'
r = 10

#klodsImageWidth =  (bpy.context.scene.render.border_max_x) - bpy.context.scene.render.border_min_x
bpy.context.scene.render.use_crop_to_border = True

for i in range(r):
    
    print('i is now'+str(i))
    bpy.data.materials["klods_mat"].node_tree.nodes["Klods_PrincipledBSDF"].inputs["Subsurface"].default_value = i/10
    
    for j in range(r):
        bpy.data.materials["klods_mat"].node_tree.nodes["Klods_PrincipledBSDF"].inputs["Roughness"].default_value = j/10
        bpy.context.scene.render.filepath =     "C:/Users/NBK/Desktop/projektklodser/BlenderOuput/img/renderTest_SS"+str(i)+"R"+str(j)
        bpy.ops.render.render(write_still = True, use_viewport=True)