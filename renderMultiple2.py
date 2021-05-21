import os, bpy
bpy.context.scene.render.image_settings.file_format = 'PNG'
r = 10

#klodsImageWidth =  (bpy.context.scene.render.border_max_x) - bpy.context.scene.render.border_min_x
bpy.context.scene.render.use_crop_to_border = True

for i in range(r):
    ivalue = ((i+1)/r)
    print('i is now'+str(i))
    bpy.data.materials["klods_mat.001"].node_tree.nodes["Klods_PrincipledBSDF"].inputs["Subsurface"].default_value = ivalue
    
    for j in range(r):
        #jvalue = ((j+1)/r)+0.3
        #bpy.context.scene.cycles.film_exposure = jvalue
        bpy.data.materials["klods_mat.001"].node_tree.nodes["Klods_PrincipledBSDF"].inputs["Roughness"].default_value = j/20
        bpy.context.scene.render.filepath =     "C:/Users/NBK/Documents/BlenderOuput/img_high_rough/renderTest_prop_brooftile_SS"+str(int(ivalue*10))+"expo0"+str(int( j*20 ))
        bpy.ops.render.render(write_still = True, use_viewport=True)