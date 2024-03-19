from numpy.linalg import inv

from core.matrix import Matrix
from core_ext.object3d import Object3D


class Camera(Object3D):
    """  Represents the virtual camera used to view the scene """
    def __init__(self, angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        super().__init__()
        self._projection_matrix = Matrix.make_perspective(angle_of_view, aspect_ratio, near, far)
        self._view_matrix = Matrix.make_identity()

    @property
    def projection_matrix(self):
        return self._projection_matrix

    @property
    def view_matrix(self):
        return self._view_matrix

    def update_view_matrix(self):
        self._view_matrix = inv(self.global_matrix)