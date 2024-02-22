# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShaperotator(RPackage):
	"""Standardised Rigid Rotations of Articulated Three-Dimensional
Structures

	Here we describe a simple geometric rigid rotation approach that removes the effect of random translation and rotation, enabling the morphological analysis of 3D articulated structures. Our method is based on Cartesian coordinates in 3D space so it can be applied to any morphometric problem that also uses 3D coordinates. See Vidal-García, M., Bandara, L., Keogh, J.S. (2018) <doi:10.1002/ece3.4018>.
	"""
	
	homepage = "https://github.com/marta-vidalgarcia/ShapeRotator"
	cran = "ShapeRotator" 

	version("0.1.0", md5="5b67d31ea2252af9552e1d73ec131422")

	depends_on("r-plot3d", type=("build", "run"))
