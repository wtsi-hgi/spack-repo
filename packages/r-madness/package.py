# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadness(RPackage):
	"""Automatic Differentiation of Multivariate Operations

	An object that supports automatic differentiation
    of matrix- and multidimensional-valued functions with 
    respect to multidimensional independent variables. 
    Automatic differentiation is via 'forward accumulation'.
	"""
	
	homepage = "https://github.com/shabbychef/madness"
	cran = "madness" 

	version("0.2.8", md5="c608f85adf2ccea87e9163aec257f2ef")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
