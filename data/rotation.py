#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
rotation.py
Rotation is a module designed to organize the three basic
rotation matrices in three dimensions, according to 
https://en.wikipedia.org/wiki/Rotation_matrix#Basic_rotations.
It is based on numpy arrays.
Context examples:
The unit vector in the direction of the x axis
of a three dimensional Cartesian coordinate system
is written as np.array([1, 0, 0]).
The identity amtrix of size 3 is written as
np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Rotation example:
# TODO 
Rotate hat(i) to get hat(k).
"""

import numpy as np

# Basic rotation

def R_x(angle):
    """Rotation matrix by given angle in radians about x-axis."""
    cos = np.cos(angle)
    sin = np.sin(angle)
    R_x_angle = np.array(
        [
            [1, 0, 0],
            [0, cos, -sin],
            [0, sin, cos]
        ]
    )
    return R_x_angle

def R_y(angle):
    """Rotation matrix by given angle in radians about y-axis."""
    cos = np.cos(angle)
    sin = np.sin(angle)
    R_y_angle = np.array(
        [
            [cos, 0, sin],
            [0, 1, 0],
            [-sin, 0, cos]
        ]
    )
    return R_y_angle

def R_z(angle):
    """Rotation matrix by given angle in radians about z-axis."""
    cos = np.cos(angle)
    sin = np.sin(angle)
    R_z_angle = np.array(
        [
            [cos, -sin, 0],
            [sin, cos, 0],
            [0, 0, 1]
        ]
    )
    return R_z_angle

# General rotation

def cartesian_rotation(vector, x_angle, y_angle, z_angle):
    """
    Rotate a given vector in a three dimensional Cartesian coordinate system
    by given angles in radians about each axis.
    """
    R_vector = np.matmul(
        R_z(z_angle), np.matmul(
            R_y(y_angle), np.matmul(
                R_x(x_angle), vector
            )
        )
    )
    return R_vector

def normalize(vector):
    norm = np.linalg.norm(vector, ord = 2)
    return vector / norm

def axis_rotation(vector, angle, axis):
    """
    Rotate a given vector by given angle in radians about given axis.
    The axis is defined by a unit vector.
    """

    unit_vector = normalize(axis)

    cos = np.cos(angle)
    sin = np.sin(angle)

    ux,uy,uz = unit_vector

    R = np.array(
        [
            [cos+(1-cos)*ux**2, ux*uy*(1-cos)-uz*sin, ux*uz*(1-cos)+uy*sin],
            [uy*ux*(1-cos)+uz*sin, cos+(1-cos)*uy**2, uy*uz*(1-cos)-ux*sin],
            [uz*ux*(1-cos)-uy*sin, uz*uy*(1-cos)+ux*sin, cos+(1-cos)*uz**2]
        ]
    )

    R_vector = np.matmul(
        R, vector
    )
    return R_vector

def orthographic_projection(vector3D, z):
    """
    Project 3D vector into 2D vector
    It is perspective_projection with FOV = np.pi/2
    """
    projection_matrix = np.array(
        [
            [z, 0, 0],
            [0, z, 0]
        ]
    )
    vector2D = np.matmul(
        projection_matrix, vector3D
    )
    return vector2D

def perspective_projection(vector, near, far, FOV = 2*np.pi/3, AR = 1):
    """
    Project 3D into 2D with perspective.
    
    Parameters
    ----------
    vector : array_like
        Input vector array.
    near : float
        Distance to the near clipping plane along the z-axis.
    far : float
        Distance to the far clipping plane along the z-axis.
    FOV : float
        Field of view.
        The angle between the upper and lower sides of the viewing frustum.
    AR : float
        The aspect ratio of the viewing window (width/height).
    Returns
    -------
    projected_vector : array_like
        Output vector array.
    """

    # perspective_matrix = np.array(
    #     [
    #         [1, 0, 0, 0],
    #         [0, 1, 0, 0],
    #         [0, 0, 1, 0],
    #         [0, 0, -1, 0]
    #     ]
    # )

    perspective_matrix = np.array(
        [
            [1/(AR*np.tan(FOV/2)), 0, 0, 0],
            [0, 1/np.tan(FOV/2), 0, 0],
            [0, 0, (near+far)/(near-far), 2*(near+far)/(near-far)],
            [0, 0, -1, 0]
        ]
    )

    aux_vector = np.matmul(
        perspective_matrix, vector
    )

    w = aux_vector[2] / near

    projected_vector = aux_vector / w

    projected_vector = projected_vector[:2]

    return projected_vector