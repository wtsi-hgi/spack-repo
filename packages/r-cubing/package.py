# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubing(RPackage):
	"""Rubik's Cube Solving

	Functions for visualizing, animating, solving and 
        analyzing the Rubik's cube. Includes data structures for
		solvable and unsolvable cubes, random moves and random 
		state scrambles and cubes, 3D displays and animations 
		using 'OpenGL', patterned cube generation, and lightweight 
		solvers. See Rokicki, T. (2008) <arXiv:0803.3435> for the
		Kociemba solver.
	"""
	
	cran = "cubing" 

	version("1.0-5", md5="32584a1cf169d62a675153b464321103")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
