# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGibble(RPackage):
	"""Geometry Decomposition

	Build a map of path-based geometry, this is a simple description of the number
 of parts in an object and their basic structure. Translation and restructuring operations for 
 planar shapes and other hierarchical types require a data model with a record of the underlying
 relationships between elements. The gibble() function creates a geometry map, a simple record of 
 the underlying structure in path-based hierarchical types. There are methods for the planar shape 
 types in the 'sf' and 'sp' packages and for types in the 'trip' and 'silicate' packages. 
	"""
	
	homepage = "https://github.com/mdsumner/gibble"
	cran = "gibble" 

	version("0.4.0", md5="fdef848cde371bc449785c12cb8fa9f7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
