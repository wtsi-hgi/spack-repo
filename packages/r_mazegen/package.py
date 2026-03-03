# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazegen(RPackage):
	"""Elithorn Maze Generator

	A maze generator that creates the Elithorn Maze (HTML file) and the functions to calculate the associated maze parameters (i.e. Difficulty and Ability). 
	"""
	
	cran = "mazeGen" 

	version("0.1.3", md5="007ad459a9297549135625e5a7c48913")

	depends_on("r-igraph", type=("build", "run"))
