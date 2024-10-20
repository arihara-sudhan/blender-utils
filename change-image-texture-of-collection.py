"""
  GOAL : TO CHANGE IMAGE OF COLLECTION
"""
import bpy
image_path = "/Users/ari/Downloads/saree-images/saree1.jpeg"
new_image = bpy.data.images.load(image_path)
collection_name = "SAREE"
collection = bpy.data.collections.get(collection_name)

if collection is None:
    print(f"Collection '{collection_name}' not found!")
else:
    for obj in collection.objects:
        if obj.type == 'MESH':
            for mat in obj.data.materials:
                if mat and mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE':
                            node.image = new_image
                            print(f"Updated image in material '{mat.name}' of object '{obj.name}'")
