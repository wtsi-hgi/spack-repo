# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcube(RPackage):
	"""Simulations and Visualizations of Rubik's Cube (with Mods)

	Provides simplified methods for managing classic Rubik's cubes and many other modifications of it (such as NxNxN size cubes, void cubes and 8-coloured cubes - so called octa cubes). Includes functions of handling special syntax for managing such cubes; and different approach to plotting 3D cubes without using external libraries (for example 'OpenGL').
	"""
	
	cran = "rcube" 

	version("0.5", md5="09fb961c1d5c1519a4772adaf48303c0")

	depends_on("r-magrittr", type=("build", "run"))
