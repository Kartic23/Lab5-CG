import numpy as np
import math

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from geometry.garfo import Garfo
from geometry.chao import Chao
from geometry.parede import Parede
from geometry.mesa import Mesa
from geometry.rolo import Rolo
from geometry.prato import Prato
from geometry.faca_baixo import Faca_Baixo
from geometry.faca_cima import Faca_Cima
from geometry.colher import Colher
from material.surface import SurfaceMaterial



from material.texture import TextureMaterial
from core_ext.texture import Texture




class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([3, 2, -1])
        self.scene.add(self.rig)
        axes = AxesHelper(axis_length=0)
        self.scene.add(axes)
        grid = GridHelper(size=20,grid_color=[1, 1, 1],center_color=[1, 1, 1])
        grid.rotate_x(-math.pi / 2)
        self.scene.add(grid)

        chao = Chao()
        grid_texture_chao = Texture(file_name="images/branco.jpg",value=0)
        material_chao = TextureMaterial(texture=grid_texture_chao)
        self.mesh_chao = Mesh(geometry=chao, material=material_chao,texture=grid_texture_chao,value=0)
        self.scene.add(self.mesh_chao)

        self.garfo = Garfo()
        self.grid_texture_garfo = Texture(file_name="images/metal.jpg",value=1)
        self.material_garfo = TextureMaterial(texture=self.grid_texture_garfo)
        self.mesh_garfo = Mesh(geometry=self.garfo, material=self.material_garfo,texture=self.grid_texture_garfo,value=1)
        self.scene.add(self.mesh_garfo)

    

        parede = Parede()
        grid_texture_parede = Texture(file_name="images/verde.jpg",value=2)
        material_parede = TextureMaterial(texture=grid_texture_parede)
        self.mesh_parede = Mesh(geometry=parede, material=material_parede,texture=grid_texture_parede,value=2)
        self.scene.add(self.mesh_parede)

        mesa = Mesa()
        grid_texture_mesa = Texture(file_name="images/preto.jpg",value=3)
        material_mesa = TextureMaterial(texture=grid_texture_mesa)
        self.mesh_mesa = Mesh(geometry=mesa,material=material_mesa,texture=grid_texture_mesa,value=3)
        self.scene.add(self.mesh_mesa)
        
        rolo = Rolo()
        grid_texture_rolo = Texture(file_name="images/madeira.jpg",value=4)
        material_rolo = TextureMaterial(texture=grid_texture_rolo)
        self.mesh_rolo = Mesh(geometry=rolo,material=material_rolo,texture=grid_texture_rolo,value=4)
        self.scene.add(self.mesh_rolo)

        prato = Prato()
        grid_texture_prato = Texture(file_name="images/branco.jpg",value=5)
        material_prato = TextureMaterial(texture=grid_texture_prato)
        self.mesh_prato = Mesh(geometry=prato,material=material_prato,texture=grid_texture_prato,value=5)
        self.scene.add(self.mesh_prato)

        faca_baixo = Faca_Baixo()
        grid_texture_faca_baixo = Texture(file_name="images/madeira.jpg",value=6)
        material_faca_baixo = TextureMaterial(texture=grid_texture_faca_baixo)
        self.mesh_faca_baixo  = Mesh(geometry=faca_baixo,material=material_faca_baixo,texture=grid_texture_faca_baixo ,value=6)
        self.scene.add(self.mesh_faca_baixo )

        faca_cima = Faca_Cima()
        grid_texture_faca_cima  = Texture(file_name="images/metal.jpg",value=7)
        material_faca_cima = TextureMaterial(texture=grid_texture_faca_cima )
        self.mesh_faca_cima  = Mesh(geometry=faca_cima,material=material_faca_cima ,texture=grid_texture_faca_cima  ,value=7)
        self.scene.add(self.mesh_faca_cima)

        colher = Colher()
        grid_texture_colher  = Texture(file_name="images/metal.jpg",value=7)
        material_faca_colher = TextureMaterial(texture=grid_texture_colher )
        self.mesh_colher  = Mesh(geometry=colher,material=material_faca_colher ,texture=grid_texture_colher  ,value=7)
        self.scene.add(self.mesh_colher)
      
        


    
    def update(self):
        self.rig.update(self.input, self.delta_time)
        if self.input.is_key_pressed('p'):
            self.mesh_garfo.translate(0.025,0,0)
        if self.input.is_key_pressed('l'):
            self.mesh_garfo.translate(-0.025,0,0)
        
        if self.input.is_key_pressed('o'):
            self.mesh_garfo.translate(0,0.025,0)
        if self.input.is_key_pressed('k'):
            self.mesh_garfo.translate(0,-0.025,0)

        if self.input.is_key_pressed('i'):
            self.mesh_garfo.translate(0,0,0.025)
        if self.input.is_key_pressed('j'):
            self.mesh_garfo.translate(0,0,-0.025)

        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
