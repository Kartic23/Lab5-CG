from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader
import random
import OpenGL.GL as GL

class Mesa(Geometry):

    def __init__(self):
        super().__init__()
        r = my_obj_reader('Obj/mesa.obj')
        position_data = r[0]
        uv_data = r[1]
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()

