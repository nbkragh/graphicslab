import os, bpy
bpy.context.scene.render.filepath = os.path.join('C:/Users/NBK/Desktop/projektklodser/BlenderOuput', 'renderTest1.jpg')
bpy.context.scene.render.image_settings.file_format = 'JPG'
bpy.ops.render.render(write_still = True, use_viewport=True)