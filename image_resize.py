# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy


bl_info = {
    "name": "Image Resize",
    "author": "todashuta",
    "version": (1, 2, 0),
    "blender": (2, 80, 0),
    "location": "Image Editor > Sidebar > Tool > Image Resize",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Image"
}


class IMAGE_RESIZE_OT_width_mul2(bpy.types.Operator):
    bl_idname = "image.resize_ex_width_mul2"
    bl_label = "*2"
    bl_description = "*2"

    @classmethod
    def poll(cls, context):
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        scene.image_resize_addon_width = scene.image_resize_addon_width * 2

        return {"FINISHED"}


class IMAGE_RESIZE_OT_height_mul2(bpy.types.Operator):
    bl_idname = "image.resize_ex_height_mul2"
    bl_label = "*2"
    bl_description = "*2"

    @classmethod
    def poll(cls, context):
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        scene.image_resize_addon_height = scene.image_resize_addon_height * 2

        return {"FINISHED"}


class IMAGE_RESIZE_OT_width_div2(bpy.types.Operator):
    bl_idname = "image.resize_ex_width_div2"
    bl_label = "/2"
    bl_description = "/2"

    @classmethod
    def poll(cls, context):
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        scene.image_resize_addon_width = scene.image_resize_addon_width / 2

        return {"FINISHED"}


class IMAGE_RESIZE_OT_height_div2(bpy.types.Operator):
    bl_idname = "image.resize_ex_height_div2"
    bl_label = "/2"
    bl_description = "/2"

    @classmethod
    def poll(cls, context):
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        scene.image_resize_addon_height = scene.image_resize_addon_height / 2

        return {"FINISHED"}


class IMAGE_RESIZE_OT_getcurrentsize(bpy.types.Operator):
    bl_idname = "image.resize_ex_getcurrentsize"
    bl_label = "Get Current Size"
    bl_description = "Get Current Size"

    @classmethod
    def poll(cls, context):
        #for area in context.screen.areas:
        #    if area.type == "IMAGE_EDITOR":
        #        if area.spaces.active.image is not None:
        #            print("active", area.spaces.active.image)
        #            print("ctx", context.space_data.image)
        #            return True
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        scene.image_resize_addon_width, scene.image_resize_addon_height = image.size

        return {"FINISHED"}


class IMAGE_RESIZE_OT_main(bpy.types.Operator):
    bl_idname = "image.resize_ex_main"
    bl_label = "Image Resize"
    bl_description = "Image Resize"

    @classmethod
    def poll(cls, context):
        #for area in context.screen.areas:
        #    if area.type == "IMAGE_EDITOR":
        #        if area.spaces.active.image is not None:
        #            print("active", area.spaces.active.image)
        #            print("ctx", context.space_data.image)
        #            return True
        if hasattr(context.space_data, "image"):
            if context.space_data.image is not None:
                return True
        return False

    def execute(self, context):
        scene = context.scene
        image = context.space_data.image
        width, height = scene.image_resize_addon_width, scene.image_resize_addon_height
        image.scale(width, height)
        bpy.ops.image.resize()

        return {"FINISHED"}


class IMAGE_RESIZE_PT_panel(bpy.types.Panel):
    bl_label = "Image Resize"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.operator(IMAGE_RESIZE_OT_getcurrentsize.bl_idname)
        split = layout.split(factor=0.6)
        split.prop(scene, "image_resize_addon_width")
        split.operator(IMAGE_RESIZE_OT_width_div2.bl_idname, text="/2")
        split.operator(IMAGE_RESIZE_OT_width_mul2.bl_idname, text="*2")
        split = layout.split(factor=0.6)
        split.prop(scene, "image_resize_addon_height")
        split.operator(IMAGE_RESIZE_OT_height_div2.bl_idname, text="/2")
        split.operator(IMAGE_RESIZE_OT_height_mul2.bl_idname, text="*2")
        layout.operator(IMAGE_RESIZE_OT_main.bl_idname)


classes = [
        IMAGE_RESIZE_OT_width_mul2,
        IMAGE_RESIZE_OT_height_mul2,
        IMAGE_RESIZE_OT_width_div2,
        IMAGE_RESIZE_OT_height_div2,
        IMAGE_RESIZE_OT_getcurrentsize,
        IMAGE_RESIZE_OT_main,
        IMAGE_RESIZE_PT_panel,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.image_resize_addon_width  = bpy.props.IntProperty(name="Width")
    bpy.types.Scene.image_resize_addon_height = bpy.props.IntProperty(name="Height")


def unregister():
    if hasattr(bpy.types.Scene, "image_resize_addon_width"):
        del bpy.types.Scene.image_resize_addon_width
    if hasattr(bpy.types.Scene, "image_resize_addon_height"):
        del bpy.types.Scene.image_resize_addon_height

    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
