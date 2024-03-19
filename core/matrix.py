"""Matrix class containing the static methods to create numpy matrices."""

from math import sin, cos, tan, pi
import numpy as np

class Matrix(object):
    """Contains the static methods to generate the matrices for identity, 
    translation, rotation (around each axis), scaling, and projection transforms."""

    @staticmethod
    def make_identity():
        """Numpy array containing the identity matrix"""
        return np.array( [[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]] ).astype(float)

    @staticmethod
    def make_translation(x, y, z):
        """Numpy array containing the translation matrix"""
        return np.array([[1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_rotation_x(angle):
        """Numpy array containing the matrix to rotate around x-axis"""
        c = cos(angle)
        s = sin(angle)
        return np.array([[1,  0,  0,  0],
                            [0,  c, -s,  0],
                            [0,  s,  c,  0],
                            [0,  0,  0,  1]]).astype(float)

    @staticmethod
    def make_rotation_y(angle):
        """Numpy array containing the matrix to rotate around y-axis"""
        c = cos(angle)
        s = sin(angle)
        return np.array([[c,  0,  s,  0],
                            [0,  1,  0,  0],
                            [-s, 0,  c,  0],
                            [0,  0,  0,  1]]).astype(float)

    @staticmethod
    def make_rotation_z(angle):
        """Numpy array containing the matrix to rotate around z-axis"""
        c = cos(angle)
        s = sin(angle)
        return np.array([[c, -s,  0,  0],
                            [s,  c,  0,  0],
                            [0,  0,  1,  0],
                            [0,  0,  0,  1]]).astype(float)

    @staticmethod
    def make_scale(s):
        """Numpy array containing the scaling matrix"""
        return np.array([[s, 0, 0, 0],
                            [0, s, 0, 0],
                            [0, 0, s, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_perspective(angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        """Numpy array containing the perspective projetion matrix"""
        a = angle_of_view * pi / 180.0
        d = 1.0 / tan(a / 2)
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array([[d / aspect_ratio, 0, 0, 0],
                            [0, d, 0, 0],
                            [0, 0, b, c],
                            [0, 0, -1, 0]]).astype(float)