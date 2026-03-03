# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZonohedra(RPackage):
	"""Compute and Plot Zonohedra from Vector Generators

	Computes a zonohedron from real vector generators.  The package also computes zonogons (2D zonotopes) and zonosegs (1D zonotopes).  An elementary S3 class for matroids is included, which supports matroids with rank 3, 2, and 1.  Optimization methods are taken from Heckbert (1985) <https://www.cs.cmu.edu/~ph/zono.ps.gz>. 
	"""
	
	cran = "zonohedra" 

	version("0.2-2", md5="58e3f5510857b13a56a66257f70902a2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
