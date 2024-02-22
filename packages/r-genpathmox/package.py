# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenpathmox(RPackage):
	"""Pathmox Approach Segmentation Tree Analysis

	It provides an interesting solution for handling a high number 
	of segmentation variables in partial least squares structural equation 
	modeling. The package implements the "Pathmox" algorithm (Lamberti, Sanchez, 
	and Aluja,(2016)<doi:10.1002/asmb.2168>) including the F-coefficient 
	test (Lamberti, Sanchez, and Aluja,(2017)<doi:10.1002/asmb.2270>) 
	to detect the path coefficients responsible for the identified differences). 
	The package also allows running the hybrid multi-group approach (Lamberti (2021) 
	<doi:10.1007/s11135-021-01096-9>).
	"""
	
	cran = "genpathmox" 

	version("1.1", md5="3159c1a3117cf428f4ca84d7b2f7de67")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-csem", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
